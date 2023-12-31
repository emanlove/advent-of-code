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

    def find_next_reflector(self, pos, heading):
        reflectors = self.reflectors
        ncols = self.ncols
        nrows = self.nrows
        
        print(f"Looking from {pos} heading {heading}..")
        match heading:
            case "left":
                # indices of points to the left
                # range(pos, beginning of this row-1, -1)
                # range(pos-1, (pos//NCOLS)*NCOLS)-1, -1)
                path = range(pos-1, ((pos//ncols)*ncols)-1, -1)
                ignore = ['-']
            case "right":
                # indices of points to the right
                # range(pos+1, (pos//NCOLS+1)*NCOLS), +1)
                path = range(pos+1, (pos//ncols+1)*ncols, +1)  # indices of points to the right
                ignore = ['-']
            case "up":
                # indices of points upward
                # !! - incorrect !!
                # range(row above, 0, -num of cols)
                # range(pos-NCOLS, 0, -NCOLS)
                # ---------------------------
                # range(row above, col in first row, -num of cols)
                # range(pos-NCOLS, pos%NCOLS, -NCOLS)
                path = range(pos-ncols, pos%ncols, -ncols)  # indices of points upward
                ignore = ['|']
            case "down":
                # indices of points downward
                # !! - incorrect !!
                # range(row below, num of rows, +num of cols)
                # range(pos+NCOLS, NROWS, +NCOLS)
                # ---------------------------
                # range(row below, col in last row, +num of cols)
                # range(pos+NCOLS, ((nrows-1)*ncols)+pos%NCOLS, +NCOLS)
                path = range(pos+ncols, ((nrows-1)*ncols)+(pos%ncols), +ncols)  # indices of points downward
                ignore = ['|']

        print(f".. searching path {path}/{list(path)} and ignoring {ignore}")
        for indx,step in enumerate(path):
            if (step in reflectors) and reflectors[step][TYPE] not in ignore:
                traversed = path[:indx+1]
                next_reflector = step
                self.remove_beam_from_reflector(pos, heading)

                # return next reflector
                print(f".. found next reflector. {next_reflector}  {reflectors[next_reflector][TYPE]}")
                return next_reflector, traversed

        # return next reflector as None since there is not one
        traversed = path
        next_reflector = None
        self.remove_beam_from_reflector(pos, heading)

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
            print(f"Found repeated beam: {pos}  {heading_towards}")
            return

        # note incoming beam so we don't repeat in future
        self.record_beam(pos, heading_towards)

        type = reflectors[pos][TYPE]
        print(f"Reflecting beam at {pos} heading towards {heading_towards} with {type}..")
        match type:
            case '|':
                match heading_towards:
                    case "left" | "right":
                        # split up and down
                        self.add_beam(pos, UP)
                        self.add_beam(pos, DOWN)
                    case _:
                        print(f"!!WARNING!! Should not be approching | ({pos}) from {heading_towards}")
            case '-':
                match heading_towards:
                    case "up" | "down":
                        # split left and right
                        self.add_beam(pos, LEFT)
                        self.add_beam(pos, RIGHT)
                    case _:
                        print(f"!!WARNING!! Should not be approching - ({pos}) from {heading_towards}")
            case '\\':
                match heading_towards:
                    case "left":
                        # reflect up
                        self.add_beam(pos, UP)
                    case "right":
                        # reflect down
                        self.add_beam(pos, DOWN)
                    case "up":
                        # reflect left
                        self.add_beam(pos, LEFT)
                    case "down":
                        # reflect right
                        self.add_beam(pos, RIGHT)
            case '/':
                match heading_towards:
                    case "left":
                        # reflect down
                        self.add_beam(pos, DOWN)
                    case "right":
                        # reflect up
                        self.add_beam(pos, UP)
                    case "up":
                        # reflect right
                        self.add_beam(pos, RIGHT)
                    case "down":
                        # reflect left
                        self.add_beam(pos, LEFT)

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
        self.all_tiles_energized = [0]

        # trace to initial reflector
        next_reflector, tiles_traversed = self.find_next_reflector(0, RIGHT)
        self.all_tiles_energized.append(tiles_traversed)
        if next_reflector:
            self.reflect_beam(next_reflector, RIGHT)

        # while any beams
        while any(reflectors[pnt][BEAMS] for pnt in reflectors):
            for rindx in reflectors:
                for heading in reflectors[rindx][BEAMS]:
                    next_reflector, tiles_traversed = self.find_next_reflector(rindx, heading)
                    self.all_tiles_energized.append(tiles_traversed)
                    if next_reflector:
                        self.reflect_beam(next_reflector, heading)

        # count up number of tiles
        tiles_energized = len(set(self.all_tiles_energized))

        print(f"The number of tiles end up being energized is {tiles_energized}")


if __name__ == "__main__":
    file = sys.argv[1]

    ctrap = Contraption()
    ctrap.read_contraption(file)
    ctrap.shine_light()
