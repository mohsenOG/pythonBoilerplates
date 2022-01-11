

def lineRemover(oldFilePath : str, newFilePath : str, filter : str) -> str :
    '''
    create a new file consisting old file without the lines consisting 'filter'.
    '''
    with open(oldFilePath, 'r') as oldFile, open(newFilePath, 'w') as newFile:
        lines = oldFile.readlines()
        for line in lines:
            if filter not in line:
                newFile.write(line)
    oldFile.close()
    newFile.close()
