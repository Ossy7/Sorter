import sys
from mysorter import isorter

def main():
    if len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        common_occurence = isorter(file1, file2)
        if common_occurence:
            print("There are " +" %s "  %len(common_occurence) +" common occurrence.")
    else:
        print("USEAGE: main.py myfile1 myfile2")
if __name__ == '__main__':
    main()

