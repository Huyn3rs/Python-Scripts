from partA import *
import sys

def compareWords(s1: set, s2: set):
    i = 0
    for s in sorted(s1):
        if s in s2:
            print(s)
            i += 1
    print(i)

def parseLine(line: str, d):
    s = ""
    for i in range(len(line)):
        if line[i].isalnum():
            s += line[i]
        else:
            if s != "":
                d.add(s.lower())
            s = ""

def readFile(f):
    d = set()
    for line in f:
        parseLine(line, d)
    return d


if __name__ == "__main__":
    if len(sys.argv) == 3:
        fn1 = sys.argv[1]
        fn2 = sys.argv[2]
        
        f1 = openFile(fn1)
        f2 = openFile(fn2)
        
        s1 = readFile(f1)
        s2 = readFile(f2)

        compareWords(s1, s2)

        f1.close()
        f2.close()
    elif len(sys.argv) < 3:
        print("Not enough arguments.")
    else:
        print("Too many arguments.")
