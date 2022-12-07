import sys

def read_multiline(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    # Hack to exit reading code
    lines.append('$ EOF')
    return lines

def build_filesystem(code):
    dirs = {}
    indx = 0
    print(f"len of code {len(code)}")
    while indx < len(code)-2:
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
                # if listing == '':
                #     print("EOF")
                
                if listing.startswith('$'):
                    indx += (2 + l_indx)
                    #import pdb; pdb.set_trace()
                    break
                elif listing.startswith('dir '):
                    _, dirname = listing.split('dir ')
                    if 'd' not in dirs[dir]:
                        #import pdb; pdb.set_trace()
                        dirs[dir]['d'] = []
                    dirs[dir]['d'].append(dirname)
                # elif listing[0] in '0123456789':
                else:
                    filesize,filename = listing.split(' ')
                    dirs[dir]['size'] += int(filesize)
                
                # #reached eof
                # if l_indx == len(code) + 1:
                #     print("l_indx is poast end of file")
                #     indx = len(code)
                #     break
                # else:
                #     # eof?
                #     print(f"Debug: EOF?")
                #     import pdb;pdb.set_trace()
                #     indx += (2 + l_indx)
                #     break
            # eof?
            # import pdb;pdb.set_trace()
            # break
        else:
            # another cd line follows
            indx += 1
    return dirs

def build_nav_filesystem(code):
    fs = {'/': {'parent':None,'files':[],'directories':[],'size':None,} }
    pwd = None
    for indx,line in enumerate(code):
        if line.startswith("$ "):
            prompt,cmd,*dir_listing = line.split(' ')
            if cmd == 'cd':
                # verify dir to change to
                if len(dir_listing) != 1:
                    raise ValueError(f"cd command has no directory! [{indx}]")
                dir = dir_listing[0]
                if dir == '..':
                    pwd = fs[pwd]['parent']
                else:
                    if dir not in fs:
                        fs[dir] = {'parent':pwd,'files':[],'directories':[],'size':None,}
                    pwd = dir
            elif cmd == 'ls':
                continue
                # use for loop to continue through
            elif cmd == "EOF":
                # Note in a FOR loop controlled parser we shouldn't have to add EOF and that code can be removed
                return fs
            else:
                print(f"Warning: Unknown Command - {cmd}")
        else:
            # a listing line
            # couple ways of parsing this . I am going based on dir line or not. Could just parse on space but can't figure out a good
            #  variable name for either_dir_listing_or_filesize (terrible var name ;) )
            if line.startswith('dir '):
                _, dir_name = line.split('dir ')
                fs[pwd]['directories'].append(dir_name)
            else:
                #should be file listing
                filesize, filename = line.split(' ')
                fs[pwd]['files'].append( (filesize,filename) )
    
    return fs

# def calculate_dir_size(dir):
#     for sub_dir in dir['directories']:

def get_dir_size(fs, dir):
    if fs[dir]['size'] is not None:
        return fs[dir]['size']
    dir_size = 0
    for sub_dir in dir['directories']:
        dir_size += get_dir_size(fs,sub_dir)
    
    for file in fs[dir]['files']:
        dir_size += file(0)
    
    fs[dir]['size'] = dir_size

    return something # knowing I need to return both dir_size but also fs as I modify it ..

# def do_something(fs):
#     for dir in fs:
#         for sub_dir in 

if __name__ == "__main__":
    file = sys.argv[1]
    #marker_size = int(sys.argv[2])

    terminal = read_multiline(file)
    # import pdb;pdb.set_trace()
    directories = build_nav_filesystem(terminal)

    # import pdb; pdb.set_trace()
    print(f"{directories}")

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
