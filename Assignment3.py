################################
## Assignment 3
## Dvir David Iluz
## 311447668
################################

def read_line(n, file):
    try:
        if not isinstance(n,int) or not isinstance(file,str):
            return "invalid input detected"
        f = open(file)
        read = f.readlines()[n-1].rstrip('\n')
        return read
    except IOError:
        return "file not found"
    except IndexError:
        return f"line {n} doesn't exist"

import re

def longest_words(file):
    try:
        if not isinstance(file,str):
            return "invalid input detected"
        with open(file, 'r') as f:
            words = f.read().strip()
            fixed = re.sub('\W+',' ', words)
            fixed = fixed.split(" ")
            longest_word = ''
            count = 0
            top_five = []
            while count < 5:
                for word in fixed:
                    if len(word) > len(longest_word):
                        longest_word = word
                top_five.append(longest_word)
                fixed.remove(longest_word)
                longest_word = ''
                count += 1
            return top_five
    except IOError:
        return "file not found"
