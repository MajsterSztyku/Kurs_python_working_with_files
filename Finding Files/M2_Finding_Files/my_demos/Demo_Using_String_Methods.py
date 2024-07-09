import os

def ends_with(fld,search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn ,"\n")

def starts_with(fld,search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn,"\n")
print("Files ending with .txt: \n")
ends_with('Finding Files/files','t.txt')
print("Files starting with 01: \n")
starts_with('Finding Files/files','01')