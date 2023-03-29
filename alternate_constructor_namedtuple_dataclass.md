# An alternative constructor using class methods in both named tuples and dataclasses

an example code for defining an alternative constructor using class methods in both named tuples and dataclasses:

```python
from typing import Tuple
from dataclasses import dataclass
from collections import namedtuple


# Example 1: Named Tuple with Alternative Constructor
PointTuple = namedtuple('PointTuple', ['x', 'y'])

class PointTuple(PointTuple):
    @classmethod
    def from_string(cls, string: str) -> 'PointTuple':
        x, y = map(int, string.split(','))
        return cls(x=x, y=y)

# Usage
pt1 = PointTuple(x=1, y=2)
pt2 = PointTuple.from_string('3,4')
print(pt1)  # PointTuple(x=1, y=2)
print(pt2)  # PointTuple(x=3, y=4)


# Example 2: Dataclass with Alternative Constructor
@dataclass
class PointDataclass:
    x: int
    y: int
    
    @classmethod
    def from_string(cls, string: str) -> 'PointDataclass':
        x, y = map(int, string.split(','))
        return cls(x=x, y=y)

# Usage
pt3 = PointDataclass(x=5, y=6)
pt4 = PointDataclass.from_string('7,8')
print(pt3)  # PointDataclass(x=5, y=6)
print(pt4)  # PointDataclass(x=7, y=8)
```

In both examples, we define an alternative constructor from_string that takes a string in the format "x,y" and creates a new point instance with the specified coordinates. We use the @classmethod decorator to indicate that this is a class method that should be called on the class itself (rather than on an instance of the class).

In the first example, we define a named tuple PointTuple and then subclass it to add the from_string method. In the second example, we use the @dataclass decorator to define a dataclass PointDataclass and add the from_string method to it.

Both examples illustrate how you can define alternative constructors for named tuples and dataclasses to provide additional ways to create instances of the class.
