from os import system
system("cls")

def create_file(filename):  # используется когда файл не создан
    with open(filename, "w") as data:
        data.write("0,max_id\n")
        data.write("id,last_name,name,second_name,phone_number")

def read_file(filename):  # превращает файл в набор листов и возвращает лист
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def show_all_items(filename):  # выводит в консоль список
    data_array = read_file(filename)
    for i in range(2, len(data_array)):
        print(f"ID: {data_array[i][0]} | Фамилия: {data_array[i][1]} | Имя: {data_array[i][2]} | Отчество: {data_array[i][3]} | Телефон: {data_array[i][4]}")

def write_file(filename, data_array):  # перезаписывает список, не используется сам по себе
    with open(filename, 'w') as data:
        for line in data_array:
            write_element = ','.join(line)
            data.write(f'{write_element}\n')

def add_item(filename, last_name = "", name = "", second_name = "", number = ""):  # добавляет элементы в список
    data_array = read_file(filename)
    last_name = input('Фамилия: ')
    name = input('Имя: ')
    second_name = input('Отчество: ')
    number = input('Телефон: ')
    next_id = int(data_array[0][0]) + 1
    new_item = [str(next_id), last_name, name, second_name, number]
    data_array[0][0] = str(next_id)  # перезаписали максимальный индекс
    data_array.append(new_item)
    write_file(filename, data_array)

    show_all_items(filename)

def find_item(filename):
    new_array = read_file(filename)
    print("1 - поиск по ID")
    print("2 - поиск по Фамилии")
    print("3 - поиск по Имени")
    print("4 - поиск по Отчеству")
    print("5 - поиск по Телефону")
    print("вы можете ввести несколько цифр одновременно для комбинированного поиска")
    search_option = input("Формат поиска: ")

    if "1" in search_option:  # поиск по ID
        id = input("введите ID: ")
        temp_array = []
        for i in range(2, len(new_array)):
            if new_array[i][0] == id:
                temp_array.append(new_array[i])
        new_array = temp_array

    if "2" in search_option:  # поиск по фамилии
        last_name = input("введите фамилию: ")
        temp_array = []
        for i in range(2, len(new_array)):
            if new_array[i][1] == last_name:
                temp_array.append(new_array[i])
        new_array = temp_array

    if "3" in search_option:  # поиск по имени
        name = input("введите имя: ")
        temp_array = []
        for i in range(2, len(new_array)):
            if new_array[i][2] == name:
                temp_array.append(new_array[i])
        new_array = temp_array

    if "4" in search_option:  # поиск по отчеству
        second_name = input("введите отчество: ")
        temp_array = []
        for i in range(2, len(new_array)):
            if new_array[i][1] == second_name:
                temp_array.append(new_array[i])
        new_array = temp_array

    if "5" in search_option:  # поиск по телефону
        number = input("введите телефон: ")
        temp_array = []
        for i in range(2, len(new_array)):
            if new_array[i][1] == number:
                temp_array.append(new_array[i])
        new_array = temp_array
    
    if len(new_array) == 0:
        print("Пользователь не найден")
        return

    if len(new_array) > 1:
        print("уточните пользователя")
        for i in range(len(new_array)): 
            print(f"ID: {new_array[i][0]} | Фамилия: {new_array[i][1]} | Имя: {new_array[i][2]} | Отчество: {new_array[i][3]} | Телефон: {new_array[i][4]}")
        id = input("Введите ID: ")
        for line in new_array:
            if line[0] == id:
                new_array = [line]
                print(f"ID: {new_array[0][0]} | Фамилия: {new_array[0][1]} | Имя: {new_array[0][2]} | Отчество: {new_array[0][3]} | Телефон: {new_array[0][4]}")
    else:
        print(f"ID: {new_array[0][0]} | Фамилия: {new_array[0][1]} | Имя: {new_array[0][2]} | Отчество: {new_array[0][3]} | Телефон: {new_array[0][4]}")

    return new_array

def edit_item(filename, last_name = "", name = "", second_name = "", number = ""):
    new_array = find_item(filename)
    if type(new_array) != list:   # выключаем если не нашли пользователя
        return
    last_name = input('Фамилия: ')
    name = input('Имя: ')
    second_name = input('Отчество: ')
    number = input('Телефон: ')
    replace_item = [new_array[0][0], last_name, name, second_name, number]

    data_array = read_file(filename)  # перезаписываем
    for i in range(2, len(data_array)):
        if data_array[i][0] == replace_item[0]:
            data_array[i] = replace_item
            write_file(filename, data_array)
            print("запись успешно изменена")
            return  # чтобы дальше не щелкать список

def del_item(filename):
    new_array = find_item(filename)
    if type(new_array) != list:   # выключаем если не нашли пользователя
        return
    data_array = read_file(filename)
    for i in range(2, len(data_array)):
        if data_array[i][0] == new_array[0][0]:
            del data_array[i]
            write_file(filename, data_array)
            print("Запись успешно удалена")
            return
    

def menu():
    try:
        open("file.txt", "r")
        print("файл найден")
    except:
        print("файл не найден, создаем пустой шаблон")
        create_file(filename)
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')

    user_operation = int(input())
    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        edit_item(filename)
    elif user_operation == 4:
        del_item(filename)

filename = "file.txt"
menu()