"""Colorama Colors — Produce colored terminal text & backgrounds.

Difficulty: 🟢 Easy
Topics: colorama, Fore, Back, Style, terminal formatting
Requires: pip install colorama

Important: Always call Style.RESET_ALL after colored text,
otherwise the color bleeds into subsequent output.

Author: @rampal-punia
"""

from colorama import Fore, Back, Style, init


def demo_colors() -> None:
    """Demonstrate foreground colors, backgrounds, and styles."""
    # init() is needed on Windows for ANSI escape code support
    init(autoreset=True)  # autoreset resets style after each print

    print("── Foreground Colors ──")
    print(Fore.RED + "  This text is Red")
    print(Fore.GREEN + "  This text is Green")
    print(Fore.BLUE + "  This text is Blue")
    print(Fore.YELLOW + "  This text is Yellow")
    print(Fore.CYAN + "  This text is Cyan")
    print(Fore.MAGENTA + "  This text is Magenta")

    print("\n── Background Colors ──")
    print(Back.WHITE + Fore.BLACK + "  White background, black text")
    print(Back.RED + "  Red background")
    print(Back.GREEN + Fore.BLACK + "  Green background, black text")

    print("\n── Styles ──")
    print(Style.BRIGHT + "  Bright/Bold text")
    print(Style.DIM + "  Dim text")
    print(Style.NORMAL + "  Normal text (reset applied)")

    # With autoreset=True, no manual reset needed
    print("\nThis line has normal colors (autoreset worked).")


if __name__ == "__main__":
    demo_colors()
