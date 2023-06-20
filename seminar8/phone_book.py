phone_book = {}
path: str = 'phone.txt'


def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu) 
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода, введите ЧИСЛО от 1 до 8')


def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = ({'name': nc[1], 'phone': nc[2], 'comment': nc[3]})
    print('\nТелефонная книга успешно загружена!')
    

def save_file():
    data = []
    for i, contact in phone_book.items():
            new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
            data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding="UTF-8") as file:
        file.write(data)
    print("\nТелефонная книга успешно сохранена!")
    print('=' * 200 + '\n')

def show_contacts(book: dict[int, dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + "\n")

def add_contact():
    uid = max(list(phone_book.keys()))+1
    name = input("Введите имя контакта: ")
    phone = input("Введите телефон контакта: ")
    comment = input("Введите комментарий к контакту: ")
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}
    print(f'\nКонтакт {name} успешно добавлен в книгу!')
    print('=' * 200 + '\n')


def search():
    result = {}
    word = input('Введите слово, по которому будет осуществляться поиск: ')
    exist = False
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            exist = True
            result[i] = contact
    if not exist:
        print('=' * 200)
        print ('Контакт не найден')
        print('=' * 200)
    return result


def edit_contact():
    result = search()
    if result:
        show_contacts(result)
        index = int(input("Введите ID контакта, который хотите редактировать: "))
        print('Введите новые данные. Если менять поле не требуется - нажмите ENTER')
        name = input("Введите новое имя: ")
        if name:
            phone_book[index]['name'] = name
        else:
            print("Имя не изменено")
        phone = input("Введите новый телефон: ")
        if phone:
            phone_book[index][phone] = phone
        else:
            print("Телефон не изменен")
        comment = input("Введите новый комментарий: ")
        if comment:
            phone_book[index]['comment'] = comment
        else:
            print("Комментарий не изменен")
        print('\nКонтакт успешно сохранен')
        print('=' * 200 + '\n')


def remove():
    result = search()
    if result:
        show_contacts(result)
        index = int(input("Введите ID контакта, который хотим удалить: "))
        del_cnt = phone_book.pop(index)
        print(f'\nКонтакт {del_cnt.get("name")} успешно удален из книги!')
        print('=' * 200 + '\n')



open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            if result:
                show_contacts(result)
        case 6:
            edit_contact()
        case 7:
            remove()
        case 8:
            print("До свидания! До новых встреч!")
            break


