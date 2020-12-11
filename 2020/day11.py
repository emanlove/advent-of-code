import sys

def read_seating_chart(filename):
    with open(filename,'r') as fh:
        seating_chart = [line.rstrip('\n') for line in fh]

    return seating_chart

def build_map(seating_chart):
    seat_map = {}
    nRows = len(seating_chart)
    nCols = len(seating_chart[0])
    
    all_seats = ''.join(seating_chart)
    seats = [indx for indx,this_spot in enumerate(all_seats) if this_spot != '.']
    for seat in seats:
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
        neighbors_with_seats = [neighbor for neighbor in all_neighbors if neighbor in seats]
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

    chart = read_seating_chart(file)
    seat_map,nrows,ncols = build_map(chart)

    hasStabilized = False
    while not hasStabilized:
        print_map(seat_map,nrows,ncols)
        changeset = []
        for seat in seat_map:
            if not seat_map[seat]['occupied']:
                if all(not seat_map[neighbor]['occupied'] for neighbor in seat_map[seat]['neighbors']):
                    changeset.append((seat,True))
            else: # has occupent
                if sum(1 for neighbor in seat_map[seat]['neighbors'] if seat_map[neighbor]['occupied']) >= 4:
                    changeset.append((seat,False))

        if changeset:
            for change in changeset:
                seat_map[change[0]]['occupied'] = change[1]
        else:
            hasStabilized = True

    total_occupied_seats = sum(1 for seat in seat_map if seat_map[seat]['occupied'])
    print(f"The total number of occupied seats are {total_occupied_seats}")
