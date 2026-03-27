class calculator:
    """calculator"""
    def __init__(self, lst):
        self.lst = lst

    def __add__(self, object) -> None:            
        print([x + object for x in self.lst])

    def __mul__(self, object) -> None:            
        print([x * object for x in self.lst])

    def __sub__(self, object) -> None:            
        print([x - object for x in self.lst])

    def __truediv__(self, object) -> None:
        if object == 0:
            print("division by 0")
        else:            
            print([x / object for x in self.lst])
