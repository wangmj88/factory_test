class TypeB(object):
    def __init__(self):
        print('TypeB')

class TypeA(object):
    def __init__(self):
        print('TypeA')

class AbstractFactory(object):
    def __init__(self):
        super().__init__()
        self.type_a = TypeA
        self.type_b = TypeB

    def get_instance_type_a(self):
        return self.type_a()

    def get_instance_type_b(self):
        return self.type_b()
def main():
    abstract_factory = AbstractFactory()
    product_a = abstract_factory.get_instance_type_a()
    product_b = abstract_factory.get_instance_type_b()
if __name__ == '__main__':
    main()
