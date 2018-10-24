import os
__version__ = "1.0.2"

def sorter(file1, file2):
    '''finds common occurences between 2 plain files'''
    if os.path.isfile(file1) and os.path.isfile(file2):
        if os.access(file1, os.R_OK) and os.access(file2, os.R_OK):
           reader = {(line1, line2) for line1 in open(file1, 'rb').readlines() for line2 in open(file2, 'rb').readlines() if line1.split() == line2.split()}
           return reader
        else:
            print("Ensure you have permission to the two files.")
    else:
        print("Ensure both are files and present in the current directory.")
            
            
