class test():
    name = 'xiaohua'
    def run(self):
        return "HelloWord"

t = test()
print(hasattr(t,'name'))

print(hasattr(t,"run"))
