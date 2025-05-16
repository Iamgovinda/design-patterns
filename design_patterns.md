# What Are Design Patterns?

Design patterns are **standard solutions** to common problems that software developers face when writing code. Think of them as **templates or blueprints** that help you organize your code in a clear, reusable, and efficient way.

Instead of solving a problem from scratch every time, design patterns provide **proven approaches** that make your code easier to understand, maintain, and extend.

# What does the pattern consist of?
Most patterns are described very formally so people can reproduce them in many contexts. Here are the sections that are usually present in a pattern description:

- **Intent** of the pattern briefly describes both the problem and the solution.
- **Motivation** further explains the problem and the solution the pattern makes possible.
- **Structure of classes** shows each part of the pattern and how they are related.
- **Code example** in one of the popular programming languages makes it easier to grasp the idea behind the pattern.


## Example: The Singleton Pattern

Imagine you are building an app where only **one** database connection should exist at a time to avoid conflicts. The Singleton pattern helps you **ensure there is only one instance** of that database connection throughout the app.

```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True, both variables point to the same instance
