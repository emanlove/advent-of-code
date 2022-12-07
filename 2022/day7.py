import sys

def read_datastream(filename):
    with open(filename,'r') as fh:
        ds_str = fh.readline().rstrip('\n')

    ds = [c for c in ds_str]

    return ds

def read_multiline(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    return lines

def build_filesystem(code):
    dirs = {}
    indx = 0
    while indx < len(code)-1:
        print(f"indx: {indx}")
    # for line in code:
        line = code[indx]
        if line.startswith('$ cd ') and not line.endswith('..') and code[indx+1]=='$ ls':
            # start of directory listing
            _,dir = line.split('$ cd ')

            # warn if we already know this dir
            if dir in dirs:
                print(f'Warning: Found listing for {dir} again!')
                break
            
            dirs[dir] = {'size':0}
            l_strtindx = indx+2
            for l_indx,listing in enumerate(code[l_strtindx:]):
                if listing.startswith('$'):
                    indx += (2 + l_indx)
                    # import pdb; pdb.set_trace()
                    break
                elif listing.startswith('dir '):
                    _, dirname = listing.split('dir ')
                    if 'd' not in dirs[dir]:
                        #import pdb; pdb.set_trace()
                        dirs[dir]['d'] = []
                    dirs[dir]['d'].append(dirname)
                else:
                    filesize,filename = listing.split(' ')
                    dirs[dir]['size'] += int(filesize)
        else:
            # another cd line follows
            indx += 1
    return dirs

# def build_filesystem(code):
#     fs = {'/':{'parent':None,'files':{},'directories':{},'size':{}}
#     for line in code:
#         if line.startswith("$ "):
#             prompt,cmd,*dir 
#             if 

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
    #marker_size = int(sys.argv[2])

    terminal = read_multiline(file)
    directories = build_filesystem(terminal)

    import pdb; pdb.set_trace()

    # total = 0
    # for line in datastream:
    #     if line[0] in '0123456789':
    #         size, *_ = line.split(' ')
    #         total += int(size)
    # pos_marker = find_start_of_packet_marker(datastream, marker_size)

    # print(f"The total is {total}")
    # part1_ans = total

    # if len(sys.argv) >= 3:
    #     if int(sys.argv[2]) == part1_ans:
    #         print(f"Answer is correct!")
