import sys
from time import time

f = open("wordlist.txt",'r')
out = open("output.txt", 'w')
words = {}
gen = []
pruneCount = 0
word = ""
final = []

for arg in sys.argv:
    word = arg

for line in f:
    words[line.strip()] = 1

elapsed = time()
def recurse(current, string):
    if string == "":
        return
    if not isPrefix(current):
        return
    gen.append(current)
    gen.append(str(current + string[:1]))
    recurse(current, string[1:])
    recurse(str(current + string[:1]), string[1:])

def checkOverlap(gen, words):
    for item in gen:
        if item in words:
            if item not in final:
                final.append(item)
            
            
def isPrefix(inStr):
    global pruneCount
    for item in words:
        if inStr == item[:len(inStr)]:
            return True
    pruneCount += 2*(len(word) - len(inStr))
    return False
            
recurse("", word)
checkOverlap(gen, words)
final.sort()
for item in final:
    out.write(item)
    out.write('\n')
print (time() - elapsed)