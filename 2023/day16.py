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
                # range(row above, 0, -num of cols)
                # range(pos-NCOLS, 0, -NCOLS)
                path = range(pos-ncols, 0, -ncols)  # indices of points upward
                ignore = ['|']
            case "down":
                # indices of points downward
                # range(row below, num of rows, +num of cols)
                # range(pos+NCOLS, NROWS, +NCOLS)
                path = range(pos+ncols, nrows, +ncols)  # indices of points downward
                ignore = ['|']

        for indx,step in enumerate(path):
            if (step in reflectors) and reflectors[step][type] not in ignore:
                traversed = path[:indx+1]
                next_reflector = step
                self.remove_beam_from_reflector(pos, heading)

                # return next reflector
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
            beam_indx = reflectors[indx][BEAMS].find(heading)
            reflectors[indx][BEAMS].pop(beam_indx)


    def reflect_beam(self, pos, coming_from):
        reflectors = self.reflectors

        # if beam coming into this reflector has arrived from same direction before
        # then don't reflect back out (as this would be looping the light)
        if reflectors[pos][coming_from]:
            return

        # note incoming beam so we don't repeat in future
        self.record_beam(pos, coming_from)

        type = reflectors[pos][TYPE]
        match type:
            case '|':
                match coming_from:
                    case "left" | "right":
                        # split up and down
                        self.add_beam(pos, UP)
                        self.add_beam(pos, DOWN)
                    case _:
                        print(f"!!WARNING!! Should not be approching | ({pos}) from {coming_from}")
            case '-':
                match coming_from:
                    case "up" | "down":
                        # split left and right
                        self.add_beam(pos, LEFT)
                        self.add_beam(pos, RIGHT)
                    case _:
                        print(f"!!WARNING!! Should not be approching - ({pos}) from {coming_from}")
            case '\':
                match coming_from:
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
                match coming_from:
                    case "left":
                        # reflect up
                        self.add_beam(pos, UP)
                    case "right":
                        # reflect down
                        self.add_beam(pos, DOWN)
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
            reflect_beam(next_reflector, RIGHT)

        # while any beams
        while any(reflectors[pnt][BEAMS] for pnt in reflectors):
            for reflector in reflectors:
                for heading in reflector[BEAMS]:
                    next_reflector, tiles_traversed = self.find_next_reflector(reflector, heading)
                    self.all_tiles_energized.append(tiles_traversed)
                    if next_reflector:
                        reflect_beam(next_reflector, heading)

        # count up number of tiles
        tiles_energized = len(set(self.all_tiles_energized))

        print(f"The number of tiles end up being energized is {tiles_energized}")


if __name__ == "__main__":
    file = sys.argv[1]

    ctrap = Contraption()
    ctrap.read_contraption(file)
    ctrap.shine_light()
