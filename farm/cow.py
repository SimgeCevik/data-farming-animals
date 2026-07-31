"""Module defining the Cow class."""

from farm.animal import Animal

class Cow(Animal):
    """Represents a cow, which is a specific type of animal."""

    def __init__(self):
        super().__init__()
        self.milk = 0

    def talk(self):
        """Return the sound a cow makes."""
        return "moo"
    
    def feed(self):
        """Feed the cow, increasing energy and producing milk."""
        super().feed()
        self.milk += 2

    