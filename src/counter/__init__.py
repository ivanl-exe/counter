from typing import Union
from util.path import conjoin, splinter
from os import listdir, getcwd
from os.path import isfile, isdir

class Counter:
    CHARACTERS = 'c'
    WORDS = 'w'
    LINES = 'l'
    FILES = 'f'
    DIRECTORIES = FOLDERS = 'd'

    def __init__(self, path: Union[str, tuple]) -> None:
        if type(path) == tuple: path = conjoin(*path)
        self.path = path
        self.structure = Counter.__entries__(self.path)
        self.files, self.directories = Counter.__unpack__(self.structure)
        self.folders = self.directories

    def __entries__(path: str) -> list[dict]:
        structure = []
        queue = [(path, structure)]
        WORKING = getcwd()
        while len(queue) > 0:
            path, directory = queue.pop(0)
            root = conjoin(WORKING, path)
            entries  = listdir(root)
            for entry in entries:
                local = conjoin(path, entry)
                if isdir(conjoin(root, entry)):
                    directory.append({})
                    directory[-1][entry] = []
                    queue.append((local, directory[-1][entry]))
                else:
                    directory.append(entry)
        return structure

    def __unpack__(structure: list[dict]) -> tuple[tuple, tuple]:
        files, directories = [], []
        queue = [('', structure)]
        while len(queue) > 0:
            parent, children = queue.pop(0)
            for child in children:
                if type(child) == dict:
                    key = list(child.keys())[0]
                    path = conjoin(parent, key)
                    directories.append(path)
                    queue.append((path, child[key]))
                else:
                    path = conjoin(parent, child)
                    files.append(path)
        return files, directories

    def count(self, mode: str) -> int:
        n = 0
        if mode == Counter.FILES:
            n = len(self.files)
        elif mode == Counter.DIRECTORIES:
            n = len(self.folders)
        else:
            for file in self.files:
                filepath = conjoin(self.path, file)
                with open(filepath, 'r') as file:
                    text = file.read()
                    if mode == Counter.CHARACTERS:
                        n += len(text)
                    elif mode == Counter.WORDS:
                        n += text.count(' ') + text.count('\n') + 1
                    elif mode == Counter.LINES:
                        n += text.count('\n') + 1
        return n