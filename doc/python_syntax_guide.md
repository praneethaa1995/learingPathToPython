# Python Syntax Guide — Basic to Expert

---

## 1. Variables & Data Types

```python
x = 10                  # int
y = 3.14                # float
name = "Alice"          # str
flag = True             # bool
nothing = None          # NoneType

# Type casting
int("42")               # 42
float("3.14")           # 3.14
str(100)                # "100"
bool(0)                 # False

# Type checking
type(x)                 # <class 'int'>
isinstance(x, int)      # True
```

---

## 2. Strings

```python
s = "Hello, World!"

s.upper()               # "HELLO, WORLD!"
s.lower()               # "hello, world!"
s.strip()               # removes whitespace
s.replace("Hello", "Hi")
s.split(", ")           # ["Hello", "World!"]
s.startswith("Hello")   # True
len(s)                  # 13

# f-strings
name = "Alice"
f"Hello, {name}!"       # "Hello, Alice!"
f"{3.14:.2f}"           # "3.14"

# Multiline
text = """
Line 1
Line 2
"""

# Slicing
s[0:5]                  # "Hello"
s[::-1]                 # reversed
```

---

## 3. Collections

```python
# List
lst = [1, 2, 3]
lst.append(4)
lst.pop()
lst[0]                  # 1
lst[-1]                 # last element
lst[1:3]                # [2, 3]
lst.sort()
lst.reverse()

# Tuple (immutable)
t = (1, 2, 3)
t[0]                    # 1

# Set
s = {1, 2, 3}
s.add(4)
s.remove(2)
s1 & s2                 # intersection
s1 | s2                 # union
s1 - s2                 # difference

# Dictionary
d = {"key": "value", "age": 25}
d["age"]                # 25
d.get("missing", 0)     # 0
d.keys()
d.values()
d.items()
d.update({"city": "NY"})
```

---

## 4. Operators

```python
# Arithmetic
+  -  *  /  //  %  **

# Comparison
==  !=  >  <  >=  <=

# Logical
and  or  not

# Identity & Membership
x is None
x is not None
"a" in "abc"            # True
3 not in [1, 2]         # True

# Walrus operator (3.8+)
if n := len(lst):
    print(n)
```

---

## 5. Conditionals

```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Ternary
result = "yes" if x > 0 else "no"

# Match-case (3.10+)
match command:
    case "quit":
        quit()
    case "go" | "move":
        move()
    case _:
        print("unknown")
```

---

## 6. Loops

```python
# for
for i in range(5):          # 0 to 4
    print(i)

for i in range(1, 10, 2):   # 1,3,5,7,9
    pass

for i, v in enumerate(lst):
    print(i, v)

for k, v in d.items():
    print(k, v)

# while
while x > 0:
    x -= 1

# Loop control
break       # exit loop
continue    # skip iteration
else:       # runs if loop completes without break
    pass
```

---

## 7. Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# *args and **kwargs
def func(*args, **kwargs):
    print(args)     # tuple
    print(kwargs)   # dict

# Keyword-only args
def func(a, *, b):  # b must be keyword
    pass

# Positional-only args (3.8+)
def func(a, b, /):  # a,b must be positional
    pass

# Lambda
square = lambda x: x ** 2

# Annotations
def add(a: int, b: int) -> int:
    return a + b
```

---

## 8. Comprehensions

```python
# List
[x**2 for x in range(10)]
[x for x in range(10) if x % 2 == 0]

# Dict
{k: v for k, v in d.items()}

# Set
{x**2 for x in range(5)}

# Generator
(x**2 for x in range(10))
```

---

## 9. Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)
except (TypeError, ValueError):
    pass
else:
    print("no error")
finally:
    print("always runs")

# Raise
raise ValueError("bad value")

# Custom exception
class MyError(Exception):
    pass
```

---

## 10. File I/O

```python
# Read
with open("file.txt", "r") as f:
    content = f.read()
    lines = f.readlines()

# Write
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Append
with open("file.txt", "a") as f:
    f.write("more\n")

# Binary
with open("img.png", "rb") as f:
    data = f.read()
```

---

## 11. Classes & OOP

```python
class Animal:
    species = "Unknown"             # class variable

    def __init__(self, name):
        self.name = name            # instance variable

    def speak(self):
        return f"{self.name} speaks"

    @classmethod
    def create(cls, name):          # class method
        return cls(name)

    @staticmethod
    def info():                     # static method
        return "I am an animal"

    def __repr__(self):
        return f"Animal({self.name})"

    def __str__(self):
        return self.name


# Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


# Multiple inheritance
class A: pass
class B: pass
class C(A, B): pass

# Dunder methods
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2

    def __getitem__(self, i):
        return (self.x, self.y)[i]
```

---

## 12. Modules & Packages

```python
import os
import sys
from math import sqrt, pi
from collections import defaultdict, Counter, deque
import json
import re

# __name__ guard
if __name__ == "__main__":
    main()
```

---

## 13. Iterators & Generators

```python
# Iterator protocol
class Counter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i

# Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator with send/throw
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

# yield from
def chain(*iterables):
    for it in iterables:
        yield from it
```

---

## 14. Decorators

```python
# Basic decorator
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@decorator
def say_hello():
    print("hello")

# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("hi")

# functools.wraps (preserves metadata)
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Class-based decorator
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"Elapsed: {time.time() - start:.4f}s")
        return result
```

---

## 15. Context Managers

```python
# Using contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("setup")
    try:
        yield
    finally:
        print("teardown")

with managed_resource():
    print("using resource")

# Class-based
class ManagedFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # don't suppress exceptions
```

---

## 16. Functional Programming

```python
from functools import reduce, partial, lru_cache

# map, filter, reduce
list(map(str, [1, 2, 3]))
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))
reduce(lambda a, b: a + b, [1, 2, 3, 4])   # 10

# partial
def power(base, exp): return base ** exp
square = partial(power, exp=2)

# lru_cache (memoization)
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
```

---

## 17. Type Hints (3.5+)

```python
from typing import List, Dict, Tuple, Optional, Union, Any, Callable
from typing import TypeVar, Generic

def greet(name: str) -> str:
    return f"Hello, {name}"

def process(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items)}

def maybe(x: Optional[int] = None) -> int:
    return x or 0

# Union (use | in 3.10+)
def func(x: Union[int, str]) -> None: pass
def func(x: int | str) -> None: pass   # 3.10+

# TypeVar
T = TypeVar("T")
def first(lst: List[T]) -> T:
    return lst[0]

# Protocols (structural subtyping)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...
```

---

## 18. Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
    tags: list = field(default_factory=list)

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5

@dataclass(frozen=True)   # immutable
class Color:
    r: int
    g: int
    b: int

@dataclass(order=True)    # enables <, >, ==
class Version:
    major: int
    minor: int
    patch: int
```

---

## 19. Async / Await

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)      # non-blocking wait
    return f"data from {url}"

async def main():
    # Sequential
    result = await fetch("http://example.com")

    # Concurrent
    results = await asyncio.gather(
        fetch("http://a.com"),
        fetch("http://b.com"),
    )

asyncio.run(main())

# Async generator
async def arange(n):
    for i in range(n):
        await asyncio.sleep(0)
        yield i

# Async context manager
class AsyncDB:
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass
```

---

## 20. Metaclasses

```python
# Basic metaclass
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)

class MyClass(metaclass=Meta):
    pass

# __init_subclass__ (simpler alternative)
class Plugin:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry.append(cls)

class MyPlugin(Plugin): pass
```

---

## 21. Descriptors

```python
class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be int")
        obj.__dict__[self.name] = value

class MyClass:
    age = Validator()
```

---

## 22. Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self):
        return f"Area: {self.area()}"

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14 * self.r
```

---

## 23. Slots

```python
class Point:
    __slots__ = ("x", "y")   # reduces memory, faster attribute access

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 24. Enums

```python
from enum import Enum, auto, Flag

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

Color.RED           # <Color.RED: 1>
Color.RED.value     # 1
Color.RED.name      # "RED"
Color(1)            # <Color.RED: 1>

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXEC = auto()
    ALL = READ | WRITE | EXEC
```

---

## 25. Regular Expressions

```python
import re

re.match(r"\d+", "123abc")          # match at start
re.search(r"\d+", "abc123")         # search anywhere
re.findall(r"\d+", "a1b2c3")        # ["1", "2", "3"]
re.sub(r"\d+", "#", "a1b2")         # "a#b#"
re.split(r"\s+", "a b  c")          # ["a", "b", "c"]

# Groups
m = re.search(r"(\w+)@(\w+)", "user@host")
m.group(1)                          # "user"
m.group(2)                          # "host"

# Named groups
m = re.search(r"(?P<user>\w+)@(?P<host>\w+)", "user@host")
m.group("user")                     # "user"

# Compiled pattern
pattern = re.compile(r"\d+", re.IGNORECASE)
```

---

## 26. Collections Module

```python
from collections import (
    defaultdict, Counter, deque,
    OrderedDict, namedtuple, ChainMap
)

# defaultdict
dd = defaultdict(list)
dd["key"].append(1)

# Counter
c = Counter("abracadabra")
c.most_common(2)            # [('a', 5), ('b', 2)]

# deque (O(1) append/pop from both ends)
dq = deque([1, 2, 3], maxlen=5)
dq.appendleft(0)
dq.popleft()

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x, p.y

# ChainMap
defaults = {"color": "red"}
overrides = {"color": "blue"}
merged = ChainMap(overrides, defaults)
```

---

## 27. Pathlib

```python
from pathlib import Path

p = Path(".")
p / "subdir" / "file.txt"      # path joining
p.exists()
p.is_file()
p.is_dir()
p.stem                          # filename without extension
p.suffix                        # ".txt"
p.parent
p.name

list(p.glob("*.py"))
list(p.rglob("*.py"))           # recursive

p.read_text()
p.write_text("content")
p.mkdir(parents=True, exist_ok=True)
```

---

## 28. Concurrency

```python
# Threading
from threading import Thread, Lock

lock = Lock()

def task():
    with lock:
        print("thread-safe")

t = Thread(target=task)
t.start()
t.join()

# Multiprocessing
from multiprocessing import Process, Pool

with Pool(4) as pool:
    results = pool.map(lambda x: x**2, range(10))

# ThreadPoolExecutor / ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=4) as ex:
    futures = [ex.submit(task, arg) for arg in args]
    results = [f.result() for f in futures]
```

---

## 29. Logging

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)
logger.debug("debug message")
logger.info("info message")
logger.warning("warning")
logger.error("error")
logger.critical("critical")

# File handler
handler = logging.FileHandler("app.log")
logger.addHandler(handler)
```

---

## 30. Testing

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.x = 10

    def test_add(self):
        self.assertEqual(self.x + 5, 15)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def tearDown(self):
        pass

# pytest style
def test_add():
    assert 1 + 1 == 2

def test_raises():
    import pytest
    with pytest.raises(ValueError):
        int("abc")
```

---

## 31. Packing & Unpacking

```python
a, b, c = 1, 2, 3
first, *rest = [1, 2, 3, 4]        # first=1, rest=[2,3,4]
*init, last = [1, 2, 3, 4]         # init=[1,2,3], last=4

# Swap
a, b = b, a

# Unpack in function call
args = [1, 2, 3]
func(*args)

kwargs = {"a": 1, "b": 2}
func(**kwargs)

# Merge dicts (3.9+)
merged = {**dict1, **dict2}
merged = dict1 | dict2
```

---

## 32. Useful Built-ins

```python
abs(-5)             # 5
all([True, True])   # True
any([False, True])  # True
bin(10)             # "0b1010"
chr(65)             # "A"
dir(obj)            # list attributes
divmod(10, 3)       # (3, 1)
enumerate(lst)
filter(func, lst)
getattr(obj, "name", default)
hasattr(obj, "name")
hash(obj)
hex(255)            # "0xff"
id(obj)
iter(lst)
len(lst)
map(func, lst)
max(lst)
min(lst)
next(iterator)
oct(8)              # "0o10"
ord("A")            # 65
pow(2, 10)          # 1024
print(*args, sep=" ", end="\n", file=sys.stdout)
range(start, stop, step)
repr(obj)
reversed(lst)
round(3.14159, 2)   # 3.14
setattr(obj, "name", value)
slice(1, 5, 2)
sorted(lst, key=func, reverse=True)
sum(lst, start=0)
vars(obj)           # __dict__
zip(lst1, lst2)
zip(*matrix)        # transpose
```

---

## 33. Walrus, Assignment Expressions

```python
# Avoid double computation
if (n := len(data)) > 10:
    print(f"Too long: {n}")

# In while loops
while chunk := f.read(8192):
    process(chunk)

# In comprehensions
results = [y for x in data if (y := process(x)) is not None]
```

---

## 34. Structural Pattern Matching (3.10+)

```python
match point:
    case (0, 0):
        print("origin")
    case (x, 0):
        print(f"x={x}")
    case (0, y):
        print(f"y={y}")
    case (x, y):
        print(f"x={x}, y={y}")

match command:
    case {"action": "move", "direction": d}:
        move(d)
    case {"action": "quit"}:
        quit()

match shape:
    case Circle(radius=r) if r > 0:
        print(f"circle r={r}")
    case Rectangle(width=w, height=h):
        print(f"rect {w}x{h}")
```

---

## 35. Performance Tips

```python
# Use local variables in tight loops (faster lookup)
local_append = lst.append

# Join strings with join, not +
"".join(["a", "b", "c"])

# Use sets for membership testing O(1) vs O(n)
if x in set(lst): pass

# Avoid global variables in hot paths
# Use __slots__ for memory-efficient classes
# Use generators instead of lists when possible
# Profile with cProfile
import cProfile
cProfile.run("main()")

# timeit
import timeit
timeit.timeit("x**2", setup="x=10", number=1_000_000)
```

---

*Generated for Python 3.10+*
