# register.py

class Register:
    def __init__(self, name):
        self.name = name  # e.g., R0, R1, etc.
        self.value = 0    # default value is 0

    def set(self, new_value):
        self.value = new_value

    def get(self):
        return self.value
