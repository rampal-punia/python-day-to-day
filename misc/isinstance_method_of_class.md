# Isintance method of Python Class

The isinstance() method is used to check if an object is an instance of a particular class or a subclass of that class. It returns True if the object is an instance of the specified class, and False otherwise.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Dino", "Poodle")
print(isinstance(dog1, Dog))
```

The isinstance() method is then used to check whether dog1 is an instance of the Dog class. Since dog1 was created using the Dog class, the isinstance() method returns True.

If we create an instance of another class or a built-in type, isinstance() will return False. For example:

```python
list1 = [1, 2, 3]
print(isinstance(list1, Dog))  # Output: False
```

Here, list1 is an instance of the list class, not the Dog class, so isinstance(list1, Dog) returns False.

The second argument to the isinstance function is the type or types to check against. It can be a single type or a tuple of types. If a tuple of types is provided, isinstance returns True if the object is an instance of any of the types in the tuple.

For example:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Dino", "Poodle")
cat1 = Cat("Kitty", "Siamese")

print(isinstance(dog1, (Dog, Cat)))  # True
print(isinstance(cat1, (Dog, Cat)))  # True
print(isinstance(dog1, tuple))      # False
```

In the above example, we define two classes Dog and Cat, and create instances of these classes dog1 and cat1. We use isinstance to check if these instances are of type Dog or Cat. Since dog1 is an instance of Dog and cat1 is an instance of Cat, both isinstance calls return True. We also use isinstance to check if dog1 is an instance of the tuple type, which returns False.
