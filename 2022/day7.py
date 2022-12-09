import sys

def read_multiline(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    # Hack to exit reading code
    lines.append('$ EOF')
    return lines

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

def build_filesystem_by_traversing(code):
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
                    relative_path = make_path_relative(traversed_path)
                    fs[relative_path] = {'files':[],'directories':[],'size':None,}
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
                print(f"Debug: Found EOF cmd!")
                return fs
            else:
                print(f"Warning: Unknown Command - {cmd}")
        else:
            # a listing line
            # couple ways of parsing this . I am going based on dir line or not. Could just parse on space but can't figure out a good
            #  variable name for either_dir_listing_or_filesize (terrible var name ;) )
            traversed_path = '/'.join(pwp)
            relative_path = make_path_relative(traversed_path)
            if line.startswith('dir '):
                _, dir_name = line.split('dir ')
                # fs[pwd]['directories'].append(dir_name)
                traversed_subdir = traversed_path + '/' + dir_name
                relative_subdir = make_path_relative(traversed_subdir)
                fs[relative_path]['directories'].append(relative_subdir)
            else:
                #should be file listing
                filesize, filename = line.split(' ')
                # fs[pwd]['files'].append( (filesize,filename) )
                fs[relative_path]['files'].append( (int(filesize),filename) )

    return fs

def resolve_all_traversed_paths(fs):
    for dirname in fs.keys():
        if is_traversed_path(dirname):
            rel_dirname = make_path_relative(dirname)
            fs[rel_dirname] = fs.pop(dirname)
        
    return fs

def calculate_filesystem_size(fs):
    # sum up file size for all directories
    for dir in fs:
        fs[dir]['size'] = sum([f[0] for f in fs[dir]['files']])

    # while any directories still have sub directories listed,
    # loop through adding in those directories that no longer
    # have any direcories listed and then remove that directory
    # from the subdirectories list
    #
    # Expect this to be a non optimal process
    # any([True if fs[d]['directories'] else False for d in fs ])
    while any([True if fs[d]['directories'] else False for d in fs ]):        
        for dir in fs:
            remove_these = []
            for indx,subdir in enumerate(fs[dir]['directories']):
                if not fs[subdir]['directories']:
                    fs[dir]['size'] += fs[subdir]['size']
                    remove_these.append(subdir)
            for remove in remove_these:
                remove_indx = fs[dir]['directories'].index(remove)
                fs[dir]['directories'].pop(remove_indx)

    return fs

if __name__ == "__main__":
    file = sys.argv[1]

    t = '//a/e/../../d'
    r = make_path_relative(t)
    print(f"traversed  {t}\nrelative   {r}")

    t2 = '//a/b/c/d/e/../../../../../f'
    r2 = make_path_relative(t2)
    print(f"traversed  {t2}\nrelative   {r2}")

    terminal = read_multiline(file)

    filesystem = build_filesystem_by_traversing(terminal)

    calculated_fs = calculate_filesystem_size(filesystem)
    print(f"{calculated_fs}")

    # print(f"The total is {total}")
    # part1_ans = total

    # if len(sys.argv) >= 3:
    #     if int(sys.argv[2]) == part1_ans:
    #         print(f"Answer is correct!")
