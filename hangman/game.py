from hangman.words import  choose_secret_word
from data.data import english_words

def init_state(secret: str, max_tries: int) -> dict:
    state = {
        "secret": secret,
        "display": list('_' * len(secret) ),
        "guessed": set(),
        "wrong_guesses": 0,
        "max_tries": max_tries
    }
    return state

def validate_guess(ch: str, state :dict ) -> tuple[bool, str]:
    if len(ch) == 1 and ch.isalpha():
        if ch not in state['guessed']:
            return True ,'Good job !'
        else:
            return False ,"Letter already found!"
    else:
        return False , 'You may choose just one letter'


def apply_guess(state: dict, ch: str) -> bool :
    state['guessed'].add(ch)
    if ch in state["secret"]:
        for i, letter in enumerate(state['secret']):
            if letter == ch :
                state["display"][i] = ch

        return True
    else:
        state["wrong_guesses"] += 1
        return False

def is_won(state: dict) -> bool:
    return set(state['secret']).issubset(state['guessed'])

def is_lost(state: dict) -> bool:
    return state["wrong_guesses"] > state["max_tries"]


def render_display(state: dict) -> str:
    return ' '.join(state['display'])


def render_summary(state: dict) -> str:
    return (
        f"Word : {state['secret']}\n"
        f"Guessed letters : {', '.join(sorted(state['guessed']))}\n")




