"""Module defining the Chicken class."""

from farm.animal import Animal

class Chicken(Animal):
    """Represents a chicken, which is a specific type of animal."""

    def __init__(self, gender):
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        """Return the sound this chicken makes based on gender."""
        if self.gender == "male":
            return "cock-a-doodle-doo"
        else:
            return "cluck cluck"

    def feed(self):
        """Feed the chicken, increasing energy; females also produce eggs."""
        super().feed()
        if self.gender == "female":
            self.eggs += 2
