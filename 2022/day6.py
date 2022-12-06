import sys

def read_datastream(filename):
    with open(filename,'r') as fh:
        ds_str = fh.readline().rstrip('\n')

    ds = [c for c in ds_str]

    return ds

def find_start_of_packet_marker(ds,size):
    """
    There is an interesting "flaw" in the following code .. can you spot it?

    I loop through the entire datastream and look from the current loop index to the index
    plus the size of the marker. This means that if the marker is not found as the loop
    approaches the end of the datastream my indexing is looking out past the length of the
    datastream. Interesting (and I didn't know this nor expect it) but Python did not throw
    an error on slicing a list outside the bounds of that list. For example, we can setup a
    list of characters (I know this sequence breaks the puzzle but having unique chars in
    the datastream helps to demonstrate which characters are at which index),

    >>> datastream = 'abcdefghijklmnopqrst' 
    >>> len(datastream)
    20
    >>> marker_size = 4
    >>> index = 5
    >>> datastream[index:index+marker_size] 
    'fghi'
    >>> index = 16
    >>> datastream[index:index+marker_size]
    'qrst'
    
    If we start near the end and our stopping index is out of the range

    >>> index = 18
    >>> datastream[index:index+marker_size]
    'st'
    
    we see we get just that slice within the bounds of the list. Interesting we can slice
    entirely outside of the list,

    >>> datastream[27:32]                   
    ''
    
    But if we index outside the  we get, what I was expecting, and out of range error,

    >>> datastream[27]    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range
    >>>     
        
    Now as this implementation does not break the solution I am going to leave it as is.
    But I do see the flaw in my logic which could cause problems moving forward.
    """
    
    for indx,_ in enumerate(ds):
        if len(set(ds[indx:indx+size])) == size:
            return indx+size   # noting Python is zero based but answer will be one based

if __name__ == "__main__":
    file = sys.argv[1]
    marker_size = int(sys.argv[2])

    datastream = read_datastream(file)
    pos_marker = find_start_of_packet_marker(datastream, marker_size)

    print(f"The position of the marker is {pos_marker}")
    part1_ans = pos_marker

    if len(sys.argv) >= 4:
        if int(sys.argv[3]) == part1_ans:
            print(f"Answer is correct!")
