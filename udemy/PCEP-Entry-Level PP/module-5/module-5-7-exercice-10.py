def unique(inList = []):
    resultList = []
    for i in inList :
        if i not in resultList:
            resultList.append(i)
    return resultList


print(unique(['Mark', 'Mark', 'John', 'Anne']))

