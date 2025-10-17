# 🧩 Chapter 1: Introduction to Object-Oriented Programming (OOP)

### 📘 Overview
This chapter introduces **Object-Oriented Programming (OOP)** in Python through simple, readable exercises like  
`Add Superhero Abilities`, `Design Parking System`, and `Design Twitter`.

The purpose here is not difficulty — but **familiarity**.

We’ll learn how to:
- Use **classes** to bundle data (attributes) and behavior (methods).
- Understand the role of `self` and constructors (`__init__`).
- Design **encapsulated systems** (like a parking lot or social feed).
- Develop **intuitive thinking** in terms of *objects interacting with each other*.

> 🧠 **Important:**  
> This chapter is meant to *build comfort*, not to test mastery.  
> Expect small, clear problems with direct logic and short code.  
> You’ll face deeper design trade-offs in later chapters.

---

### 🏗️ What Is Object-Oriented Programming?

OOP is a way to organize your code by grouping related data and actions together.  
Think of it as building **blueprints** for objects that can act on their own.

| Concept | Example | Meaning |
|----------|----------|----------|
| **Class** | `class SuperHero:` | A *blueprint* (like a design for a building). |
| **Object / Instance** | `catwoman = SuperHero("Catwoman", "Agility", 120)` | A *real* building created from the blueprint. |
| **Attributes** | `self.name`, `self.health` | Data that belongs to each object. |
| **Methods** | `attack()`, `heal()` | Functions that define what objects *can do*. |
| **Encapsulation** | Keeping internal data protected (through methods). | Keeps data consistent and prevents direct manipulation. |
| **Abstraction** | Hiding details, showing only behavior. | You know what it does, not how. |
| **Inheritance** | Child classes reusing or extending parent class features. | Lets you build hierarchies. |
| **Polymorphism** | Same interface, different behavior. | Makes code flexible and dynamic. |

Example snippet from `Add Superhero Abilities`:

```python
class SuperHero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    def heal(self):
        self.health += 10
        print(f"{self.name} heals 10 points. New health: {self.health}.")
```

### 🧱 How We Apply OOP Here

Each small project in **Week 12 (OOP + Design)** builds on the previous one, gradually introducing new ideas about class design, data management, and system behavior.

| File | Concept Focus | What You’ll Learn |
|------|----------------|-------------------|
| **0. Familiar_with_OOP_question.py** | Warm-up reflection | A few simple print-based or mini-class questions to recall what classes, objects, and methods mean in Python. |
| **1. [Easy] Design Data structure Two Sum.py** | Data encapsulation | Shows how to wrap a simple data structure (like a list or hash map) into a class with controlled access — the first step from procedural to OOP thinking. |
| **2. [Easy] Design Parking System.py** | Encapsulation & state tracking | How to manage internal counts safely using attributes and methods — a gentle first design example. |
| **3. [Easy] Mars Rover.py** | Object state & movement logic | Simulates an object that reacts to commands and maintains position, direction, and boundary limits — introduces behavior tied to state. |
| **4. [Medium] Design Twitter.py** | Composition of multiple entities | Models how objects (users, tweets, relationships) interact. You’ll see how multiple classes can cooperate in a small system. |
| **5. [Medium] LRU Cache.py** | Data structure + OOP integration | Combines OOP with an internal data structure (doubly linked list + dict) for efficient caching — introduces time/space trade-offs. |
| **6. [Medium] LFU Cache.py** | Frequency-based state management | Extends the caching concept with frequency buckets and internal coordination between linked lists and maps. Demonstrates advanced object collaboration. |

---

### 💬 Note

This **chapter is intentionally easy and familiar**.  
Its goal is to **help you think in terms of objects**, not to challenge you with algorithmic complexity.

You should:
- Feel comfortable with syntax like `class Name:`, `self`, and `__init__()`.  
- Understand how data and functions combine into *behavior*.  
- Begin to visualize programs as *systems of small cooperating objects.*

Later chapters (starting from `Design LRU Cache` and beyond) will gradually move from conceptual OOP to **system-level design** — where structure, efficiency, and coordination start to matter.

> 🧠 **Key mindset:**  
> Don’t worry about “hardness” here.  
> Focus on writing clear, readable code and understanding *why* we organize logic into objects.

---
## 🌟 Final Thoughts

Next up... → okay, there’s actually **no next up** 😅  

If you’ve made it this far — seriously, props to you.  
I hope these chapters were useful, not just for solving coding questions, but for helping you understand **how to think** through problems step by step.  

And honestly... I really, *really* hope you land that dream job.  
Go out there, build cool stuff, and someday help others who are just as curious and willing to learn as you once were.  

Keep coding. Keep growing. Keep believing that you’ll figure it out — because you absolutely will.  

All the best for your upcoming interviews 💪  
and hey, maybe one day... **I’ll meet you at the top. 🚀**
