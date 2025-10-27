from hangman.game import init_state,validate_guess,apply_guess,is_won,is_lost
from hangman.words import choose_secret_word
from data.data import english_words
from hangman.io import prompt_guess,print_status,print_result


def play(words: list[str], max_tries: int = 6):
    secret_word = choose_secret_word(words)
    state = init_state(secret_word, max_tries)

    while not is_won(state) and not is_lost(state):
        ch = prompt_guess()
        is_valid, message = validate_guess(ch, state)
        print(message)
        if not is_valid:
            continue
        apply_guess(state, ch)
        print_status(state)

    print_result(state)
play(english_words,6)
