import random


def choose_word():
    words = ["python", "programacao", "desenvolvimento", "inteligencia", "artificial", "computador"]
    return random.choice(words)


def display_current_progress(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem", len(word), "letras.")

    while attempts > 0:
        print("\nPalavra:", display_current_progress(word, guessed_letters))
        print("Tentativas restantes:", attempts)

        guess = input("Adivinhe uma letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, digite uma única letra.")
            continue

        if guess in guessed_letters:
            print("Você já adivinhou essa letra. Tente outra.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correto!")
        else:
            print("Errado!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nParabéns! Você adivinhou a palavra:", word)
            break
    else:
        print("\nFim de jogo! A palavra era:", word)


def main():
    while True:
        play_hangman()
        play_again = input("\nVocê quer jogar novamente? (s/n): ").lower()
        if play_again != 's':
            print("Obrigado por jogar! Até a próxima!")
            break


if __name__ == "__main__":
    main()
