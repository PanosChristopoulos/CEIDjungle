import os

def listFilesInCollectionA():
    location = 'collectionA'
    files_in_dirA = []

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


def listConcatTextsCollE():
    location = 'catText'
    files_in_dirA = []

    for r, d, f in os.walk(location):
        for item in f:
            files_in_dirA.append(os.path.join(r, item))

    print(len(files_in_dirA),'total files in collection A')
    return files_in_dirA

def makeFilesForCollectionE():
    counter = 0
    pathList = listFilesInCollectionE()
    for x in range(len(pathList[1])):        
        for idx in range(len(pathList[1][x])):
            try:
                with open(pathList[1][x][idx], 'rb') as f:
                    contents = f.read()
                    lines = []
                    contents = str(contents, errors='ignore')
                    contents = contents.split("\n")
                    for line in contents:
                        if line.startswith("From:") or line.startswith("Subject:") or line.startswith("Organization:") or line.startswith("X-Newsreader:") or line.startswith("Lines:") or line.startswith("Reply-To:") or line.startswith("NNTP-Posting-Host:") or line.startswith("Nntp-Posting-Host:"):
                            pass
                        else:
                            lines.append(line)
                    tempArticle = "".join(lines)
            except Exception as e: print(e)
            try:
                f = open('catText/{}'.format(pathList[0][x]),'a+')
                f.write(tempArticle)
                f.write("\n")
                f.close()
            except Exception as e: print(e)

#makeFilesForCollectionE()
