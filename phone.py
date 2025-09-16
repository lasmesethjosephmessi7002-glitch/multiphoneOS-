# phone.py
class Phone:
    def __init__(self, name, apps):
        self.name = name
        self.apps = apps

    def get_info(self):
        return f"{self.name} with apps: {', '.join(self.apps)}"