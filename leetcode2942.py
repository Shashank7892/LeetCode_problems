# 2942. Find Words Containing Character
def findwordcontaining(words,x):
    indexes=[]
    for i in range(len(words)):
        if x in words[i]:
            indexes.append(i)

    return indexes


words=["leet","code"]
x="e"
print(findwordcontaining(words,x))