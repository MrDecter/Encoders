import time

"""
-Добавить отработку ошибок
-Проблема с большим кол-ом букв
"""


def morze(all_word):
    """Функция преобразования текста в морзе"""
    list_morze = []
    z = 0
    while z < len(all_word):
        if all_word[z] == "A":
            list_morze.append(" *- ")
            z += 1
        elif all_word[z] == "Б":
            list_morze.append(" -*** ")
            z += 1
        elif all_word[z] == "В":
            list_morze.append(" *-- ")
            z += 1
        elif all_word[z] == "Г":
            list_morze.append(" --* ")
            z += 1
        elif all_word[z] == "Д":
            list_morze.append(" -** ")
            z += 1
        elif all_word[z] == "Е":
            list_morze.append(" * ")
            z += 1
        elif all_word[z] == "Ж":
            list_morze.append(" ***- ")
            z += 1
        elif all_word[z] == "З":
            list_morze.append(" --** ")
            z += 1
        elif all_word[z] == "И":
            list_morze.append(" ** ")
            z += 1
        elif all_word[z] == "Й":
            list_morze.append(" *--- ")
            z += 1
        elif all_word[z] == "К":
            list_morze.append(" -*- ")
            z += 1
        elif all_word[z] == "Л":
            list_morze.append(" *-** ")
            z += 1
        elif all_word[z] == "М":
            list_morze.append(" -- ")
            z += 1
        elif all_word[z] == "Н":
            list_morze.append(" -* ")
            z += 1
        elif all_word[z] == "О":
            list_morze.append(" --- ")
            z += 1
        elif all_word[z] == "П":
            list_morze.append(" *--* ")
            z += 1
        elif all_word[z] == "Р":
            list_morze.append(" *-* ")
            z += 1
        elif all_word[z] == "С":
            list_morze.append(" *** ")
            z += 1
        elif all_word[z] == "Т":
            list_morze.append(" - ")
            z += 1
        elif all_word[z] == "У":
            list_morze.append(" **- ")
            z += 1
        elif all_word[z] == "Ф":
            list_morze.append(" **-* ")
            z += 1
        elif all_word[z] == "Х":
            list_morze.append(" **** ")
            z += 1
        elif all_word[z] == "Ц":
            list_morze.append(" -*-* ")
            z += 1
        elif all_word[z] == "Ч":
            list_morze.append(" ---* ")
            z += 1
        elif all_word[z] == "Ш":
            list_morze.append(" ---- ")
            z += 1
        elif all_word[z] == "Щ":
            list_morze.append(" --*- ")
            z += 1
        elif all_word[z] == "Ы":
            list_morze.append(" -*-- ")
            z += 1
        elif all_word[z] == "Э":
            list_morze.append(" **-** ")
            z += 1
        elif all_word[z] == "Ю":
            list_morze.append(" **-- ")
            z += 1
        elif all_word[z] == "Я":
            list_morze.append(" *-*- ")
            z += 1
        elif all_word[z] == " ":
            list_morze.append("   ")
            z += 1
    post_list = "".join(list_morze)
    return post_list


def menu():
    manager = int(input("1.Код морзе\n"))
    if manager == 1:
        words = list(input("Введите текст для кодирования: ").upper())
        print(morze(words))
        time.sleep(2)
        menu()


print("\"Шифратор-Дешифратор\" \n From: Decter")
time.sleep(2)
menu()
