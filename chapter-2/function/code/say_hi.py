# coding: utf-8


def say_hi(dog, **kwargs):
    for name, greeting in kwargs.items():
        print '{name} say {greeting} to {dog}'.format(name=name, greeting=greeting, dog=dog)


say_hi('Dachshund', jack='你好', rose='hi', mike='こんにちは')
