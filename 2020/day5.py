import sys

def read_seating_chart(filename):
    with open(filename,'r') as fh:
        seat_chart = [line.rstrip('\n') for line in fh]

    return seat_chart

def get_row_col(seat):
    row_chars = seat[:7]
    col_chars = seat[-3:]

    row_bchars = ['1' if s=='B' else '0' for s in row_chars]
    row_bin = ''.join(row_bchars)
    row = int(row_bin,2)

    col_bchars = ['1' if s=='R' else '0' for s in col_chars]
    col_bin = ''.join(col_bchars)
    col = int(col_bin,2)
    
    return row,col
    
if __name__ == "__main__":
    file = sys.argv[1]
    chart = read_seating_chart(file)

    elimination_chart = list(range(902))
    ids =[]
    for seat in chart:
        r,c = get_row_col(seat)
        seatID = (r*8) + c
        ids.append(seatID)

        elimination_chart[seatID] = 0

    print(f"The highest seat ID is {max(ids)}")

    open_seats = [id for id in elimination_chart if id != 0]
    print(f"Empty seats include {open_seats}")
