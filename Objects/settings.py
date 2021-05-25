class Settings:


    def __init__(self, theme):
        self.theme = theme

    def reset(self):
        self.theme = "default"

    def change_theme(self, new_theme):
        self.theme = new_theme