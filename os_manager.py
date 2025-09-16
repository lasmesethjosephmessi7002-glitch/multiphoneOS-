# os_manager.py
class OSManager:
    def __init__(self):
        self.phones = []
        self.current = None

    def add_phone(self, phone):
        self.phones.append(phone)
        if self.current is None:
            self.current = phone

    def switch_phone(self, index):
        if 0 <= index < len(self.phones):
            self.current = self.phones[index]
            return f"Switched to {self.current.name}"
        return "Invalid phone index"