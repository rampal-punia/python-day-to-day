"""Asyncio Examples — Async/await patterns from basic to HTTP fetching.

Difficulty: 🟡 Intermediate → 🔴 Advanced
Topics: asyncio, async/await, gather(), coroutines, aiohttp

Key concepts:
    - async def    → defines a coroutine function
    - await        → pauses until the awaited coroutine completes
    - asyncio.run  → entry point to run the event loop
    - gather()     → run multiple coroutines concurrently

Author: @rampal-punia
"""

import asyncio


# ── 🟡 Example 1: Basic async function ──


async def greet(name: str) -> str:
    """A simple coroutine that returns a greeting."""
    return f"Hello, {name}!"


async def example_basic() -> None:
    """Demonstrate calling a basic async function."""
    print("── Example 1: Basic Async ──")
    result = await greet("Python")
    print(f"  {result}")


# ── 🟡 Example 2: Concurrent execution with gather() ──


async def delayed_task(name: str, delay: float) -> str:
    """Simulate a task that takes `delay` seconds."""
    await asyncio.sleep(delay)
    msg = f"  Task '{name}' done after {delay}s"
    print(msg)
    return msg


async def example_gather() -> None:
    """Run multiple tasks concurrently with asyncio.gather()."""
    print("\n── Example 2: Concurrent with gather() ──")
    results = await asyncio.gather(
        delayed_task("fast", 0.5),
        delayed_task("medium", 1.0),
        delayed_task("slow", 1.5),
    )
    print(f"  All {len(results)} tasks completed.")


# ── 🔴 Example 3: HTTP fetching with aiohttp ──


async def example_fetch() -> None:
    """Fetch a webpage asynchronously (requires aiohttp)."""
    print("\n── Example 3: HTTP Fetch (aiohttp) ──")
    try:
        import aiohttp

        async with aiohttp.ClientSession() as session:
            async with session.get("http://httpbin.org/get") as response:
                data = await response.text()
                print(f"  Status: {response.status}")
                print(f"  Body (first 200 chars): {data[:200]}")
    except ImportError:
        print("  ⚠️  Install aiohttp: pip install aiohttp")
    except Exception as e:
        print(f"  ⚠️  Fetch failed: {e}")


async def main() -> None:
    """Run all async examples sequentially."""
    await example_basic()
    await example_gather()
    await example_fetch()


if __name__ == "__main__":
    asyncio.run(main())
