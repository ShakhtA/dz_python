import text
import view
import model


view.menu()
def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                if result:
                    view.show_contacts(result, text.empty_search(word))
                    index = view.input_id_contact()
                    new = view.edit_contact()
                    model.edit_contact(index, new)
                    view.print_message(text.change_successful(new.get('name')))
            case 7:
                word = view.search_word()
                result = model.search(word)
                if result:
                    view.show_contacts(result, text.empty_search(word))
                    index = view.input_id_contact()
                    del_name = model.remove_contact(index)
                    view.print_message(text.del_successful(del_name))
            case 8:
                break