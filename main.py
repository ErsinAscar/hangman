# Для импорта
import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

os.system('clear')


def clear():
    os.system('clear')


print(logo)
# Для цикла

game_is_finished = False
lives = len(stages) - 1
# Выбирает рандом слово,из листа
chosen_word = random.choice(word_list)
# Считает сколько цифр в слове
word_length = len(chosen_word)

display = []
# печатает сколько "_" находиться в слове
for _ in range(word_length):
    display += "_"
# Цикл
while not game_is_finished:
    guess = input("Выбери букву ").lower()

    # Функция очищает консоль
    clear()

    if guess in display:
        print(f"Вы выбрали {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"Ты выбрал {guess}, неправильный выбор. Выбери другую букву.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Ты проиграл.")
    # Цикл закончен если
    if not "_" in display:
        game_is_finished = True
        print("Ты выиграл.")

    print(stages[lives])
