# coding: utf-8


def say_hello(dog, *args):
    for client in args:
        print '{dog} say hello to {client}'.format(dog=dog, client=client)


say_hello('Ennly', 'lilei', 'hanmei')
say_hello('beira', 'friday', 'thursday', 'wednesday')
