from external import Synthesizer, Human


class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def e(self):
        return 'executes a program'


class Adapter:

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(e=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(e=human.speak)))

    print()
    for i in objects:
        print('8888888888888888888888888888888')
        print(i.e())
        print('================================')
        print('{}----------------- {}'.format(str(i), i.e()))

if __name__ == "__main__":
    main()
