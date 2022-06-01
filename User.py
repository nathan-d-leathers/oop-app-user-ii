class User:
    def __init__(self, name, email_address, phone_number, age):
        self.name = name
        self.email_address = email_address
        self.phone_number = str(phone_number)
        self.age = age

    def name_upper(self):
        return self.name.upper()
    
    def age_in_human_years(self):
        return f"My name is {self.name}, and I'm {self.age * 7} years old in human years"

nathan = User("Nathan", "nathan@codeplatoon.org", 1231231230)

evan = User("Evan", "evan@codeplatoon.org", 5027152210)

raphael = User("Raphael", "raphael@codeplatoon.org", 3125551234, 3)

# print(raphael.age_in_human_years())
