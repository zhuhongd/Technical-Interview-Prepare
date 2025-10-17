"""
=========================================================
Problem: Add Superhero Abilities
Link: (Practice warm-up problem for class-based programming)
=========================================================

🧩 Description
--------------
We are given a base `SuperHero` class.  
We need to *extend* it by adding two new ability methods:

1️⃣ attack(): prints  "<name> attacks with <power>!"
2️⃣ heal(): increases `health` by 10 and prints  
            "<name> heals 10 points. New health: <health>."

Then we create a hero instance and demonstrate these abilities.

---------------------------------------------------------
Key Example
---------------------------------------------------------
Input:
  (no direct input — just class methods)

Output:
  Catwoman attacks with Agility!
  Catwoman heals 10 points. New health: 130
---------------------------------------------------------
"""

# =========================================================
# 🧠 Beginner Intuition
# ---------------------------------------------------------
# This is an introduction to object-oriented programming (OOP).
# A class defines a "blueprint" for creating objects that have:
#  - attributes (data)
#  - methods (behaviors)
#
# We'll add new *methods* to our existing SuperHero class,
# then call them from an instance of that class.
# =========================================================


# =========================================================
# 🏗️ Step 1: Define the SuperHero class
# =========================================================
class SuperHero:
    def __init__(self, name, power, health):
        self.name = name      # superhero's name (string)
        self.power = power    # superhero's ability/power (string)
        self.health = health  # current health points (int)

    # Add new ability: attack()
    def attack(self):
        """Prints a message showing the hero attacking with their power."""
        print(f"{self.name} attacks with {self.power}!")

    # Add new ability: heal()
    def heal(self):
        """Increases health by 10 and prints the updated value."""
        self.health += 10
        print(f"{self.name} heals 10 points. New health: {self.health}.")


# =========================================================
# 🧪 Step 2: Create an instance and test the abilities
# =========================================================
if __name__ == "__main__":
    # Create a superhero named Catwoman
    catwoman = SuperHero("Catwoman", "Agility", 120)

    # Call the abilities
    catwoman.attack()
    catwoman.heal()


"""
=========================================================
✅ Expected Output
---------------------------------------------------------
Catwoman attacks with Agility!
Catwoman heals 10 points. New health: 130
=========================================================

Complexity:
- Time Complexity: O(1) per method (constant operations)
- Space Complexity: O(1) (only attributes stored per object)
=========================================================
"""
