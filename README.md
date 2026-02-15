<div align="center">

# 🐍 Python Day-To-Day

### A Curated Collection of Python Code Examples, Tutorials & Projects

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Twitter](https://img.shields.io/badge/Follow-@rs__punia__-1DA1F2?logo=x&logoColor=white)](https://x.com/rs_punia_)

**110+ Python scripts** | **49 tutorials** | **21 topic modules** | From beginner to advanced

*Learn Python through practical, well-documented, and runnable code examples.*

[Get Started](#-quick-start) · [Topics](#-topics-at-a-glance) · [Contribute](#-contributing)

</div>

---

## ✨ What Makes This Repo Special?

- **🏃 Runnable examples** — Every `.py` file runs standalone with demo output
- **📖 Well-documented** — Detailed comments, docstrings, and markdown tutorials
- **📈 Progressive difficulty** — From basics to production-grade patterns
- **🔬 Real-world patterns** — ETL pipelines, caching, config layering, and more
- **🧩 Modular** — Each topic is self-contained, learn in any order

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/rampal-punia/python-day-to-day.git
cd python-day-to-day

# Run any script directly
python functions/decorators_deep_dive.py
python generators/06_advanced_generators.py
python beginners_projects/tic_tac_toe.py
```

> **Requires Python 3.10+** for match/case examples. Most other files work with Python 3.8+.

---

## 📚 Topics at a Glance

### 🟢 Fundamentals

| Topic | Files | Highlights |
|:------|:-----:|:-----------|
| [**conditions/**](conditions/) | 2 | Ternary, chained comparisons, walrus `:=`, `match/case` (3.10+), guard clauses |
| [**strings/**](strings/) | 9 | f-string mastery, all string methods, regex patterns, slicing, palindromes |
| [**numbers/**](numbers/) | 5 | Number formatting, prime number algorithms (4 approaches) |
| [**lists/**](lists/) | 9 | Comprehensions, slicing, sorting, `bisect`, copy patterns, stack/queue, `zip` |
| [**tuple/**](tuple/) | 4 | Immutability, unpacking, namedtuple, tuple-as-dict-key, performance comparison |
| [**dictionary/**](dictionary/) | 5 | Comprehensions, merging (`\|`), `defaultdict`, nested dicts, grouping/aggregation |
| [**sets/**](sets/) | 16 | Every set method documented — union, intersection, difference, subset, superset |

### 🟡 Intermediate

| Topic | Files | Highlights |
|:------|:-----:|:-----------|
| [**functions/**](functions/) | 15 | Decorators deep dive, `*args/**kwargs`, closures & LEGB scope, `functools`, lambda/map/filter/reduce |
| [**generators/**](generators/) | 8 | Lazy evaluation, pipelining, `yield from`, `send()`, ETL pipeline, `itertools` |
| [**collections_module/**](collections_module/) | 6 | `deque` (BFS, sliding window), `defaultdict`, `Counter`, `ChainMap`, performance benchmarks |
| [**datetime/**](datetime/) | 7 | Timezones (`zoneinfo`), `timedelta`, parsing/formatting, calendar, countdown timer |
| [**dataclasses/**](dataclasses/) | 3 | Tutorial, `field()`, `__post_init__`, dataclass vs class comparison |
| [**named_tuple/**](named_tuple/) | 3 | Tutorials, alternate constructors, comparison with dataclasses |

### 🔴 Applied & Projects

| Topic | Files | Highlights |
|:------|:-----:|:-----------|
| [**beginners_projects/**](beginners_projects/) | 10 | Tic-Tac-Toe (with AI), password checker/generator, todo manager, RPS, dice, FizzBuzz |
| [**operations_on_images/**](operations_on_images/) | 8 | Resize, rotate, grayscale, thumbnail, format conversion (OpenCV + PIL) |
| [**pathlib_organise_files_project/**](pathlib_organise_files_project/) | 4 | File organizer project, `pathlib` tutorial, sample files for practice |
| [**logging/**](logging/) | 1 | Loggers, handlers, formatters, console + file logging |
| [**misc/**](misc/) | 10 | `asyncio`, `colorama`, object sizes, Python easter eggs, keywords |

### 📝 Reference & Learning

| Topic | Files | Highlights |
|:------|:-----:|:-----------|
| [**python_FAQs/**](python_FAQs/) | 12 | `__name__`, deep vs shallow copy, truthy/falsy, polymorphism, parameters vs arguments |
| [**python_quizzes/**](python_quizzes/) | 19 | "What's the output?" challenges — test your Python knowledge |
| [**random_module/**](random_module/) | 3 | `random.choice`, RGB generation, sampling |

---

## 🗂️ Directory Structure

```
python-day-to-day/
│
├── 🟢 FUNDAMENTALS
│   ├── conditions/              # if/elif, match/case, walrus operator
│   ├── strings/                 # formatting, methods, regex, slicing
│   ├── numbers/                 # formatting, prime algorithms
│   ├── lists/                   # comprehensions, slicing, sorting, bisect
│   ├── tuple/                   # immutability, unpacking, named tuples
│   ├── dictionary/              # comprehensions, merging, nested access
│   └── sets/                    # all set operations & methods
│
├── 🟡 INTERMEDIATE
│   ├── functions/               # decorators, closures, functools, lambda
│   ├── generators/              # lazy eval, pipelines, yield from, send()
│   ├── collections_module/      # deque, defaultdict, Counter, ChainMap
│   ├── datetime/                # timezones, timedelta, formatting
│   ├── dataclasses/             # modern Python data containers
│   └── named_tuple/             # lightweight immutable objects
│
├── 🔴 PROJECTS & APPLIED
│   ├── beginners_projects/      # games, tools, practical apps
│   ├── operations_on_images/    # OpenCV & PIL image processing
│   ├── pathlib_organise_files_project/  # file organizer
│   ├── logging/                 # production logging patterns
│   └── misc/                    # asyncio, colorama, curiosities
│
└── 📝 REFERENCE
    ├── python_FAQs/             # frequently asked questions
    ├── python_quizzes/          # test your knowledge
    └── random_module/           # random number generation
```

---

## 🌟 Featured Examples

### Decorators — From Basics to Production Patterns
```python
# functions/decorators_deep_dive.py — 8 decorator patterns
@retry(max_attempts=3, delay=0.5)
def unreliable_api_call():
    """Auto-retry on failure — a real production pattern."""
    ...

@timer
def compute_sum(n: int) -> int:
    """Measure execution time automatically."""
    return sum(range(n))
```

### Generators — ETL Pipeline
```python
# generators/06_advanced_generators.py
pipeline = add_tax(
    filter_valid(
        normalize(
            parse_records(raw_data)   # Each stage processes lazily
        )
    )
)
# Memory-efficient: processes 1 record at a time, not all at once!
```

### Pattern Matching (Python 3.10+)
```python
# conditions/conditions_complete_guide.py
def process_event(event: dict):
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"Click at ({x}, {y})"
        case {"type": "keypress", "key": key}:
            return f"Key pressed: {key}"
```

### Collections — Sliding Window with Deque
```python
# collections_module/collections_deep_dive.py
recent_logs = deque(maxlen=100)  # Auto-drops oldest when full
recent_logs.append(new_log)      # Always O(1), never exceeds 100
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-topic`)
3. **Add** well-documented, runnable Python files
4. **Submit** a pull request

### Contribution Guidelines
- Every `.py` file should be **runnable standalone** with `if __name__ == "__main__"`
- Include **clear comments** and **docstrings**
- Add **practical examples**, not just theory
- Follow the existing file structure and naming conventions

---

## 📬 Connect

I share Python tips, code snippets, and learning resources regularly:

- **𝕏 (Twitter):** [@rs_punia_](https://x.com/rs_punia_)

---

<div align="center">

### ⭐ If you find this repository helpful, give it a star!

*Learning Python is Fun. Keep Improving!* 🚀

</div>
