from flags import Flags
from counter import Counter
from sys import argv

if __name__ == '__main__':
    filename = argv.pop(0)

    paths, flags = [], []
    for arg in argv:
        if arg[0] != '-':
            paths.append(arg)
        else:
            flags.append(arg)
    
    n = 0
    for path in paths: 
        counter = Counter(path)
        for mode in  Flags().parse(*flags):
            n += counter.count(mode)
    print(n)