class Character:
    def __init__(self, name, age, origin):
        """
        Initialize a general character.
        """
        self.name = name
        self.age = age
        self.origin = origin

    def introduce(self):
        """
        Introduce the character.
        """
        print(f"Hello, I'm {self.name}, from {self.origin}. I'm {self.age} years old.")


class Superhero(Character):
    def __init__(self, name, age, origin, alias, superpower, strength_level):
        """
        Initialize a superhero, inheriting from Character.
        """
        super().__init__(name, age, origin)
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level  

    def use_superpower(self):
        """
        Use the superhero's superpower.
        """
        print(f"{self.alias} uses their superpower: {self.superpower}!")

    def save_the_day(self):
        """
        Simulate saving the day.
        """
        print(f"{self.alias} saves the day with incredible strength level {self.strength_level}!")

    def introduce(self):
        """
        Override the introduce method to include superhero identity.
        """
        print(f"I am {self.alias}, also known as {self.name}. My superpower is {self.superpower}!")


class Villain(Character):
    def __init__(self, name, age, origin, alias, evil_plan, danger_level):
        """
        Initialize a villain, inheriting from Character.
        """
        super().__init__(name, age, origin)
        self.alias = alias
        self.evil_plan = evil_plan
        self.danger_level = danger_level  

    def execute_evil_plan(self):
        """
        Execute the villain's evil plan.
        """
        print(f"{self.alias} is executing their evil plan: {self.evil_plan}! Danger level: {self.danger_level}")

    def introduce(self):
        """
        Override the introduce method to include villain identity.
        """
        print(f"I am {self.alias}, the feared villain! Beware of my plan: {self.evil_plan}.")


