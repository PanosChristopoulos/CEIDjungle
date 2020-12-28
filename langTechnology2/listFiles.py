import os

def listFilesInCollectionA():
    location = 'collectionA'
    files_in_dirA = []

    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in f:
            files_in_dirA.append(os.path.join(r, item))

    print(len(files_in_dirA),'total files in collection A')
    return files_in_dirA

def listFilesInCollectionE():
    location = 'collectionE'
    files_in_dirE = []
    dirsList = os.listdir(location)
    for dirName in range(len(dirsList)):
        tempList = []
        tempPath = os.path.join(location, dirsList[dirName])
        for r, d, f in os.walk(tempPath):
            for item in f:
                tempList.append(os.path.join(r, item))
        files_in_dirE.append(tempList)
    return [dirsList,files_in_dirE]
