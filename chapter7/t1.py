'''
    设计模式-享元模式
    享元模式（Flyweight Pattern):运用共享技术有效地支持大量细粒度的对象
    对一个类进行的实例，只在第一次使用时建立，其他时候是用同一个实例，减少内存的开销
'''
#抽象网站类
class Website(object):

    def user(self):
        pass

#具体网站类
class ConcreteWebsite(Website):

    def __init__(self,name):
        self.name = name

    def use(self):
        print('网站分类',self.name)

#不共享的网站类
class UnshareConcreteWebsite(Website):
    def __init__(self,name):
        self.name = name

    def use(self):
        print('不共享网站分类',self.name)


#网站工厂
class WebsiteFactory(object):

    def __init__(self):
        self.hashtable = dict()

    #获取网站类，如果存在直接返回，如果不存在建好之后返回

    def get_website(self,key):
        if not key in self.hashtable:
            self.hashtable[key] = ConcreteWebsite(key)
        return self.hashtable[key]

    #网站实例的个数
    def get_website_count(self):
        return len(self.hashtable.keys())

if __name__ == '__main__':
    factory = WebsiteFactory()
    f1 = factory.get_website("blog")
    f2 = factory.get_website('blog')
    f3 = factory.get_website('blog')
    f4 = factory.get_website('webstie')
    f5 = factory.get_website('webstie')
    f6 = factory.get_website('webstie')
    f7 = UnshareConcreteWebsite('test')

    f1.use()
    f2.use()
    f3.use()
    f4.use()
    f5.use()
    f6.use()
    f7.use()
    print(factory.get_website_count())

