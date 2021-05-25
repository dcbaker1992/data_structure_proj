import random
from linked_list import Linked_List


months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December')


def one_part_a(tupil):
    print(tupil[2])


places = {'Tempe', 'Dallas', 'Scottsdale', 'Saudi Arabia', 'Iraq'}
print(places)
places.add('Cabo')
places.update(['San Diego', 'Las Vegas'])


def one_part_b(set):
    for i in set:
        print(i)


contestants = {}


def one_part_c(object):
    object['contestant_uno'] = "Mario"
    object['contestant_dose'] = "Lois"
    object['contestant_tres'] = "Becky G"
    object['contestant_quatro'] = "Karen"
    object['contestant_cinco'] = "Ken"

    print(random.choice(list(object.values())))


madre = {
    'first_name': 'Tammy',
    'last_name': 'Baker',
    'relationship': 'Mother'
}

padre = {
    'first_name': 'Glynn',
    'last_name': 'Gross',
    'relationship': 'Father'
}
hermano = {
    'first_name': 'Jack',
    'last_name': 'Gross',
    'relationship': 'Brother'
}


def two():
    family = []
    family.append(madre)
    family.append(padre)
    family.append(hermano)
    print(family)


if __name__ == '__main__':
    one_part_a(months)
    one_part_b(places)
    one_part_c(contestants)
    two()

    linked_list = Linked_List()
    linked_list.append_node(1)
    linked_list.append_node(2)
    linked_list.append_node(3)
