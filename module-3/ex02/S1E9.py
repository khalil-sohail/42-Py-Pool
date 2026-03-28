from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract base class representing a character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a character."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Mark the character as dead."""
        pass


class Stark(Character):
    """A concrete class representing a member of the Stark family."""
    def die(self):
        """Mark the Stark character as dead."""
        self.is_alive = False
