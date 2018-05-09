import sys
from collections import defaultdict

def printDict(d):
    sorted_dict = sorted(d.items(), key = lambda kv: (-kv[1], kv[0]))
    for word in sorted_dict:
        print("{} -- {}".format(word[0], word[1]))
    print(len(sorted_dict))


def parseLine(line: str, d):
    s = ""
    for i in range(len(line)):
        if line[i].isalnum():
            s += line[i]
        else:
            if s != "":
                d[s.lower()] += 1
            s = ""


def readFile(fn):
    d = defaultdict(int)
    for line in fn:
        parseLine(line.rstrip("\n"), d)
    return d

def openFile(filename):
    try:
        f = open(filename, 'r')
        return f
    except Exception:
        print("File not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        f = openFile(filename)
        d = readFile(f)
        printDict(d)

        f.close()
    elif len(sys.argv) < 2:
        print("Not enough arguments.")
    else:
        print("Too many arguments.")
