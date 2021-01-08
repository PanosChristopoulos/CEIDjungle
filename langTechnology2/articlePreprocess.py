import nltk
import json
from listFiles import *
from collections import Counter
from nltk.stem import PorterStemmer 
import traceback

closedClassTags = ['CD', 'CC', 'DT', 'EX', 'IN', 'LS', "''", ',', '.', '``', 'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB']

def listToString(test_list):  
    res = str(test_list).strip('[]')
    return res


def tokenizedPreprocessor(NTLKList):
    tempFinalList = []
    wordsList = []
    for x in NTLKList:
        if x[1] in closedClassTags:
            pass
        else:
            tempFinalList.append(x)
    for x in tempFinalList:
        wordsList.append(x[0])
    counts = Counter(wordsList)
    your_list = [list(i) for i in counts.items()]

    return [tempFinalList,your_list]

def tokenization(tempArticlePath):
    f = open(tempArticlePath, 'r')
    eris = f.read()
    lines = []
    for line in eris:
        if line in ['\n', '\r\n']:
            break
    for line in f:
        lines.append(line)
    tempArticle = "".join(lines)
    tokens = nltk.word_tokenize(eris)
    tempTokenizedArticleList = nltk.pos_tag(tokens)
    preprocessedFunctionReturn = tokenizedPreprocessor(tempTokenizedArticleList)
    tempTokenizedArticle = preprocessedFunctionReturn[0]
    totalLemmaArticleCount = preprocessedFunctionReturn[1]
    signigicantWordCount = len(tempTokenizedArticleList)
    ps = PorterStemmer()
    for item in totalLemmaArticleCount:
        item[0] = ps.stem(item[0])
    res = {}
    for sub in totalLemmaArticleCount:
        try:
            res.update({sub[0]: res.get(sub[0]) + sub[1]})
        except:
            res[sub[0]] = sub[1]
    totalLemmaArticleCount = []
    for key,value in res.items():
        totalLemmaArticleCount.append([key,value])
    return tempTokenizedArticle,totalLemmaArticleCount,signigicantWordCount



