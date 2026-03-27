from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """The King."""

    def set_eyes(self, eyes):
        """set_eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """set_hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """get_eyes"""
        return self.eyes

    def get_hairs(self):
        """get_hairs"""
        return self.hairs


    def func(self):
        return "Ours is the Fury"

