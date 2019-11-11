class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print('wassup')

new_guy = Person('duncan', 20)

print(new_guy.name)
new_guy.greeting()