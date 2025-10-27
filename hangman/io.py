from hangman.game import init_state,is_won,is_lost,render_display,render_summary

def prompt_guess() -> str:
    return input('Guess a letter: ')


def print_status(state: dict) -> None:
    remaining = max(0, state["max_tries"] - state["wrong_guesses"])
    print(f"Display: {render_display(state)}")
    print(f"Letters guessed: {', '.join(sorted(state['guessed']))}")
    print(f"You have {remaining} attempts left.")


def print_result(state: dict) -> None:
    print("\n--- Game Over ---")

    if is_won(state):
        print("🎉 Congratulations! You won!")
    elif is_lost(state):
        print("😢 You lost. Better luck next time!")
    else:
        print("Game ended unexpectedly.")

    print("\nSummary:")
    print(f"Secret word: {state['secret']}")
    print(f"Final display: {render_display(state)}")
    print(render_summary(state))
    remaining = max(0, state["max_tries"] - state["wrong_guesses"])
    print(f"Remaining attempts: {remaining}")

