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
        self.next_reflector_beams = {}
        self.all_tiles_energized = []

    def read_contraption (self, filename):
        with open(filename,'r') as fh:
            lines = [line.rstrip('\n') for line in fh]
    
        flattened = ''.join(lines)

        self.ncols = len(lines[0])
        self.nrows = len(lines)

        for coord,tile in enumerate(flattened):
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

    def find_next_reflector(self, pos, heading):
        """ Find the next reflector along a path
        
            Starting at `pos` and traveling in the direction of `heading` look
            for any reflectors that should not be ignored. That is, ignored reflectors
            are those splitters approached from the "pointy ends".

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
                path = range(pos-1, ((pos//ncols)*ncols)-1, -1)
                ignore = ['-']
            case "right":
                # indices of points to the right
                if pos == -1:
                    path = range(0, ncols, +1)
                else:
                    path = range(pos+1, (pos//ncols+1)*ncols, +1)
                ignore = ['-']
            case "up":
                # indices of points upward
                path = range(pos-ncols, (pos%ncols)-ncols, -ncols)
                ignore = ['|']
            case "down":
                # indices of points downward
                path = range(pos+ncols, (nrows*ncols)+(pos%ncols), +ncols)
                ignore = ['|']

        # print(f".. searching path {path}/{list(path)} and ignoring {ignore}")
        for indx,step in enumerate(path):
            if (step in reflectors) and reflectors[step][TYPE] not in ignore:
                traversed = list(path[:indx+1])
                next_reflector = step
                # self.remove_beam_from_reflector(pos, heading)

                # return next reflector
                # print(f".. found next reflector. {next_reflector}  {reflectors[next_reflector][TYPE]}")
                return next_reflector, traversed

        # return next reflector as None since there is not one
        traversed = list(path)
        next_reflector = None
        # self.remove_beam_from_reflector(pos, heading)

        return next_reflector, traversed

    def remove_beam_from_reflector(self, indx, heading):
        # remove beam from reflector (conditional based upon pos in reflector - needed for initial start)
        reflectors = self.reflectors

        if indx in reflectors:
            beam_indx = reflectors[indx][BEAMS].index(heading)
            reflectors[indx][BEAMS].pop(beam_indx)


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
                        # self.add_beam(pos, UP)
                        # self.add_beam(pos, DOWN)
                    case _:
                        print(f"!!WARNING!! Should not be approching | ({pos}) from {heading_towards}")
            case '-':
                match heading_towards:
                    case "up" | "down":
                        # split left and right
                        return [LEFT, RIGHT]
                        # self.add_beam(pos, LEFT)
                        # self.add_beam(pos, RIGHT)
                    case _:
                        print(f"!!WARNING!! Should not be approching - ({pos}) from {heading_towards}")
            case '\\':
                match heading_towards:
                    case "left":
                        # reflect up
                        return [UP]
                        # self.add_beam(pos, UP)
                    case "right":
                        # reflect down
                        return [DOWN]
                        # self.add_beam(pos, DOWN)
                    case "up":
                        # reflect left
                        return [LEFT]
                        # self.add_beam(pos, LEFT)
                    case "down":
                        # reflect right
                        return [RIGHT]
                        # self.add_beam(pos, RIGHT)
            case '/':
                match heading_towards:
                    case "left":
                        # reflect down
                        return [DOWN]
                        # self.add_beam(pos, DOWN)
                    case "right":
                        # reflect up
                        return [UP]
                        # self.add_beam(pos, UP)
                    case "up":
                        # reflect right
                        return [RIGHT]
                        # self.add_beam(pos, RIGHT)
                    case "down":
                        # reflect left
                        return [LEFT]
                        # self.add_beam(pos, LEFT)

    def reset_next_reflector_beams(self):
        next_reflector_beams = self.next_reflector_beams
        reflectors = self.reflectors
        for rindx in next_reflector_beams:
            next_reflector_beams[rindex] = []

    def update_beams(self):
        next_reflector_beams = self.next_reflector_beams
        reflectors = self.reflectors
        for rindx in next_reflector_beams:
            reflectors[rindx][BEAMS] = list(set(next_reflector_beams[rindx]))
            next_reflector_beams[rindx] = []

    def add_beam(self, pos, going):
        reflectors = self.reflectors

        if going in reflectors[pos][BEAMS]:
            print(f"Note: Finding duplicate beams")            
            return
        
        reflectors[pos][BEAMS].append(going)

    def record_beam(self, pos, heading):
        reflectors = self.reflectors

        if reflectors[pos][heading]:
            print(f"!!WARNING!! Should have caught previously record beam. pos:{pos} heading:{heading}")
        
        reflectors[pos][heading] = True

    def shine_light(self):
        reflectors = self.reflectors
        # self.all_tiles_energized = [0]

        # trace to initial reflector
        # import pdb;pdb.set_trace()
        next_reflector, tiles_traversed = self.find_next_reflector(-1, RIGHT)
        self.all_tiles_energized += tiles_traversed
        new_beams = self.reflect_beam(next_reflector, RIGHT)
        reflectors[next_reflector][BEAMS] = new_beams
        # if next_reflector:
        #     new_beams = self.reflect_beam(next_reflector, RIGHT)
        #     reflectors[next_reflector][BEAMS] = new_beams

        # while any beams
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
        ate = list(set(self.all_tiles_energized))
        # print(f"{ate}")
        nrows = self.nrows; ncols=self.ncols
        ate_map = ['#' if i in ate else '.' for i in range(ncols*nrows)]
        for r in range(nrows):
            print(''.join(ate_map[r*ncols:r*ncols+ncols]))

        print(f"The number of tiles end up being energized is {tiles_energized}")


if __name__ == "__main__":
    file = sys.argv[1]

    ctrap = Contraption()
    ctrap.read_contraption(file)
    ctrap.shine_light()
