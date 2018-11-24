#encoding=utf8
__author__ = 'jianchao.jjc'
import random
#单例
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
class Multiton(object):
    ins_lst=[]
    max_ins=2
    def __new__(cls, *args, **kw):
        if len(cls.ins_lst)<cls.max_ins:
            orig = super(Multiton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            cls.ins_lst.append(cls._instance)
            return cls._instance
        return cls.ins_lst[random.randint(0,1)]
class singletonExample(Multiton):
    share_value=0
def singleTest():
    a=singletonExample()
    print a.share_value
    b=singletonExample()
    b.share_value=2
    print a.share_value
    c=singletonExample()
    c.share_value=1
    print a.share_value
#工厂
class Factory:
    def createFruit(self,fruit):
        if fruit=="apple":
            return Apple()
        elif fruit=="banana":
            return Banana()
        else:
            return Fruit()
class Fruit:
    def __str__(self):
        return "fruit"
class  Apple(Fruit):
    def __str__(self):
        return "apple"
class Banana(Fruit):
    def __str__(self):
        return "banana"
def factoryTest():
    factory=Factory()
    print factory.createFruit("apple")
    print factory.createFruit("banana")
#模板
class Car():
    def start(self):
        print "start..."
    def stop(self):
        print "stop..."
    def accelerate(self):
        print "accelerate..."
    def run(self):
        self.start()
        self.accelerate()
        self.stop()
class Truck(Car):
    def start(self):
        print "truck start..."
    def stop(self):
        print "truck stop..."
    def accelerate(self):
        print "truck accelerate..."
def templateTest():
    myCar=Truck()
    myCar.run()
#建造者模式
class PersonBuilder():
    def BuildHead(self):
        pass
    def BuildBody(self):
        pass
    def BuildArm(self):
        pass
    def BuildLeg(self):
        pass
class PersonFatBuilder(PersonBuilder):
    type = 'Fat'
    def BuildHead(self):
        print 'Building %s Head' % self.type
    def BuildBody(self):
        print 'Building %s Body' % self.type
    def BuildArm(self):
        print 'Building %s Arm' % self.type
    def BuildLeg(self):
        print 'Building %s Leg' % self.type
class PersonThinBuilder(PersonBuilder):
    type = 'Thin'
    def BuildHead(self):
        print 'Building %s Head' % self.type
    def BuildBody(self):
        print 'Building %s Body' % self.type
    def BuildArm(self):
        print 'Building %s Arm' % self.type
    def BuildLeg(self):
        print 'Building %s Leg' % self.type
class PersonDirector():
    pb = None
    def __init__(self, pb):
        self.pb = pb
    def CreatePerson(self):
        self.pb.BuildHead()
        self.pb.BuildBody()
        self.pb.BuildArm()
        self.pb.BuildLeg()
def builderTest():
    pb = PersonThinBuilder()
    pd = PersonDirector(pb)
    pd.CreatePerson()

    pb = PersonFatBuilder()
    pd = PersonDirector(pb)
    pd.CreatePerson()
#代理模式
import time
class Manager(object):
    def work(self):
        pass

    def talk(self):
        pass

class SalesManager(Manager):
    def work(self):
        print"Sales Manager working..."

    def talk(self):
        print"Sales Manager ready to talk"

class Proxy(Manager):
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def work(self):
        print"Proxy checking for Sales Manager availability"
        if self.busy == 'Yes':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print"Sales Manager is busy"
def proxyTest():
    p = Proxy()
    p.work()
#原型模式
from copy import copy, deepcopy
class test_obj:
    def __init__(self, id):
        self.id = id
class proto_type:
    def __init__(self, name, id):
        self.name = name
        self.obj = test_obj(id)
    def display(self):
        print self.name
        print self.obj.id
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)
def protoTest():
    obj1 = proto_type('name1', 1)
    obj2 = obj1.clone()
    obj3 = obj1.deep_clone()
    obj2.name = 'name2'
    obj2.obj.id = 2
    obj3.name = 'name3'
    obj3.obj.id = 3
    obj1.display()
    obj2.display()
    obj3.display()
    print obj1.__class__
    print obj2.__class__
    print obj3.__class__
#中介者模式
def printInfo(info):
    print unicode(info, 'utf-8').encode('gbk')
class Mediator():
    def Send(self, message, colleague):
        pass
class Colleague():
    mediator = None
    def __init__(self,mediator):
        self.mediator = mediator
class ConcreteColleague(Colleague):
    name = ''
    def __init__(self, name, mediator):
        self.name = name
        Colleague.__init__(self,mediator)
    def Send(self,message):
        self.mediator.Send(message, self)
    def Notify(self,message):
        printInfo('%s get infos：%s' % (self.name, message))
class ConcreteMediator(Mediator):
    name = ''
    colleague1 = None
    colleague2 = None
    def __init__(self, name):
        self.name = name
    def Send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.Notify(message)
        else:
            self.colleague1.Notify(message)
def mediatorTest():
    mediator = ConcreteMediator('UN')
    USA = ConcreteColleague('U.S.A',mediator)
    mediator.colleague1 = USA
    Iraq = ConcreteColleague('IRAQ',mediator)
    mediator.colleague2 = Iraq

    USA.Send('Nuclear Or War!')
    Iraq.Send('No Nuclear and no afraid!')
    return
#命令模式
def printInfo(info):
    print unicode(info, 'utf-8').encode('gbk')

import time
class Command():
    receiver = None
    def __init__(self, receiver):
        self.receiver = receiver
    def Execute(self):
        pass
class BakeMuttonCommand(Command):
    def SetHandsetSoft(self, receiver):
        Command.__init__(self,receiver)
    def Execute(self):
        self.receiver.BakeMutton()
    def ToString(self):
        return 'Mutton...'
class BakeChickenWingCommand(Command):
    def SetHandsetSoft(self, receiver):
        Command.__init__(self,receiver)
    def Execute(self):
        self.receiver.BakeChickenWing()
    def ToString(self):
        return 'Chicken Wings...'
class Barbecuer():
    def BakeChickenWing(self):
        printInfo('Baking Chicken Wings!')
    def BakeMutton(self):
        printInfo('Baking Mutton！')
class Waiter():
    commandList = []
    def SetOrder(self,command):
        printInfo('%s add order：%s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),command.ToString()))
        self.commandList.append(command)

    def CancelOrder(self,command):
        printInfo('%s delete order：%s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),command.ToString()))
        self.commandList.remove(command)

    def Notify(self):
        printInfo('\nNotify：')
        for command in self.commandList:
            command.Execute()
    def Run(self):
        printInfo('Contact')

def cmdTest():
    boy = Barbecuer()
    bakeMuttonCommand1 = BakeMuttonCommand(boy)
    bakeMuttonCommand2 = BakeMuttonCommand(boy)
    bakeChickenWingCommand1 = BakeChickenWingCommand(boy)
    girl = Waiter()

    girl.SetOrder(bakeMuttonCommand1)
    girl.SetOrder(bakeMuttonCommand2)
    girl.SetOrder(bakeChickenWingCommand1)
    girl.CancelOrder(bakeMuttonCommand1)
    girl.Notify()
#责任链模式
class Manager():
    successor = None
    name = ''
    def __init__(self, name):
        self.name = name
    def SetSuccessor(self, successor):
        self.successor = successor
    def HandleRequest(self, request):
        pass
class CommonManager(Manager):
    def HandleRequest(self, request):
        if request.RequestType == 'DaysOff' and request.Number <= 2:
            printInfo('%s:%s Num:%d Accepted' % (self.name, request.RequestContent, request.Number))
        else:
            if self.successor != None:
                self.successor.HandleRequest(request)
class Majordomo(Manager):
    def HandleRequest(self, request):
        if request.RequestType == 'DaysOff' and request.Number <= 5:
            printInfo('%s:%s num:%d Accepted' % (self.name, request.RequestContent, request.Number))
        else:
            if self.successor != None:
                self.successor.HandleRequest(request)
class GeneralManager(Manager):
    def HandleRequest(self, request):
        if request.RequestType == 'DaysOff':
            printInfo('%s:%s num:%d Accepted' % (self.name, request.RequestContent, request.Number))
        elif request.RequestType == 'PayRise' and request.Number <= 500:
            printInfo('%s:%s num:%d Accepted' % (self.name, request.RequestContent, request.Number))
        elif request.RequestType == 'PayRise' and request.Number > 500:
            printInfo('%s:%s num:%d Delay' % (self.name, request.RequestContent, request.Number))
class Request():
    RequestType = ''
    RequestContent = ''
    Number = 0
def dutyChainTest():
    jinLi = CommonManager('JINLI')
    zongJian = Majordomo('ZONGJIAN')
    zhongJingLi = GeneralManager('ZHONGJINGLI')

    jinLi.SetSuccessor(zongJian)
    zongJian.SetSuccessor(zhongJingLi)

    request = Request()
    request.RequestType = 'DaysOff'
    request.RequestContent = 'Ask a day off'
    request.Number = 1
    jinLi.HandleRequest(request)

    request.RequestType = 'DaysOff'
    request.RequestContent = 'Ask 5 days off'
    request.Number = 5
    jinLi.HandleRequest(request)

    request.RequestType = 'PayRise'
    request.RequestContent = 'Ask for 500 yuan pay rise'
    request.Number = 500
    jinLi.HandleRequest(request)

    request.RequestType = 'PayRise'
    request.RequestContent = 'Ask for 1000 yuan pay rise'
    request.Number = 1000
    jinLi.HandleRequest(request)
#装饰模式
class Beverage:
    description = "Unknown Beverage"

    def get_description(self):
        return self.description

    def cost(self):
        pass


class CondimentDecorator(Beverage):
    def get_description(self):
        pass


class MilkyTea(Beverage):
    def __init__(self):
        self.description = "MilkyTea"

    def cost(self):
        return 1.99


class FruitJuice(Beverage):
    def __init__(self):
        self.description = "FruitJuice"

    def cost(self):
        return 1.80


class Coffee(Beverage):
    def __init__(self):
        self.description = "Coffee"

    def cost(self):
        return 2.00


class Pearl(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " + Pearl"

    def cost(self):
        return 1.50 + self.beverage.cost()


class Pudding(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " + Pudding"

    def cost(self):
        return 1.60 + self.beverage.cost()


class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " + Milk"

    def cost(self):
        return 2.10 + self.beverage.cost()
def decorateTest():
    b = FruitJuice()
    print "%s = $%s\n" % (b.get_description(), b.cost())

    b = MilkyTea()
    b = Pearl(b)
    b = Pudding(b)
    print "%s = $%s\n" % (b.get_description(), b.cost())

    b = Coffee()
    b = Pearl(b)
    b = Milk(b)
    print "%s = $%s\n" % (b.get_description(), b.cost())
#策略模式
class Duck:
    def display(self):
        pass

    def setFlyBehavior(self,fb):
        self.flyBehavior = fb

    def setQuackBehavior(self,qb):
        self.quackBehavior = qb

    def performQuack(self):
        self.quackBehavior.quack()

    def performFly(self):
        self.flyBehavior.fly()




class FlyBehavior:
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print "Fly with wings."

class FlyNoWay(FlyBehavior):
    def fly(self):
        print "Fly no way."



class QuackBehavior:
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print "gua gua"

class Squeak(QuackBehavior):
    def quack(self):
        print "zhi zhi"

class MuteQuack(QuackBehavior):
    def quack(self):
        print "nothing"



class MallardDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Squeak())

    def display(self):
        print "MallardDuck"

class RedheadDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Quack())

    def display(self):
        print "RedheadDuck"

class RubberDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(MuteQuack())

    def display(self):
        print "RubberDuck"

class DecoyDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(MuteQuack())

    def display(self):
        print "DecoyDuck"
def strategyTest():
    for n in MallardDuck(),RedheadDuck(),RubberDuck(),DecoyDuck():
        n.display()
        n.performFly()
        n.performQuack()
        print ""
    n.setFlyBehavior(FlyNoWay())
    n.setQuackBehavior(Quack())
    n.display()
    n.performFly()
    n.performQuack()
#适配器模式
class Player():
    name = ''
    def __init__(self,name):
        self.name = name
    def Attack(self,name):
        pass
    def Defense(self):
        pass
class Forwards(Player):
    def __init__(self,name):
        Player.__init__(self,name)
    def Attack(self):
        printInfo("Forward %s Attack!" % self.name)
    def Defense(self,name):
        printInfo("Forward %s Defend!" % self.name)
class Center(Player):
   def __init__(self,name):
       Player.__init__(self,name)
   def Attack(self):
       printInfo("Center %s Attack!" % self.name)
   def Defense(self):
       printInfo("Center %s Defend!" % self.name)
class Guards(Player):
   def __init__(self,name):
       Player.__init__(self,name)
   def Attack(self):
       printInfo("Guards %s Attack!" % self.name)
   def Defense(self):
       printInfo("Guards %s Defend!" % self.name)
class ForeignCenter(Player):
    name = ''
    def __init__(self,name):
        Player.__init__(self,name)
    def ForeignAttack(self):
        printInfo("Foreign Center %s Attack!" % self.name)
    def ForeignDefense(self):
        printInfo("Foreign Center %s Defend!" % self.name)

class Translator(Player):
    foreignCenter = None
    def __init__(self,name):
        self.foreignCenter = ForeignCenter(name)
    def Attack(self):
        self.foreignCenter.ForeignAttack()
    def Defense(self):
        self.foreignCenter.ForeignDefense()
def adapterTest():
    b = Forwards('Battier')
    m = Guards('McGrady')
    ym = Translator('Yaoming!')

    b.Attack()
    m.Defense()
    ym.Attack()
    ym.Defense()
#备忘录模式
class GameCharacter():
    vitality = 0 #生命力
    attack = 0  #攻击力
    defense = 0 #防御力
    def DisplayState(self):
        printInfo('Current Values:')
        printInfo('\tLife：%d' % self.vitality)
        printInfo('\tAttack：%d' % self.attack)
        printInfo('\tDefence：%d' % self.defense)
    def InitState(self):
        self.vitality = 100
        self.attack = 100
        self.defense = 100
    def Fight(self):
        self.vitality = 0
        self.attack = 0
        self.defense = 0
    def SaveState(self):
        return RoleStateMemento(self.vitality, self.attack, self.defense)
    def RecoveryState(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense
class RoleStateMemento():
    vitality = 0
    attack = 0
    defense = 0
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
class RoleStateCaretaker():
    memento = None
def memoTest():
    id1 = GameCharacter()
    id1.InitState()
    id1.DisplayState()
    stateAdmin = RoleStateCaretaker()
    stateAdmin.memento = id1.SaveState()
    id1.Fight()
    id1.DisplayState()
    id1.RecoveryState(stateAdmin.memento)
    id1.DisplayState()
#迭代器模式
#python list可以认为是迭代器模式的实现，同时，用yield去构造生成器也是不错的方法
class Iterator:
  def First(self):
    pass
  def Next(self):
    pass
  def IsDone(self):
    pass
  def CurrentItem(self):
    pass
class Aggregate:
  def CreateIterator(self):
    pass
class ConcreteIterator(Iterator):
    aggregate = None
    current = 0
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current = 0
    def First(self):
        return self.aggregate[0]
    def Next(self):
        ret = None
        self.current += 1
        if(self.current < len(self.aggregate)):
            ret = self.aggregate[self.current]
        return ret
    def IsDone(self):
        if(self.current < len(self.aggregate)):
            return False
        else:
            return True
    def CurrentItem(self):
        ret = None
        if(self.current < len(self.aggregate)):
            ret = self.aggregate[self.current]
        return ret
class ConcreteAggregate(Aggregate):
    items = None
    def __init__(self):
        self.items = []
def iterTest():
    a = ConcreteAggregate()
    a.items.append('Li')
    a.items.append('Wang')
    a.items.append('Zhang')
    a.items.append('Liu')
    a.items.append('Xu')
    a.items.append('Jia')
    i = ConcreteIterator(a.items)
    item = i.First()
    while(False == i.IsDone()):
        printInfo("%s: Please Buy Tickeds！" % i.CurrentItem());
        i.Next()
#观察者模式
class Informer():
    observers = []
    action = ''
    def Attach(self, observer):
        self.observers.append(observer)
    def Notify(self):
        for o in self.observers:
            o.Update()
class Secretary(Informer):
    observers = []
    action = "The boss is back!"
class Boss(Informer):
    observers = []
    update = [] #更新函数接口列表
    action = "I am back!"
    def AddEventCB(self,eventCB):
        self.update.append(eventCB)
    def Notify(self):
        for o in self.update:
            o()
class Observer():
    name = ''
    nformer = None
    def __init__(self, name, secretary):
        self.name = name
        self.secretary = secretary
    def Update(self):
        pass
class StockObserver(Observer):
    name = ''
    secretary = None
    def __init__(self, name, secretary):
        Observer.__init__(self, name, secretary)
    def Update(self):
        printInfo("%s, %s, give up checking stocking, continue working..." % (self.secretary.action,self.name))

    def CloseStock(self):
        printInfo("%s, %s, give up checking stocking, working..." % (self.secretary.action,self.name))
class NBAObserver(Observer):
    name = ''
    secretary = None
    def __init__(self, name, secretary):
        Observer.__init__(self, name, secretary)
    def Update(self):
        printInfo("%s, %s, give up watching NBA, continue working..." % (self.secretary.action,self.name))

def observerTest():
    secretary = Secretary()
    stockObserver1 = StockObserver('Zhang3',secretary)
    nbaObserver1 = NBAObserver('Wang5',secretary)

    secretary.Attach(stockObserver1)
    secretary.Attach(nbaObserver1)

    secretary.Notify()

    huHanShan = Boss()
    stockObserver2 = StockObserver('Lisi',huHanShan)
    huHanShan.AddEventCB(stockObserver2.CloseStock)
    huHanShan.Notify()
#组合模式
class Company:
    name = ''
    def __init__(self, name):
        self.name = name
    def Add(self, company):
        pass
    def Remove(self, company):
        pass
    def Display(self, depth):
        pass
    def LineOfDuty(self):
        pass

class ConcreteCompany(Company):
    childrenCompany = None
    def __init__(self, name):
        Company.__init__(self,name)
        self.childrenCompany = []
    def Add(self, company):
        self.childrenCompany.append(company)
    def Remove(self, company):
        self.childrenCompany.remove(company)
    def Display(self, depth):
        printInfo('-'*depth + self.name)
        for component in self.childrenCompany:
            component.Display(depth+2)
    def LineOfDuty(self):
        for component in self.childrenCompany:
            component.LineOfDuty()
class HRDepartment(Company):
    def __init__(self, name):
         Company.__init__(self,name)
    def Display(self, depth):
        printInfo('-'*depth + self.name)
    def LineOfDuty(self): #履行职责
        printInfo('%s\t Enrolling management.' % self.name)

class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self,name)
    def Display(self, depth):
        printInfo('-'*depth + self.name)
    def LineOfDuty(self): #履行职责
        printInfo('%s\tFinance Management.' % self.name)

def compositeTest():
    root = ConcreteCompany('Beijing HQ')
    root.Add(HRDepartment('HQ HR'))
    root.Add(FinanceDepartment('HQ Finance'))

    comp = ConcreteCompany('East China Branch')
    comp.Add(HRDepartment('E.C.Br HR'))
    comp.Add(FinanceDepartment('E.C.Br Finance'))
    root.Add(comp)

    comp1 = ConcreteCompany('Nanjing Branch')
    comp1.Add(HRDepartment('Nanjing Branch HR'))
    comp1.Add(FinanceDepartment('Nanjing Branch Finance'))
    comp.Add(comp1)

    comp2 = ConcreteCompany('Hangzhou Branch')
    comp2.Add(HRDepartment('Hangzhou Branch'))
    comp2.Add(FinanceDepartment('Hangzhou Branch'))
    comp.Add(comp2)

    root.Display(1)

    root.LineOfDuty()
#门面模式
class TC1:
    def run(self):
        print "####In Test 1####"
        time.sleep(1)
        print "Setting up"
        time.sleep(1)
        print "Running test"
        time.sleep(1)
        print "Tearing down"
        time.sleep(1)
        print "Test Finished\n"

class TC2:
    def run(self):
        print "#####In Test 2 ######"
        time.sleep(1)
        print "Setting up"
        time.sleep(1)
        print "Running test"
        time.sleep(1)
        print "Tearing down"
        time.sleep(1)
        print "Test Finished\n"

class TC3:
    def run(self):
        print "#####In Test 3 ######"
        time.sleep(1)
        print "Setting up"
        time.sleep(1)
        print "Running test"
        time.sleep(1)
        print "Tearing down"
        time.sleep(1)
        print "Test Finished\n"
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()

    def runAll(self):
        self.tc1.run()
        self.tc2.run()
        self.tc3.run()

def facadeTest():
    testrunner = TestRunner()
    testrunner.runAll()
#访问者模式
class Person():
    def Accept(self, visitor):
        pass
class Man(Person):
    type = 'Man'
    def Accept(self, visitor):
        visitor.GetManConclusion(self)
class Woman(Person):
    type = 'Woman'
    def Accept(self, visitor):
        visitor.GetWomanConclusion(self)
class Action():
    def GetManConclusion(self, person):
        pass
    def GetWomanConclusion(self, person):
        pass

class Success(Action):
    type = 'Succeed'
    def GetManConclusion(self, person):
        printInfo('When %s %s, there is a successful woman' %(person.type, self.type))
    def GetWomanConclusion(self, person):
        printInfo('When %s %s，there is a unsuccessful man' %(person.type, self.type))

class Failing(Action):
    type = 'Failed'
    def GetManConclusion(self, person):
        printInfo('When %s %s，just drink...' %(person.type, self.type))
    def GetWomanConclusion(self, person):
        printInfo('When %s %s，just cry...' %(person.type, self.type))
class Love(Action):
    type = 'Love'
    def GetManConclusion(self, person):
        printInfo('When %s %s，pretend to know all.' %(person.type, self.type))
    def GetWomanConclusion(self, person):
        printInfo('When %s %s，pretend to know nothing.' %(person.type, self.type))
class ObjectStructure:
    elements = []
    def Attach(self, element):
        self.elements.append(element)
    def Detach(self, element):
        self.elements.remove(element)
    def Display(self, visitor):
        for e in self.elements:
            e.Accept(visitor)
def visitorTest():
    o = ObjectStructure()
    o.Attach(Man())
    o.Attach(Woman())

    o.Display(Success())
    o.Display(Failing())
    o.Display(Love())
#享元模式
class WebSite():
    def Use(self):
        pass
class ConcreteWebSite(WebSite):
    name = ''
    def __init__(self,name):
        self.name = name
    def Use(self, user):
        printInfo('Web-Classify：%s User %s' % (self.name,user.name))
class WebSiteFactory():
    WebSites = {}

    def GetWebSiteCategory(self, key):
        if self.WebSites.has_key(key) == False:
            self.WebSites[key] = ConcreteWebSite(key)
        return self.WebSites[key]

    def GetWebSiteCount(self):
        return len(self.WebSites)

class User():
    name = None
    def __init__(self,name):
        self.name = name

def flyweightTest():
    f = WebSiteFactory()

    fx = f.GetWebSiteCategory('Product Show')
    fy = f.GetWebSiteCategory('Product Show')
    fz = f.GetWebSiteCategory('Product Show')
    fx.Use(User('A'))
    fy.Use(User('B'))
    fz.Use(User('C'))

    fx = f.GetWebSiteCategory('Blog')
    fy = f.GetWebSiteCategory('Blog')
    fz = f.GetWebSiteCategory('Blog')
    fx.Use(User('D'))
    fy.Use(User('E'))
    fz.Use(User('F'))

    printInfo('Total-Classify-Number：%d' % f.GetWebSiteCount())
#状态模式
class State():
    def WriteProgram(self):
        pass
class ForenoonState(State):
    def WriteProgram(self,w):
        if (w.Hour < 12):
            printInfo("Current Time：%d Working State：Morning! Go and do!" % w.Hour)
        else:
            w.SetState(noonState())
            w.WriteProgram()

class noonState(State):
    def WriteProgram(self,w):
        if (w.Hour < 13):
            printInfo("Current Time：%d Working State：Noon! Take a nap" % w.Hour)
        else:
            w.SetState(AfternoonState())
            w.WriteProgram()

class AfternoonState(State):
    def WriteProgram(self,w):
        if (w.Hour < 18):
            printInfo("Current Time：%d Working State：Afternoon! Go on!" % w.Hour)
        else:
            w.SetState(EveningState())
            w.WriteProgram();

class EveningState(State):
    def WriteProgram(self,w):
        if(w.TaskFinished):
            w.SetState(RestState())
            w.WriteProgram()
            return
        if (w.Hour < 21):
            printInfo("Current Time：%d Working State：Evening! Tired..." % w.Hour)
        else:
            w.SetState(SleepingState())
            w.WriteProgram();

class SleepingState(State):
    def WriteProgram(self,w):
        printInfo("Current Time：%d Working State：Night! Sleep..." % w.Hour)

class RestState(State):
    def WriteProgram(self,w):
        printInfo("Current Time：%d Working State：Back Home..." % w.Hour)


class Work():
    state = ForenoonState();
    TaskFinished = False
    Hour = 8.0
    def SetState(self, state):
        self.state = state
    def WriteProgram(self):
        self.state.WriteProgram(self)


def stateTest():
    work = Work()
    for i in range(9,23,1):
        work.Hour = i
        if(i > 19):
            work.TaskFinished = True
        work.WriteProgram()
    return

#解释器模式
class PlayContext():
    text = None
    PlayText = None

class Expression():
    def Interpret(self, context):
        if len(context.PlayText) == 0:
            return
        else:
            playKey = context.PlayText[0:1]
            context.PlayText = context.PlayText[2:]
            tmp = context.PlayText.index(' ')
            playValue = context.PlayText[0:tmp]
            context.PlayText = context.PlayText[tmp+1:]
            self.Excute(playKey,playValue)
    def Excute(self,playKey,playValue):
        pass

class Pitch(Expression):
    pitch = None
    def Excute(self, key, value):
        value = int(value)
        if value == 1:
            self.pitch = 'Low'
        elif value == 2:
            self.pitch = 'Middle'
        elif value == 3:
            self.pitch = 'High'
        printInfo(self.pitch)

class Note(Expression):
    Notes = {
    'C':1,
    'D':2,
    'E':3,
    'F':4,
    'G':5,
    'A':6,
    'B':7,
    }
    note = None
    def Excute(self, key, value):
        self.note = self.Notes[key]
        printInfo('%d' % self.note)


def interpreterTest():
    context = PlayContext()
    context.PlayText = "O 2 E 0.5 G 0.5 A 3 E 0.5 G 0.5 D 3 E 0.5 G 0.5 A 0.5 O 3 C 1 O 2 A 0.5 G 1 C 0.5 E 0.5 D 3 "
    expression = None
    while(len(context.PlayText) > 0):
        str = context.PlayText[0:1]
        if(str == 'O'):
            expression = Pitch()
        elif(str == 'C' or str == 'D' or str == 'E' or str == 'F' or str == 'G' or str == 'A' or str == 'B' or str == 'P'):
            expression = Note()
        expression.Interpret(context)
#桥接模式
class HandsetBrand():
    soft = None
    def SetHandsetSoft(self, soft):
        self.soft = soft
    def Run(self):
        pass
class HandsetBrand1(HandsetBrand):
    def Run(self):
        printInfo('HuaWei:')
        self.soft.Run()

class HandsetBrand2(HandsetBrand):
    def Run(self):
        printInfo('Samsung:')
        self.soft.Run()

class HandsetSoft():
    def Run(self):
        pass

class HandsetGame(HandsetSoft):
    def Run(self):
        printInfo('Running Games...')

class HandsetAddressList(HandsetSoft):
    def Run(self):
        printInfo('Running Contact...')

def bridgeTest():
    h1 = HandsetBrand1()
    h1.SetHandsetSoft(HandsetAddressList())
    h1.Run()
    h1.SetHandsetSoft(HandsetGame())
    h1.Run()

    h2 = HandsetBrand2()
    h2.SetHandsetSoft(HandsetAddressList())
    h2.Run()
    h2.SetHandsetSoft(HandsetGame())
    h2.Run()
    return
if __name__=="__main__":
    #singleTest()
    #factoryTest()
    #templateTest()
    #builderTest()
    #proxyTest()
    #protoTest()
    #mediatorTest()
    #cmdTest()
    #dutyChainTest()
    #decorateTest()
    #strategyTest()
    #adapterTest()
    #memoTest()
    #iterTest()
    #observerTest()
    #compositeTest()
    #facadeTest()
    #visitorTest()
    #flyweightTest()
    #stateTest()
    #interpreterTest()
    bridgeTest()