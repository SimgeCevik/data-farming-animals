"""Module defining the base Animal class."""

class Animal:
    """Represents a generic animal with an energy level."""

    def __init__(self):
        self.energy = 0

    def feed(self):
        """Increase the animal's energy by 1."""
        self.energy += 1


    