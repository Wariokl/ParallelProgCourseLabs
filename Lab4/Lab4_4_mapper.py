import sys
import re, locale

for line in sys.stdin:
    line = line.strip()
    line=re.sub(r'[^0-9a-zA-Z]+', ' ', line)
    words = line.split()
    if len(words)==1:
        print ("%s\t%s" % (words[0],"1"))
    else:
        for word in range(len(words)):
            if word<=len(words)-2:
                print ("%s\t%s" % (words[word]+' '+words[word+1],"1"))