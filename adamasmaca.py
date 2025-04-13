import random

kelimeler = ["elma", "armut", "portakal", "göktuğ", "tuğberk", "muz"]

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/| ",
        "/  "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\"),
}

def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(f"Doğru kelime: {answer}")

def main():
    answer = random.choice(kelimeler).lower()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Tahmin et: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Tek harf gir!")
            continue

        if guess in guessed_letters:
            print("Zaten bu harfi söyledin!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Yanlış tahmin! {guess}")

        if "_" not in hint:
            display_hint(hint)
            print("Tebrikler! Doğru kelimeyi buldun!")
            is_running = False

        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Maalesef kaybettin!")
            is_running = False

if __name__ == "__main__":
    main()
