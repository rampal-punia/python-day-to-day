"""Set Methods Demo — All built-in set methods with examples.

Difficulty: 🟢 Easy
Topics: set operations, add, remove, union, intersection, difference

Sets are unordered collections of unique elements.
They support mathematical set operations natively.

Author: @rampal-punia
"""


def demonstrate_set_methods() -> None:
    """Show every built-in set method with practical examples."""
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    print("── Set Operations ──")
    print(f"  a = {a}")
    print(f"  b = {b}")

    # Combining sets
    print(f"\n  union:             a | b  = {a | b}")
    print(f"  intersection:      a & b  = {a & b}")
    print(f"  difference:        a - b  = {a - b}")
    print(f"  symmetric_diff:    a ^ b  = {a ^ b}")

    # Subset / superset checks
    print(
        f"\n  {{1,2}} ⊆ a?  {{{1, 2}}} issubset:   {{1, 2}}.issubset(a)   = {{1, 2}}.issubset(a) -> {({1, 2}).issubset(a)}"
    )
    print(f"  a ⊇ {{1,2}}?  a.issuperset({{1,2}}) = {a.issuperset({1, 2})}")
    print(f"  a disjoint b? a.isdisjoint(b) = {a.isdisjoint(b)}")

    # Mutating methods
    demo = {1, 2, 3}
    print(f"\n── Mutating Methods ──")
    print(f"  Start:    {demo}")
    demo.add(4)
    print(f"  add(4):   {demo}")
    demo.discard(2)  # No error if missing
    print(f"  discard(2): {demo}")
    demo.remove(3)  # Raises KeyError if missing
    print(f"  remove(3):  {demo}")
    popped = demo.pop()
    print(f"  pop():      removed {popped}, remaining {demo}")
    demo.update({10, 20})
    print(f"  update({{10,20}}): {demo}")
    demo.clear()
    print(f"  clear():    {demo}")

    # Copy
    original = {1, 2, 3}
    shallow = original.copy()
    print(f"\n  copy: {shallow} (id differs: {id(original) != id(shallow)})")


if __name__ == "__main__":
    demonstrate_set_methods()
