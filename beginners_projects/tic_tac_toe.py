"""
Tic-Tac-Toe — Clean OOP Implementation
========================================
A terminal-based Tic-Tac-Toe game with AI opponent.

Author: @rampal-punia
"""

import random
from typing import Optional


class TicTacToe:
    """A complete Tic-Tac-Toe game with smart AI."""

    WINNING_COMBOS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),              # diagonals
    ]

    def __init__(self):
        self.board: list[str] = [" "] * 9
        self.current_player: str = "X"
        self.move_count: int = 0

    def display(self) -> None:
        """Print the current board state."""
        print()
        for i in range(0, 9, 3):
            row = " | ".join(
                f"\033[92m{c}\033[0m" if c == "X"
                else f"\033[91m{c}\033[0m" if c == "O"
                else str(i + j + 1)
                for j, c in enumerate(self.board[i:i+3])
            )
            print(f"    {row}")
            if i < 6:
                print(f"   {'---+---+---'}")

    def make_move(self, position: int) -> bool:
        """Place current player's mark. Returns True if valid."""
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = self.current_player
            self.move_count += 1
            return True
        return False

    def check_winner(self) -> Optional[str]:
        """Check if there's a winner. Returns 'X', 'O', or None."""
        for a, b, c in self.WINNING_COMBOS:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def is_draw(self) -> bool:
        """Check if the game is a draw."""
        return self.move_count == 9 and self.check_winner() is None

    def available_moves(self) -> list[int]:
        """Get list of available positions."""
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def switch_player(self) -> None:
        """Switch to the other player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    # ── AI: Minimax Algorithm ──
    def minimax(self, is_maximizing: bool) -> int:
        """
        Minimax algorithm — the AI plays perfectly.
        Returns the best score for the current state.
        """
        winner = self.check_winner()
        if winner == "O":
            return 1
        if winner == "X":
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for move in self.available_moves():
                self.board[move] = "O"
                self.move_count += 1
                score = self.minimax(False)
                self.board[move] = " "
                self.move_count -= 1
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for move in self.available_moves():
                self.board[move] = "X"
                self.move_count += 1
                score = self.minimax(True)
                self.board[move] = " "
                self.move_count -= 1
                best_score = min(score, best_score)
            return best_score

    def ai_move(self) -> int:
        """Find the best move for AI (O) using minimax."""
        best_score = -float("inf")
        best_move = self.available_moves()[0]

        for move in self.available_moves():
            self.board[move] = "O"
            self.move_count += 1
            score = self.minimax(False)
            self.board[move] = " "
            self.move_count -= 1

            if score > best_score:
                best_score = score
                best_move = move

        return best_move


def play_demo():
    """Demonstrate a game between random player and AI."""
    game = TicTacToe()

    print("  🎮 Tic-Tac-Toe: Random (X) vs AI (O)")
    print("  " + "=" * 40)

    game.display()

    while True:
        if game.current_player == "X":
            # Random player
            move = random.choice(game.available_moves())
            print(f"\n  ❌ X plays position {move + 1}")
        else:
            # AI player
            move = game.ai_move()
            print(f"\n  ⭕ O (AI) plays position {move + 1}")

        game.make_move(move)
        game.display()

        winner = game.check_winner()
        if winner:
            symbol = "❌" if winner == "X" else "⭕"
            print(f"\n  🏆 {symbol} {winner} wins!")
            break

        if game.is_draw():
            print(f"\n  🤝 It's a draw!")
            break

        game.switch_player()


if __name__ == "__main__":
    play_demo()
