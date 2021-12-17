from os import system
from random import randint


word_dictionary = open('words.txt', 'r').read().split()
word = list(word_dictionary[randint(0, len(word_dictionary) - 1)])
word_field = list(('_ ' * len(word)).strip())
body_array = ['O', '/', '|', '\\', '/', '\\']
body_display = ['', '', '', '', '', '']
attempts = 0


def clear_screen():
    system('cmd /c "cls"')


def reset_word():
    global word, word_field, body_display, attempts
    word = list(word_dictionary[randint(0, len(word_dictionary) - 1)])
    word_field = list(('_ ' * len(word)).strip())
    body_display = ['', '', '', '', '', '']
    attempts = 0


def list_to_string(list):
    converted_list = ''
    for i in range(0, len(list)):
        converted_list += list[i]
    return converted_list


def read_letter():
    chosen_letter = input('Escolha uma letra: ')
    if len(chosen_letter) > 1:
        draw()
        print('Escolha apenas uma letra!')
        return read_letter()
    return chosen_letter


def verify_letter(chosen_letter):
    global word, word_field, attempts

    occurrences = word.count(chosen_letter)

    if occurrences == 0:
        body_display[attempts] = body_array[attempts]
        attempts += 1
        return

    occurrence_index = 0

    for i in range(0, occurrences):
        occurrence_index = word.index(chosen_letter, occurrence_index)
        word_field[occurrence_index * 2] = chosen_letter
        occurrence_index += 1


def loop():
    while True:
        draw()
        verify_letter(read_letter())
        if attempts == 6:
            draw()
            print('Você perdeu o jogo!')
            print('A palavra era ' + list_to_string(word))
            break
        if list_to_string(word_field).replace(' ', '') == list_to_string(word):
            draw()
            print('Parabéns! Você ganhou!')
            break


def draw():
    clear_screen()
    print(
        f"{'-' * 20} Jogo da Forca {'-' * 20}\n{'_' * 11}\n|{' ' * 9}|\n|{' ' * 9}{body_display[0]}\n|{' ' * 8}{body_display[1]}{body_display[2]}{body_display[3]}\n|{' ' * 8}{body_display[4]} {body_display[5]}\n|{'_' * 5}\n\n\n{' ' * 14}{list_to_string(word_field)}\n")


def run():
    loop()
    if input('Deseja jogar novamente? (s ou n)\n->') == 's':
        reset_word()
        run()


run()
