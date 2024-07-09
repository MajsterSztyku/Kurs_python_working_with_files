from pathlib import Path

def glob_match(fld,search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)

# glob_match('Finding Files/files','*1*_*.c*')
glob_match('Finding Files/files/subfolder','*1*_*.c*')