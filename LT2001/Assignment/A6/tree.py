import sys
from pathlib import Path

# def print_dir(dir_path, depth):
#     for file in Path(dir_path).glob('*'):
#         if file.is_dir():
#             print(f"{' '*int(depth)}D {file}")
#         elif file.is_file():
#             print(f"{' '*int(depth)}F {file}")

def print_dir(dir_path, depth):
    for file in sorted(Path(dir_path).glob('*'), key=lambda path: path.name):
        if file.is_dir():
            print(f"{' '*int(depth)}D {file}")
            print_dir(file, int(depth)+1)
        elif file.is_file():
            print(f"{' '*int(depth)}F {file}")
        
def main():
    dir_path = sys.argv[1] 
    depth =  sys.argv[2]

    print_dir(dir_path, depth)


if __name__=="__main__":
    main()
