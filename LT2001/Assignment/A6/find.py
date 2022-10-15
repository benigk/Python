import sys
from pathlib import Path

def find(dir_path, pattern):
    for file in Path(dir_path).rglob(pattern):
        print(file)

def main():
    dir_path = sys.argv[1] 
    pattern =  sys.argv[2]
    if not Path(dir_path).is_dir():
        sys.exit('the path is not a directory') 
    elif '/' in pattern:
        sys.exit('there is a / in the pattern') 
    find(dir_path, pattern)

if __name__=="__main__":
    main()