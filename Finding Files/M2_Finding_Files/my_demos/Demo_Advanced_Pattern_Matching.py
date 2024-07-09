import os, fnmatch

def match(fld,search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn,search):
            print(fn)
#match("Finding Files/files",'*_file*.*')
#match("Finding Files/files",'*_file_*.*')
match("Finding Files/files",'*0*')