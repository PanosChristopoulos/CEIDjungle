import string
import numpy as np
import math
from numpy import linalg


# A Cosine Calculation function is created in order to calculate two files' cosine using given function
def CosineCalculation():
    for x in range(0,len(FilesNameList)):
        for y in range(x,len(FilesNameList)):
            if x==y:
                continue
            Document1=EveryVector[x]
            Document2=EveryVector[y]

            Doc1Norm = linalg.norm(Document1,ord=2)
            Doc2Norm = linalg.norm(Document2,ord=2)
            InnerProduct = np.dot(Document1,Document2)
            cosine = InnerProduct/(Doc1Norm*Doc2Norm)
            CosineResults.append(cosine)


# A list is declared containing the cosines from previous function
CosineResults = list()

# A function is created that requests user to type in K, calculates the binomial coefficient and checks if it is valid
def BinomialCoef(size):
    kmost=int(input("Type in K:"))
    binom=int(math.factorial(size)/(math.factorial(2)*math.factorial(size-2)))
    acceptable=False
    while not acceptable: 
        if kmost<=binom:
            acceptable=True
            return kmost
        else:
            print("Given K is not eligible, type in another K")
            kmost=int(input("Type in K:"))

# Files' number is initialized to -1
# A while loop checks if there is a minimum number of files to work with, by continuously
# asking the user the amount of files he wishes to input when his initial number is less than 2
NumOfFiles=-1
while NumOfFiles < 2:
    NumOfFiles = int(input('How many files do you want to input?'))

# FilesNameList, Directory and EveryVector lists are declared
FilesNameList = list()
Directory = list()
EveryVector = list()

# This while loop checks if the files' extensions are valid for the program to use(it supports .txt files)
while NumOfFiles != 0:
    name = input('Type in File Name:')
    if name.endswith('.txt'):
        FilesNameList.append(name)
        NumOfFiles=NumOfFiles-1
    else:
        print('Invalid file extension')


# This for loop splits every word from a file's lines and unless they are already added, appends them to directory list
# while ignoring capital distinctions between words
for name in range(len(FilesNameList)):
    with open(FilesNameList[name], 'r') as file:
        for line in file:
            for word in line.split():
                if word in Directory:
                    continue
                else:
                    Directory.append(word.translate(str.maketrans('','', string.punctuation)).lower())


# It adds a vector position every time a word is accessed
for i in range(len(FilesNameList)):
    vector = list(0 for x in range(len(Directory)))
    with open(FilesNameList[i],'r') as file:
        for line in file: 
            for word in line.split():
                pos=Directory.index(word.translate(str.maketrans('','', string.punctuation)).lower())
                vector[pos] = vector[pos] + 1
    EveryVector.append(vector) 
    print(vector)

# Cosine Calculation and binomial coefficient are called
CosineCalculation()
K=int(BinomialCoef(len(FilesNameList)))

# Cosine Results are sorted
CosineResults.sort()

# Archive similarity float is printed
print("Archive similarity is:")
for i in range(K):
    print(CosineResults[i])
