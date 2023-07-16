JOINT = ('/', '\\')

def splinter(arg: str) -> tuple:
    for c in JOINT: arg = arg.replace(c, ' ')
    return arg.split(' ')

def until(arg: str, conditional: tuple, start: int, increment: int) -> int:
    i = start
    while i >= 0 and i < len(arg) and arg[i] in conditional: i += increment
    return i

def conjoin(*args: str) -> str:
    return '/'.join([arg[until(arg, JOINT, 0, +1):until(arg, JOINT, len(arg)-1, -1)+1] for arg in args])