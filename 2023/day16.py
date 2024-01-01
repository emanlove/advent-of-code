import sys

TYPE  = 'type'
LEFT  = 'left'
RIGHT = 'right'
UP    = 'up'
DOWN  = 'down'
BEAMS = 'beams'

class Contraption():
    def __init__(self) -> None:
        self.reflectors = {}
        self.ncols = None
        self.nrows = None
        self.flattened_contraption = None

    def reset_contraption(self):
        self.next_reflector_beams = {}
        self.all_tiles_energized = []

        for coord,tile in enumerate(self.flattened_contraption):
            if tile != '.':
                self.reflectors[coord] = {}
                self.reflectors[coord][TYPE] = tile
                self.reflectors[coord][LEFT] = False
                self.reflectors[coord][RIGHT] = False
                self.reflectors[coord][UP] = False
                self.reflectors[coord][DOWN] = False
                self.reflectors[coord][BEAMS] = []

        for rindx in self.reflectors:
            self.next_reflector_beams[rindx] = []

    def read_contraption(self, filename):
        with open(filename,'r') as fh:
            lines = [line.rstrip('\n') for line in fh]
    
        self.flattened_contraption = ''.join(lines)

        self.ncols = len(lines[0])
        self.nrows = len(lines)

        self.reset_contraption()

    def find_next_reflector(self, pos, heading, initial=False):
        """ Find the next reflector along a path
        
            Starting at `pos` and traveling in the direction of `heading` look
            for any reflectors that should not be ignored. That is, ignored reflectors
            are those splitters approached from the "pointy ends". If `initial` is True
            then instead of starting at the next tile, the path starts on the tile
            provided in `pos`. Note this method does not check that if `initial` is true
            that `pos` is an edge tile. It just will do what you ask.

            About the paths:
            As our map is flattened the travering in a path or along a row or column
            is a bit more complicated then just increasing or decreasing the current
            row and column. Instead if we are heading left then we want to generate a
            path heading towards the beginning of a row. We start at the tile to our
            left or current position minus one. Our step increment is minis one as we
            are traversing down the flattened grid. The end of path or start of the
            row is calculated as the floor division of position by number of columns.
            Remembering that range is up to but not including we want to subtract one
            from the start of the row. So for the path to the left we have

                path = range(pos-1, ((pos//ncols)*ncols)-1, -1)     # left

            For paths heading right we step plus one and start to the tile to the right.
            The end of the row plus one (or end of the path right) is floor division of
            position by number of cols plus one and times the number of cols. Thus,

                path = range(pos+1, (pos//ncols+1)*ncols, +1)       # right

            For up and down we start with and step by minus or plus the number of
            columns, respectively. For up, the end of path is the current column minus
            the number of columns.  (Remember for range we want to extend the end out
            beyond the first row thus the minus number of columns). With down the end
            of path is the total number of coordinates plus the current column. We have
            then,

                path = range(pos-ncols, (pos%ncols)-ncols, -ncols)  # up

                path = range(pos+ncols, (nrows*ncols)+(pos%ncols), +ncols)  # down
        """
        reflectors = self.reflectors
        ncols = self.ncols
        nrows = self.nrows
        
        # print(f"Looking from {pos} heading {heading}..")
        match heading:
            case "left":
                # indices of points to the left
                start = pos if initial else pos-1
                path = range(start, ((pos//ncols)*ncols)-1, -1)
                ignore = ['-']
            case "right":
                # indices of points to the right
                start = pos if initial else pos+1
                path = range(start, (pos//ncols+1)*ncols, +1)
                ignore = ['-']
            case "up":
                # indices of points upward
                start = pos if initial else pos-ncols
                path = range(start, (pos%ncols)-ncols, -ncols)
                ignore = ['|']
            case "down":
                # indices of points downward
                start = pos if initial else pos+ncols
                path = range(start, (nrows*ncols)+(pos%ncols), +ncols)
                ignore = ['|']

        # print(f".. searching path {path}/{list(path)} and ignoring {ignore}")
        for indx,step in enumerate(path):
            if (step in reflectors) and reflectors[step][TYPE] not in ignore:
                traversed = list(path[:indx+1])
                next_reflector = step
                # print(f".. found next reflector. {next_reflector}  {reflectors[next_reflector][TYPE]}")
                return next_reflector, traversed

        # return next reflector as None since there is not one
        traversed = list(path)
        next_reflector = None

        return next_reflector, traversed

    def reflect_beam(self, pos, heading_towards):
        reflectors = self.reflectors

        # if beam coming into this reflector has arrived from same direction before
        # then don't reflect back out (as this would be looping the light)
        if reflectors[pos][heading_towards]:
            # print(f"Found repeated beam: {pos}  {heading_towards}")
            return []

        # note incoming beam so we don't repeat in future
        self.record_beam(pos, heading_towards)

        type = reflectors[pos][TYPE]
        # print(f"Reflecting beam at {pos} heading towards {heading_towards} with {type}..")
        match type:
            case '|':
                match heading_towards:
                    case "left" | "right":
                        # split up and down
                        return [UP, DOWN]
                    case _:
                        print(f"!!WARNING!! Should not be approching | ({pos}) from {heading_towards}")
            case '-':
                match heading_towards:
                    case "up" | "down":
                        # split left and right
                        return [LEFT, RIGHT]
                    case _:
                        print(f"!!WARNING!! Should not be approching - ({pos}) from {heading_towards}")
            case '\\':
                match heading_towards:
                    case "left":
                        # reflect up
                        return [UP]
                    case "right":
                        # reflect down
                        return [DOWN]
                    case "up":
                        # reflect left
                        return [LEFT]
                    case "down":
                        # reflect right
                        return [RIGHT]
            case '/':
                match heading_towards:
                    case "left":
                        # reflect down
                        return [DOWN]
                    case "right":
                        # reflect up
                        return [UP]
                    case "up":
                        # reflect right
                        return [RIGHT]
                    case "down":
                        # reflect left
                        return [LEFT]

    def update_beams(self):
        next_reflector_beams = self.next_reflector_beams
        reflectors = self.reflectors
        for rindx in next_reflector_beams:
            reflectors[rindx][BEAMS] = list(set(next_reflector_beams[rindx]))
            next_reflector_beams[rindx] = []

    def record_beam(self, pos, heading):
        reflectors = self.reflectors

        if reflectors[pos][heading]:
            print(f"!!WARNING!! Should have caught previously record beam. pos:{pos} heading:{heading}")
        
        reflectors[pos][heading] = True

    def shine_light(self, starting_pos=0, starting_dir=RIGHT):
        reflectors = self.reflectors
        # self.all_tiles_energized = [0]

        # trace to initial reflector
        next_reflector, tiles_traversed = self.find_next_reflector(starting_pos, starting_dir, initial=True)
        self.all_tiles_energized += tiles_traversed
        if next_reflector is not None:
            new_beams = self.reflect_beam(next_reflector, starting_dir)
            reflectors[next_reflector][BEAMS] = new_beams
        else:
            # count up number of tiles
            tiles_energized = len(set(self.all_tiles_energized))
            return tiles_energized


        # while any beams reflect around contraption
        while any(reflectors[pnt][BEAMS] for pnt in reflectors):
            for rindx in reflectors:
                all_new_beams = []
                for heading in reflectors[rindx][BEAMS]:
                    next_reflector, tiles_traversed = self.find_next_reflector(rindx, heading)
                    self.all_tiles_energized += tiles_traversed
                    if next_reflector:
                        new_beam = self.reflect_beam(next_reflector, heading)
                        self.next_reflector_beams[next_reflector] += new_beam
                # print(f"New beams heading out of {rindx}: {reflectors[rindx][BEAMS]}")
            # update beams heading out of the reflectors
            self.update_beams()
        # count up number of tiles
        tiles_energized = len(set(self.all_tiles_energized))

        # debug output
        # ate = list(set(self.all_tiles_energized))
        # print(f"{ate}")
        # nrows = self.nrows; ncols=self.ncols
        # ate_map = ['#' if i in ate else '.' for i in range(ncols*nrows)]
        # for r in range(nrows):
        #     print(''.join(ate_map[r*ncols:r*ncols+ncols]))

        return tiles_energized

if __name__ == "__main__":
    file = sys.argv[1]

    ctrap = Contraption()
    ctrap.read_contraption(file)
    tiles_energized = ctrap.shine_light()
    print(f"The number of tiles end up being energized is {tiles_energized}")

    # -- Part 2 -------
    # Reset contraption
    ctrap.reset_contraption()

    # Create list of starting positions and directions
    ncols = ctrap.ncols; nrows = ctrap.nrows
    from_the_top    = [(t,DOWN) for t in range(ncols)]
    from_the_left   = [(t,RIGHT) for t in range(0,ncols*nrows,ncols)]
    from_the_right  = [(t,LEFT) for t in range(ncols-1,ncols*nrows,ncols)]
    from_the_bottom = [(t,UP) for t in range((nrows-1)*ncols,ncols*nrows)]
    starting_tiles = from_the_top + from_the_left + from_the_right + from_the_bottom

    energized_by_start_pos= []
    for start in starting_tiles:
        # print(f"{start}")
        tiles_energized = ctrap.shine_light(starting_pos=start[0], starting_dir=start[1])
        energized_by_start_pos.append(tiles_energized)
        ctrap.reset_contraption()

    print(f"The largest number of tiles energized is {max(energized_by_start_pos)}")

