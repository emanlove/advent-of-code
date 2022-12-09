import sys

# class Directory:
#     def __init__(self,)


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

def is_traversed_path(path):
    """
    Returns True if path is a tranversed path. Otherwise, it is a relative path and
    returns false.
    """
    return '..' in path

def make_path_relative(path):
    dirs = path.split('/')
    indx = 0
    end = len(dirs)
    while indx < end:
        if dirs[indx] == '..':
            dirs.pop(indx)
            dirs.pop(indx-1)
            end -= 2
            indx -= 1
        else:
            indx += 1

    return '/'.join(dirs)

def build_nav_filesystem(code):
    fs = {'/': {'parent':None,'files':[],'directories':[],'size':None,} }
    pwd = None
    pwp = []
    for indx,line in enumerate(code):
        if line.startswith("$ "):
            prompt,cmd,*dir_listing = line.split(' ')
            if cmd == 'cd':
                # verify dir to change to
                if len(dir_listing) != 1:
                    raise ValueError(f"cd command has no directory! [{indx}]")
                dir = dir_listing[0]            
                pwp.append(dir)
                traversed_path = '/'.join(pwp)
                # don't think I need to save directories but going to start to do so .. just to see what I see
                # only want to save when not changing directory to parent,or really when the next command is ls,
                # but for now will will do this ..
                # .. still worried about that inital '/' and then '' directory which is the root ..
                if dir != '..':
                    fs[traversed_path] = {'files':[],'directories':[],'size':None,}
                # if dir == '..':
                #     pwd = fs[pwd]['parent']
                # else:
                #     if dir not in fs:
                #         fs[dir] = {'parent':pwd,'files':[],'directories':[],'size':None,}
                #     pwd = dir
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
            traversed_path = '/'.join(pwp)
            if line.startswith('dir '):
                _, dir_name = line.split('dir ')
                # fs[pwd]['directories'].append(dir_name)
                fs[traversed_path]['directories'].append(traversed_path + '/' + dir_name)
            else:
                #should be file listing
                filesize, filename = line.split(' ')
                # fs[pwd]['files'].append( (filesize,filename) )
                fs[traversed_path]['files'].append( (filesize,filename) )

    return fs

# def calculate_dir_size(dir):
#     for sub_dir in dir['directories']:

def resolve_all_traversed_paths(fs):
    for dirname in fs.keys():
        if is_traversed_path(dirname):
            rel_dirname = make_path_relative(dirname)
            fs[rel_dirname] = fs.pop(dirname)
        
    return fs

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

    t = '//a/e/../../d'
    r = make_path_relative(t)
    print(f"traversed  {t}\nrelative   {r}")

    t2 = '//a/b/c/d/e/../../../../../f'
    r2 = make_path_relative(t2)
    print(f"traversed  {t2}\nrelative   {r2}")

    terminal = read_multiline(file)
    # import pdb;pdb.set_trace()
    directories = build_nav_filesystem(terminal)

    # import pdb; pdb.set_trace()
    print(f"{directories}")

    new_filesystem = resolve_all_traversed_paths(directories)
    print(f"{new_filesystem}")

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
