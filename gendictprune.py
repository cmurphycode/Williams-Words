import sys

#input into this structure
words = {}
wordList = []
#strings generated go here
gen = []
#input word
word = ""
#final output
final = []
#output file
outFile = ""



def recurse(current, string, prefixList):
    ''' calculates all the substrings forward (cannot backtrack)
    Input: current string, base string
    Example: spray => recurse("s","pray"), recurse("","pray") (exponential)'''
    #base case: no more base string to process
    if string == "":
        return
    #if the current string is not a prefix for a word, might as well quit
    if len(current) < len(prefixList):
        if current not in prefixList[len(current)]:
            return
    
    #recursive case: we create two new threads of processing, one with the first character in the base string,
    #and one without, thus we will hit all possible strings that can be generated forward 
    #note: this is different than just mixing all of the letters together however you please
    #So here we add the two cases to our generated strings list
    gen.append(current)
    gen.append(str(current + string[:1]))
    #then recurse on the two
    recurse(current, string[1:],prefixList)
    recurse(str(current + string[:1]), string[1:],prefixList)


def checkOverlap(gen, words):
    '''check the generated strings for words
    input: string list, word list'''
    for item in gen:
    #these are just strings, so lets check if they're words
        if item in words:
            #ignoring duplicates as we go
            if item not in final:
                final.append(item)
                
def generatePrefixes(words):
    prefixList = [{},{},{},{},{},{},{}]
    for word in words:
        for i in range(7):
            prefixList[i][word[:i]] = 1
    
    return prefixList
    
    
            

if __name__ == "__main__":
    #first arg = word to parse, second arg = wordlist name, optional, third arg = (generated word) minimum length, optional
    arglength = len(sys.argv)
    if arglength > 1:
        word = sys.argv[1]
    else:
        print "Please specify an input word"
        quit()
    if arglength > 2:
        list = sys.argv[2]
    else:
        print "Using default wordlist.txt"
        list = "wordlist.txt"
    if arglength > 3:
        cutoff = int(sys.argv[3])
    else:
        print "Using default cutoff of 1 letter"
        cutoff = 1

    #create output file based on the word we're generating
    outFile = "pruned-output-" + word + ".txt"
    out = open(outFile, 'w')
    #create input file 
    f = open(list,'r')

    #file is one word per line, strip out the endline character, and throw in a dictionary
    for line in f:
        line = line.strip()
        if len(line) > cutoff:
            words[line] = 1
            wordList.append(line)
           
    prefixList = generatePrefixes(wordList)
    

           
    #start recursion on the input word           
    recurse("", word, prefixList)
    #given the generated strings, find the words
    checkOverlap(gen, words)
    #sort the output
    final.sort()
    #write the output
    for item in final:
        out.write(item)
        out.write('\n')
    print "Output written to " + outFile