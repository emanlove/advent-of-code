import sys

def read_seating_chart(filename):
    with open(filename,'r') as fh:
        seating_chart = [line.rstrip('\n') for line in fh]

    return seating_chart

def get_surrounding_neighbor(seat,seats,nRows,nCols):
    row = int(seat/nCols)
    col = seat%nCols
    all_neighbors = []
    all_neighbors += [seat-nCols-1] if row>0 and col>0 else []
    all_neighbors += [seat-nCols] if row>0 else []
    all_neighbors += [seat-nCols+1] if row>0 and col<nCols-1 else []
    all_neighbors += [seat-1] if col>0 else []
    all_neighbors += [seat+1] if col<nCols-1 else []
    all_neighbors += [seat+nCols-1] if row<nRows-1 and col>0 else []
    all_neighbors += [seat+nCols] if row<nRows-1 else []
    all_neighbors += [seat+nCols+1] if row<nRows-1 and col<nCols-1 else []
    surrounding_neighbors_with_seats = [neighbor for neighbor in all_neighbors if neighbor in seats]

    return surrounding_neighbors_with_seats
    
def get_lineofsight_neighbor(seat,seats,nRows,nCols):
    row = int(seat/nCols)
    col = seat%nCols

    nearest_neighbors = []

    # direction 1
    if row>0 and col>0:
        steps_to_edge = min(row,col)
        line_of_sight_cords = list(zip(range(row-1,row-1-steps_to_edge,-1),range(col-1,col-1-steps_to_edge,-1)))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []
    # direction 2
    if row>0:
        steps_to_edge = row
        line_of_sight_cords = list(zip(range(row-1,row-1-steps_to_edge,-1),[col]*steps_to_edge))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []
    # direction 3
    if row>0 and col<nCols-1:
        steps_to_edge = min(row,nCols-col+1)
        line_of_sight_cords = list(zip(range(row-1,row-1-steps_to_edge,-1),range(col+1,nCols)))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []
    # direction 4
    if col>0:
        steps_to_edge = col
        line_of_sight_cords = list(zip([row]*steps_to_edge,range(col-1,col-1-steps_to_edge,-1)))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []
    # direction 5
    if col<nCols-1:
        steps_to_edge = nCols-col+1
        line_of_sight_cords = list(zip([row]*steps_to_edge,range(col+1,nCols)))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []
    # direction 6
    if row<nRows-1 and col>0:
        steps_to_edge = min(nRows-row+1,col)
        line_of_sight_cords = list(zip(range(row+1,nRows),range(col-1,col-1-steps_to_edge,-1)))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []
    # direction 7
    if row<nRows-1:
        steps_to_edge = nRows-row+1
        line_of_sight_cords = list(zip(range(row+1,nRows),[col]*steps_to_edge))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []
    # direction 8
    if row<nRows-1 and col<nCols-1:
        steps_to_edge = min(nRows-row+1,nCols-col+1)
        line_of_sight_cords = list(zip(range(row+1,nRows),range(col+1,nCols)))
        line_of_sight = [cord_pair[0]*nCols+cord_pair[1] for cord_pair in line_of_sight_cords]
        chairs_in_lineofsight = [chair for chair in line_of_sight if chair in seats]
        nearest_neighbors += [chairs_in_lineofsight[0]] if chairs_in_lineofsight else []

    return nearest_neighbors

def build_map(seating_chart):
    seat_map = {}
    nRows = len(seating_chart)
    nCols = len(seating_chart[0])
    
    all_seats = ''.join(seating_chart)
    seats = [indx for indx,this_spot in enumerate(all_seats) if this_spot != '.']
    for seat in seats:
        #neighbors_with_seats = get_surrounding_neighbor(seat,seats,nRows,nCols)    # Part One
        neighbors_with_seats = get_lineofsight_neighbor(seat,seats,nRows,nCols)     # Part Two
        seat_map[seat] = {'neighbors': neighbors_with_seats,
                     'occupied': (True if all_seats[seat]=='#' else False)
                    }
    #print_map(seat_map,nRows,nCols)
    return seat_map,nRows,nCols

def print_map(seat_map,nRows,nCols):
    numSeats = nRows * nCols
    for row in range(nRows):
        seat_nums=[row*nCols+col for col in range(nCols)]
        prow = ''.join(['.' if seat not in seat_map else '#' if seat_map[seat]['occupied'] else 'L' for seat in seat_nums])
        print(f"{prow}")

    print("\n\n")

if __name__ == "__main__":
    file = sys.argv[1]
    TOLERANCE_LEVEL = 5  # 4 for Part One or 5 for Part Two

    chart = read_seating_chart(file)
    seat_map,nrows,ncols = build_map(chart)

    hasStabilized = False
    while not hasStabilized:
        #print_map(seat_map,nrows,ncols)
        changeset = []
        for seat in seat_map:
            if not seat_map[seat]['occupied']:
                if all(not seat_map[neighbor]['occupied'] for neighbor in seat_map[seat]['neighbors']):
                    changeset.append((seat,True))
            else: # has occupent
                if sum(1 for neighbor in seat_map[seat]['neighbors'] if seat_map[neighbor]['occupied']) >= TOLERANCE_LEVEL:
                    changeset.append((seat,False))

        if changeset:
            for change in changeset:
                seat_map[change[0]]['occupied'] = change[1]
        else:
            hasStabilized = True

    total_occupied_seats = sum(1 for seat in seat_map if seat_map[seat]['occupied'])
    print(f"The total number of occupied seats are {total_occupied_seats}")
