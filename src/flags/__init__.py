from typing import Union
from toml import load
from util.path import conjoin, until

class Flags:
    SINGLE_DASH = 1
    DOUBLE_DASH = 2

    def __init__(self, config: Union[tuple, str] = ('flags', '/toml', 'flags.toml')) -> None:
        if type(config) == tuple: config = conjoin(*config)
        self.config = config
        
        with open(self.config, 'r') as file:
            self.flags = load(file)
    
    def parse(self, *args: str) -> tuple:
        flags = []
        for arg in args:
            flag_type = Flags.__type__(arg)
            flag = arg[flag_type:].lower()
            if flag_type == Flags.SINGLE_DASH:
                flags.extend([f for f in flag if f in self.flags])
            elif flag_type == Flags.DOUBLE_DASH:
                flags.append(self.__simplify__(flag))
            else: continue
        return tuple(flags)

    def __type__(arg: str) -> int:
        n = until(arg, ('-'), 0, +1)
        return n if n == 1 or n == 2 else -1

    def __simplify__(self, arg: str) -> str:
        for key, value in self.flags.items():
            if arg in value: return key
        return ''