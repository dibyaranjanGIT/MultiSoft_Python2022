word = 'geeks for geeks'

# print(word.find('for'))
#
# print(word.index('for'))

print(word.count('e'))

new_word = word.replace('geeks', 'dk')
print(new_word)


class Car:
    def __init__(self, type):
        self.type = type

    def change_gear():
        print('Car change 7 gear')

car = Car('Sedan')
car.change_gear()
