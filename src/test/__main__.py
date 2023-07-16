from counter import Counter

PATH = ('test', 'grandparent')

if __name__ == '__main__':
    counter = Counter(PATH)
    for mode in [Counter.CHARACTERS, Counter.WORDS, Counter.LINES, 
                 Counter.FILES, Counter.FOLDERS]:
        n = counter.count(mode)
        print(f'{mode}: {n}')