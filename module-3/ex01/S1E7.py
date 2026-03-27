from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __repr__(self):
        """__repr__"""
        return self.__str__()  
 
    def __str__(self):
        """__str__"""
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def func(self):
        return "Ours is the Fury"
    

class Lannister(Character):
    """Representing the Lannister family."""
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"


    def __repr__(self):
        """__repr__"""
        return self.__str__()  
 
    def __str__(self):
        """__str__"""
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def func(self):
        return "Hear Me Roar!"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
    

