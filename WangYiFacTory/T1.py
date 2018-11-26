class Pizza():
    def __init__(self,builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        extra_cheeese = 'yes' if self.extra_cheese else 'no'
        info = ('garlic:{}'.format(garlic),'extra_cheese:{}'.format(extra_cheeese))
        return '\n'.join(info)

    class PizzaBuilder:
        def __init__(self):
            self.garlic = False
            self.extra_cheese = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)
if __name__ == '__main__':
    pizza = Pizza.PizzaBuilder().add_extra_cheese().add_garlic().build()
    print(pizza)
