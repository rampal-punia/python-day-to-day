"""
Decorators Deep Dive — From Basics to Advanced Patterns
========================================================
Decorators are one of Python's most powerful features.
They modify or enhance functions/classes without changing their source code.

Author: @rampal-punia
"""

import time
import functools
from typing import Callable, Any


# ─────────────────────────────────────────────────
# 1. BASIC DECORATOR — Understanding the Pattern
# ─────────────────────────────────────────────────


def simple_logger(func: Callable) -> Callable:
    """Logs function calls with arguments and return value."""

    @functools.wraps(func)  # preserves __name__, __doc__ of original function
    def wrapper(*args, **kwargs):
        print(f"📞 Calling: {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} returned: {result}")
        return result

    return wrapper


@simple_logger
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# ─────────────────────────────────────────────────
# 2. DECORATOR WITH ARGUMENTS (Decorator Factory)
# ─────────────────────────────────────────────────


def repeat(n: int = 2):
    """Repeat a function call n times and return last result."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
                print(f"  Run {i+1}/{n}: {result}")
            return result

        return wrapper

    return decorator


@repeat(n=3)
def greet(name: str) -> str:
    return f"Hello, {name}! 👋"


# ─────────────────────────────────────────────────
# 3. TIMING DECORATOR — Real-World Performance Tool
# ─────────────────────────────────────────────────


def timer(func: Callable) -> Callable:
    """Measure and display execution time."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️  {func.__name__} took {elapsed:.6f}s")
        return result

    return wrapper


@timer
def compute_sum(n: int) -> int:
    """Sum numbers from 0 to n."""
    return sum(range(n))


# ─────────────────────────────────────────────────
# 4. MEMOIZATION DECORATOR — Caching Results
# ─────────────────────────────────────────────────


def memoize(func: Callable) -> Callable:
    """Cache function results to avoid redundant computation."""
    cache: dict = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"  💾 Cache hit for {func.__name__}{args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    wrapper.cache = cache  # expose cache for inspection
    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """Compute nth Fibonacci number recursively."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Compare with built-in: functools.lru_cache
@functools.lru_cache(maxsize=128)
def fibonacci_builtin(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_builtin(n - 1) + fibonacci_builtin(n - 2)


# ─────────────────────────────────────────────────
# 5. STACKING DECORATORS — Order Matters!
# ─────────────────────────────────────────────────


def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"

    return wrapper


def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"

    return wrapper


@bold  # applied second (outer)
@italic  # applied first (inner)
def styled_text(text: str) -> str:
    return text


# styled_text("hello") → "<b><i>hello</i></b>"
# Execution: bold(italic(styled_text))("hello")


# ─────────────────────────────────────────────────
# 6. CLASS-BASED DECORATOR
# ─────────────────────────────────────────────────


class CountCalls:
    """Decorator that counts how many times a function is called."""

    def __init__(self, func: Callable):
        functools.update_wrapper(self, func)
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"📊 {self.func.__name__} called {self.call_count} time(s)")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


# ─────────────────────────────────────────────────
# 7. RETRY DECORATOR — Production-Grade Pattern
# ─────────────────────────────────────────────────


def retry(max_attempts: int = 3, delay: float = 1.0):
    """Retry a function on failure with configurable attempts and delay."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"⚠️  Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception

        return wrapper

    return decorator


@retry(max_attempts=3, delay=0.5)
def unreliable_api_call():
    """Simulates an API that might fail."""
    import random

    if random.random() < 0.7:
        raise ConnectionError("Server unavailable")
    return {"status": "success", "data": [1, 2, 3]}


# ─────────────────────────────────────────────────
# 8. VALIDATE TYPES DECORATOR
# ─────────────────────────────────────────────────


def validate_types(*types):
    """Validate argument types at runtime."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Expected {expected_type.__name__}, "
                        f"got {type(arg).__name__}: {arg!r}"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_types(str, int)
def create_user(name: str, age: int) -> dict:
    return {"name": name, "age": age}


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("1. Simple Logger Decorator")
    print("=" * 55)
    add(3, 5)

    print("\n" + "=" * 55)
    print("2. Repeat Decorator")
    print("=" * 55)
    greet("Python")

    print("\n" + "=" * 55)
    print("3. Timer Decorator")
    print("=" * 55)
    compute_sum(1_000_000)

    print("\n" + "=" * 55)
    print("4. Memoize Decorator")
    print("=" * 55)
    print(f"fibonacci(10) = {fibonacci(10)}")

    print("\n" + "=" * 55)
    print("5. Stacked Decorators")
    print("=" * 55)
    print(styled_text("Python is awesome"))

    print("\n" + "=" * 55)
    print("6. Class-Based Decorator")
    print("=" * 55)
    say_hello("Alice")
    say_hello("Bob")
    print(f"   Total calls: {say_hello.call_count}")

    print("\n" + "=" * 55)
    print("7. Type Validation Decorator")
    print("=" * 55)
    print(create_user("Alice", 30))
    try:
        create_user("Bob", "thirty")  # Will raise TypeError
    except TypeError as e:
        print(f"❌ TypeError: {e}")
