import json


class PhoneBook:
    def __init__(self, path: str = 'phones.json'):
        self.contact: dict = {}
        self.path = path


    def get(self, index: int | None = None):
        if index:
            return self.contact.get(index)
        return self.contact


    def open_file(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                self.contact = json.load(file)
            return True
        except:
            return False


    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.contact, file, ensure_ascii=False)
            return True
        except:
            return False


    def search(self, word: str) -> dict[int:dict[str, str]]:
        result = {}
        for index, contact in self.contact.items():
            if word.lower() in ' '.join(contact.values()).lower():
                result[index] = contact
        return result


    def check_id(self):
        if self.contact:
            return max(list(map(int, self.contact))) + 1
        return 1


    def add_contact(self, new: dict[str, str]):
        contact = {self.check_id(): new}
        self.contact.update(contact)


    def edit_contact(self, index, new: dict[str, str]):
         tmp = new
         for key in tmp:
             if new[key] != '':
                 self.contact[index][key] = new[key]


    def remove_contact(self, index):
        del_cnt = self.contact.pop(str(index))
        return del_cnt['name']
