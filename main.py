import sys
from mysorter import sorter, word_counter

def main():
    if len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        common_occurence = sorter(file1, file2)
        WordCounter = word_counter(file1)
        wordCounter = word_counter(file2)
        if common_occurence:
            print("There are  %s  common occurrence. "  %common_occurence)
        print("There are %s words in %s" %(WordCounter, file1))
        print("There are %s words in %s" %(wordCounter, file2))
            
    else:
        print("USEAGE: main.py myfile1 myfile2")
if __name__ == '__main__':
    main()
