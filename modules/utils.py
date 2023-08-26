import csv
import re

def count_word_occurences(text, target = None):
    if target is None:
        file = open('tools.csv', 'r')
        tools = list(csv.reader(file, delimiter=','))
        file.close()
        target = list(map(lambda tool: tool[0], tools))
        
    matched_word = []
    
    for tool in target:
        count = 0

        if findWholeWord(tool)(text) is not None:
            count +=1
            
        if count > 0:
            matched_word.append(tool)
    return matched_word

def findWholeWord(w):
    return re.compile(r"(?<![^\s,\/,\,,\\,\:,\(,\[,\{{])\b({0})\b(?![^\s,\/,\,,\\,\:,\),\],\}}])".format(w), flags=re.IGNORECASE).search