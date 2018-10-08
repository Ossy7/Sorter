#Reads two plain files and finds their common occurences


def isorter(file1, file2):
    '''finds common occurences between 2 files'''
    try:
        fp1 = open(file1, 'rb')
    except Exception:
        print("Ensure " +file1+" is in the current directory and you have access.")
        return
    try:
        fp2 = open(file2, 'rb')
    except Exception:
        print( "Ensure "+file2+" is in the current directory and you have access.")
        return
    reader1 = {line for line in fp1.readlines()}
    reader2 = {line for line in fp2.readlines()}
    fp1.close()
    fp2.close()
    return (reader1 & reader2)








    


