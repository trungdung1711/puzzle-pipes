from state.direction import Direction
from state.type import PipeType


class Pipe:
    def __init__(self, type: PipeType, direction: Direction):
        self.__type = type
        self.__direction = direction


    def get_type(self) -> PipeType:
        return self.__type
    
    
    def set_type(self, type: PipeType):
        self.__type = type
    

    def get_direction(self) -> Direction:
        return self.__direction
    

    def set_direction(self, direction: Direction):
        self.__direction = direction


    def show(self):
        print(f'[{self.__type.name},{self.__direction.name}]')