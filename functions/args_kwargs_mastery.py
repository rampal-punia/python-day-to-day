"""
*args and **kwargs — Flexible Function Arguments
==================================================
Master variable-length arguments in Python.

Author: @rampal-punia
"""

# ─────────────────────────────────────────────────
# 1. *args — Positional Variable Arguments
# ─────────────────────────────────────────────────


def sum_all(*args: int) -> int:
    """Accept any number of positional arguments."""
    print(f"  args = {args}")  # args is a tuple
    print(f"  type = {type(args)}")  # <class 'tuple'>
    return sum(args)


# ─────────────────────────────────────────────────
# 2. **kwargs — Keyword Variable Arguments
# ─────────────────────────────────────────────────


def build_profile(**kwargs: str) -> dict:
    """Accept any number of keyword arguments."""
    print(f"  kwargs = {kwargs}")  # kwargs is a dict
    print(f"  type   = {type(kwargs)}")  # <class 'dict'>
    return kwargs


# ─────────────────────────────────────────────────
# 3. COMBINING: Positional + *args + **kwargs
# ─────────────────────────────────────────────────
# Order: positional → *args → keyword → **kwargs


def create_order(customer: str, *items: str, discount: float = 0.0, **details):
    """
    Demonstrates all argument types together.

    Args:
        customer:  Required positional argument
        *items:    Variable positional arguments (menu items)
        discount:  Keyword-only argument with default
        **details: Variable keyword arguments (extra info)
    """
    total_items = len(items)
    print(f"  🧑 Customer : {customer}")
    print(f"  🍕 Items    : {items}")
    print(f"  💰 Discount : {discount}%")
    print(f"  📋 Details  : {details}")
    return {
        "customer": customer,
        "items": list(items),
        "total_items": total_items,
        "discount": discount,
        **details,
    }


# ─────────────────────────────────────────────────
# 4. UNPACKING — Passing sequences/dicts to functions
# ─────────────────────────────────────────────────


def display_coordinates(x: float, y: float, z: float) -> str:
    return f"({x}, {y}, {z})"


# ─────────────────────────────────────────────────
# 5. REAL-WORLD: Wrapper / Proxy Function Pattern
# ─────────────────────────────────────────────────


def debug_call(func, *args, **kwargs):
    """
    A wrapper that logs any function call — works with ANY function
    regardless of its signature, thanks to *args/**kwargs.
    """
    arg_str = ", ".join(
        [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
    )
    print(f"  🔍 {func.__name__}({arg_str})")
    result = func(*args, **kwargs)
    print(f"  ✅ → {result!r}")
    return result


# ─────────────────────────────────────────────────
# 6. KEYWORD-ONLY ARGUMENTS (after *)
# ─────────────────────────────────────────────────


def connect(host: str, port: int, *, timeout: int = 30, ssl: bool = True):
    """
    Parameters after * MUST be passed as keywords.
    connect("localhost", 8080, timeout=10)  ✅
    connect("localhost", 8080, 10)          ❌ TypeError
    """
    return {
        "host": host,
        "port": port,
        "timeout": timeout,
        "ssl": ssl,
    }


# ─────────────────────────────────────────────────
# 7. POSITIONAL-ONLY ARGUMENTS (before /) — Python 3.8+
# ─────────────────────────────────────────────────


def power(base, exp, /):
    """
    Parameters before / MUST be passed positionally.
    power(2, 10)        ✅
    power(base=2, exp=10)  ❌ TypeError
    """
    return base**exp


# ─────────────────────────────────────────────────
# 8. FULL SIGNATURE — Every Arg Type Combined
# ─────────────────────────────────────────────────


def ultimate(pos_only, /, normal, *args, kw_only, **kwargs):
    """
    pos_only  → positional-only (before /)
    normal    → regular (positional or keyword)
    *args     → extra positional
    kw_only   → keyword-only (after *)
    **kwargs  → extra keyword
    """
    return {
        "pos_only": pos_only,
        "normal": normal,
        "args": args,
        "kw_only": kw_only,
        "kwargs": kwargs,
    }


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("1. *args — Variable Positional Arguments")
    print("=" * 55)
    print(f"  sum_all(1,2,3,4,5) = {sum_all(1, 2, 3, 4, 5)}")

    print("\n" + "=" * 55)
    print("2. **kwargs — Variable Keyword Arguments")
    print("=" * 55)
    profile = build_profile(name="Alice", role="Dev", lang="Python")
    print(f"  Profile: {profile}")

    print("\n" + "=" * 55)
    print("3. Combined: pos + *args + kwarg + **kwargs")
    print("=" * 55)
    order = create_order(
        "Alice",
        "Pizza",
        "Pasta",
        "Coffee",
        discount=10.0,
        table=5,
        notes="No onions",
    )

    print("\n" + "=" * 55)
    print("4. Unpacking with * and **")
    print("=" * 55)
    coords = [10.5, 20.3, 30.1]
    print(f"  List unpacking:  {display_coordinates(*coords)}")

    config = {"x": 1.0, "y": 2.0, "z": 3.0}
    print(f"  Dict unpacking:  {display_coordinates(**config)}")

    print("\n" + "=" * 55)
    print("5. Proxy/Wrapper Function Pattern")
    print("=" * 55)
    debug_call(max, 10, 20, 30)
    debug_call(sorted, [3, 1, 2], reverse=True)

    print("\n" + "=" * 55)
    print("6. Keyword-Only Arguments")
    print("=" * 55)
    print(f"  {connect('db.example.com', 5432, timeout=10, ssl=False)}")

    print("\n" + "=" * 55)
    print("7. Positional-Only Arguments (Python 3.8+)")
    print("=" * 55)
    print(f"  power(2, 10) = {power(2, 10)}")

    print("\n" + "=" * 55)
    print("8. Full Signature Demo")
    print("=" * 55)
    result = ultimate("a", "b", "c", "d", kw_only="e", extra1="f", extra2="g")
    print(f"  {result}")
