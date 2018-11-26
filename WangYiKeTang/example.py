#encoding=utf8
class StockQueryDevice():
    stock_code="0"
    stock_price=0.0
    def login(self,usr,pwd):
        pass
    def setCode(self,code):
        self.stock_code=code
    def queryPrice(self):
        pass
    def showPrice(self):
        pass
    def operateQuery(self,usr,pwd,code):
        if not self.login(usr,pwd):
            return False
        self.setCode(code)
        self.queryPrice()
        self.showPrice()
        return True
class WebAStockQueryDevice(StockQueryDevice):
    def login(self,usr,pwd):
        if usr=="myStockA" and pwd=="myPwdA":
            print "Web A:Login OK... user:%s pwd:%s"%(usr,pwd)
            return True
        else:
            print "Web A:Login ERROR... user:%s pwd:%s"%(usr,pwd)
            return False
    def queryPrice(self):
        print "Web A Querying...code:%s "%self.stock_code
        self.stock_price=20.00
    def showPrice(self):
        print "Web A Stock Price...code:%s price:%s"%(self.stock_code,self.stock_price)
class WebBStockQueryDevice(StockQueryDevice):
    def login(self,usr,pwd):
        if usr=="myStockB" and pwd=="myPwdB":
            print "Web B:Login OK... user:%s pwd:%s"%(usr,pwd)
            return True
        else:
            print "Web B:Login ERROR... user:%s pwd:%s"%(usr,pwd)
            return False
    def queryPrice(self):
        print ("Web B Querying...code:%s "%self.stock_code
        self.stock_price=30.00
    def showPrice(self):
        print "Web B Stock Price...code:%s price:%s"%(self.stock_code,self.stock_price)
class Burger():
    name=""
    price=0.0
    type="BURGER"
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0

class Snack():
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

class order():
    burger=""
    snack=""
    beverage=""
    def __init__(self,orderBuilder):
        self.burger=orderBuilder.bBurger
        self.snack=orderBuilder.bSnack
        self.beverage=orderBuilder.bBeverage
    def show(self):
        print("Burger:%s"%self.burger.getName())
        print("Snack:%s"%self.snack.getName())
        print("Beverage:%s"%self.beverage.getName())

class orderBuilder():
    bBurger=""
    bSnack=""
    bBeverage=""
    def addBurger(self,xBurger):
        self.bBurger=xBurger
    def addSnack(self,xSnack):
        self.bSnack=xSnack
    def addBeverage(self,xBeverage):
        self.bBeverage=xBeverage
    def build(self):
        return order(self)
class orderDirector():
    order_builder=""
    def __init__(self,order_builder):
        self.order_builder=order_builder
    def createOrder(self,burger,snack,beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()
class simpleFoodFactory():
    @classmethod
    def createFood(cls,foodClass):
        print "Simple factory produce a instance."
        foodIns = foodClass()
        return foodIns
class foodFactory():
    type=""
    def createFood(self,foodClass):
        print self.type," factory produce a instance."
        foodIns=foodClass()
        return foodIns
class burgerFactory(foodFactory):
    def __init__(self):
        self.type="BURGER"
class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"
class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"



import threading
import time
#这里使用高级方法__new__来实现单例模式
class Singleton(object):#抽象单例
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
#总线
class Bus(Singleton):
    lock = threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print "Sending Signal Data...",data
        self.lock.release()
#线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus=""
    name=""
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)
from copy import copy, deepcopy
class simpleLayer:
    background=[0,0,0,0]
    content="blank"
    def getContent(self):
        return self.content
    def getBackgroud(self):
        return self.background
    def paint(self,painting):
        self.content=painting
    def setParent(self,p):
        self.background[3]=p
    def fillBackground(self,back):
        self.background=back
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)
info_struct=dict()
info_struct["addr"]=10000
info_struct["content"]=""
class Server:
    content=""
    def recv(self,info):
        pass
    def send(self,info):
        pass
    def show(self):
        pass
class infoServer(Server):
    def recv(self,info):
        self.content=info
        return "recv OK!"
    def send(self,info):
        pass
    def show(self):
        print "SHOW:%s"%self.content
class serverProxy:
    pass
class infoServerProxy(serverProxy):
    server=""
    def __init__(self,server):
        self.server=server
    def recv(self,info):
        return self.server.recv(info)
    def show(self):
        self.server.show()

class whiteInfoServerProxy(infoServerProxy):
    white_list=[]
    def recv(self,info):
        try:
            assert type(info)==dict
        except:
            return "info structure is not correct"
        addr=info.get("addr",0)
        if not addr in self.white_list:
            return "Your address is not in the white list."
        else:
            content=info.get("content","")
            return self.server.recv(content)
    def addWhite(self,addr):
        self.white_list.append(addr)
    def rmvWhite(self,addr):
        self.white_list.remove(addr)
    def clearWhite(self):
        self.white_list=[]
class LogManager:
    @staticmethod
    def log(func):
        def wrapper(*args):
            print "Visit Func %s"%func.__name__
            return func(*args)
        return wrapper
class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    @LogManager.log
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    @LogManager.log
    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

class drinkDecorator():
    def getName(self):
        pass
    def getPrice(self):
        pass

class iceDecorator(drinkDecorator):
    def __init__(self,beverage):
        self.beverage=beverage
    def getName(self):
        return self.beverage.getName()+" +ice"
    def getPrice(self):
        return self.beverage.getPrice()+0.3

class sugarDecorator(drinkDecorator):
    def __init__(self,beverage):
        self.beverage=beverage
    def getName(self):
        return self.beverage.getName()+" +sugar"
    def getPrice(self):
        return self.beverage.getPrice()+0.5

class abstractMediator():
    purchase=""
    sales=""
    warehouse=""
    def setPurchase(self,purchase):
        self.purchase=purchase
    def setWarehouse(self,warehouse):
        self.warehouse=warehouse
    def setSales(self,sales):
        self.sales=sales
    def execute(self,content,num):
        pass
class stockMediator(abstractMediator):
    def execute(self,content,num):
        print "MEDIATOR:Get Info--%s"%content
        if  content=="buy":
            self.warehouse.inc(num)
            self.sales.getNotice("Bought %s"%num)
        elif content=="increase":
            self.sales.getNotice("Inc %s"%num)
            self.purchase.getNotice("Inc %s"%num)
        elif content=="decrease":
            self.sales.getNotice("Dec %s"%num)
            self.purchase.getNotice("Dec %s"%num)
        elif content=="warning":
            self.sales.getNotice("Stock is low.%s Left."%num)
            self.purchase.getNotice("Stock is low. Please Buy More!!! %s Left"%num)
        elif content=="sell":
            self.warehouse.dec(num)
            self.purchase.getNotice("Sold %s"%num)
        else:
            pass
class colleague():
    mediator = None
    def __init__(self,mediator):
        self.mediator = mediator
class purchaseColleague(colleague):
    def buyStuff(self,num):
        print "PURCHASE:Bought %s"%num
        self.mediator.execute("buy",num)
    def getNotice(self,content):
        print "PURCHASE:Get Notice--%s"%content
class warehouseColleague(colleague):
    total=0
    threshold=100
    def setThreshold(self,threshold):
        self.threshold=threshold
    def isEnough(self):
        if self.total<self.threshold:
            print "WAREHOUSE:Warning...Stock is low... "
            self.mediator.execute("warning",self.total)
            return False
        else:
            return True
    def inc(self,num):
        self.total+=num
        print "WAREHOUSE:Increase %s"%num
        self.mediator.execute("increase",num)
        self.isEnough()
    def dec(self,num):
        if num>self.total:
            print "WAREHOUSE:Error...Stock is not enough"
        else:
            self.total-=num
            print "WAREHOUSE:Decrease %s"%num
            self.mediator.execute("decrease",num)
        self.isEnough()
class salesColleague(colleague):
    def sellStuff(self,num):
        print "SALES:Sell %s"%num
        self.mediator.execute("sell",num)
    def getNotice(self, content):
        print "SALES:Get Notice--%s" % content

class Command():
    receiver = None
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        pass
class foodCommand(Command):
    dish=""
    def __init__(self,receiver,dish):
        self.receiver=receiver
        self.dish=dish
    def execute(self):
        self.receiver.cook(self.dish)

class mainFoodCommand(foodCommand):
    pass
class coolDishCommand(foodCommand):
    pass
class hotDishCommand(foodCommand):
    pass

class backSys():
    def cook(self,dish):
        pass
class mainFoodSys(backSys):
    def cook(self,dish):
        print "MAINFOOD:Cook %s"%dish
class coolDishSys(backSys):
    def cook(self,dish):
        print "COOLDISH:Cook %s"%dish
class hotDishSys(backSys):
    def cook(self,dish):
        print "HOTDISH:Cook %s"%dish
class menuAll:
    menu_map=dict()
    def loadMenu(self):
        self.menu_map["hot"] = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]
    def isHot(self,dish):
        if dish in self.menu_map["hot"]:
            return True
        return False
    def isCool(self,dish):
        if dish in self.menu_map["cool"]:
            return True
        return False
    def isMain(self,dish):
        if dish in self.menu_map["main"]:
            return True
        return False
class waiterSys():
    menu_map=dict()
    commandList=[]
    def setOrder(self,command):
        print "WAITER:Add dish"
        self.commandList.append(command)

    def cancelOrder(self,command):
        print "WAITER:Cancel order..."
        self.commandList.remove(command)

    def notify(self):
        print "WAITER:Nofify..."
        for command in self.commandList:
            command.execute()
class manager():
    successor = None
    name = ''
    def __init__(self, name):
        self.name = name
    def setSuccessor(self, successor):
        self.successor = successor
    def handleRequest(self, request):
        pass
class lineManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 3:
            print '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)
        else:
            print '%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number)
            if self.successor != None:
                self.successor.handleRequest(request)
class departmentManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 7:
            print '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)
        else:
            print '%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number)
            if self.successor != None:
                self.successor.handleRequest(request)
class generalManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff':
            print '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)
class request():
    requestType = ''
    requestContent = ''
    number = 0

class customer:
    customer_name=""
    snd_way=""
    info=""
    phone=""
    email=""
    def setPhone(self,phone):
        self.phone=phone
    def setEmail(self,mail):
        self.email=mail
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email
    def setInfo(self,info):
        self.info=info
    def setName(self,name):
        self.customer_name=name
    def setBrdWay(self,snd_way):
        self.snd_way=snd_way
    def sndMsg(self):
        self.snd_way.send(self.info)
class msgSender:
    dst_code=""
    def setCode(self,code):
        self.dst_code=code
    def send(self,info):
        pass
class emailSender(msgSender):
    def send(self,info):
        print "EMAIL_ADDRESS:%s EMAIL:%s"%(self.dst_code,info)
class textSender(msgSender):
    def send(self,info):
        print "PHONE_NUMBER:%s TEXT:%s"%(self.dst_code,info)
class ACpnStaff:
    name=""
    id=""
    phone=""
    def __init__(self,id):
        self.id=id
    def getName(self):
        print "A protocol getName method...id:%s"%self.id
        return self.name
    def setName(self,name):
        print "A protocol setName method...id:%s"%self.id
        self.name=name
    def getPhone(self):
        print "A protocol getPhone method...id:%s"%self.id
        return self.phone
    def setPhone(self,phone):
        print "A protocol setPhone method...id:%s"%self.id
        self.phone=phone
class BCpnStaff:
    name=""
    id=""
    telephone=""
    def __init__(self,id):
        self.id=id
    def get_name(self):
        print "B protocol get_name method...id:%s"%self.id
        return self.name
    def set_name(self,name):
        print "B protocol set_name method...id:%s"%self.id
        self.name=name
    def get_telephone(self):
        print "B protocol get_telephone method...id:%s"%self.id
        return self.telephone
    def set_telephone(self,telephone):
        print "B protocol get_name method...id:%s"%self.id
        self.telephone=telephone
class CpnStaffAdapter:
    b_cpn=""
    def __init__(self,id):
        self.b_cpn=BCpnStaff(id)
    def getName(self):
        return self.b_cpn.get_name()
    def getPhone(self):
        return self.b_cpn.get_telephone()
    def setName(self,name):
        self.b_cpn.set_name(name)
    def setPhone(self,phone):
        self.b_cpn.set_telephone(phone)


class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor=AlarmSensor()
        self.water_sprinker=WaterSprinker()
        self.emergency_dialer=EmergencyDialer()
    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()
class Company:
    name = ''
    def __init__(self, name):
        self.name = name
    def add(self, company):
        pass
    def remove(self, company):
        pass
    def display(self, depth):
        pass
    def listDuty(self):
        pass

class ConcreteCompany(Company):
    childrenCompany = None
    def __init__(self, name):
        Company.__init__(self,name)
        self.childrenCompany = []
    def add(self, company):
        self.childrenCompany.append(company)
    def remove(self, company):
        self.childrenCompany.remove(company)
    def display(self, depth):
        print'-'*depth + self.name
        for component in self.childrenCompany:
            component.display(depth+1)
    def listDuty(self):
        for component in self.childrenCompany:
            component.listDuty()
class HRDepartment(Company):
    def __init__(self, name):
         Company.__init__(self,name)
    def display(self, depth):
        print '-'*depth + self.name
    def listDuty(self): #履行职责
        print '%s\t Enrolling & Transfering management.' % self.name

class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self,name)
    def display(self, depth):
        print "-" * depth + self.name
    def listDuty(self): #履行职责
        print '%s\tFinance Management.'%self.name

class RdDepartment(Company):
    def __init__(self,name):
        Company.__init__(self,name)
    def display(self, depth):
        print "-"*depth+self.name
    def listDuty(self):
        print "%s\tResearch & Development."% self.name

class Coffee:
    name = ''
    price =0
    def __init__(self,name):
        self.name = name
        self.price = len(name)#在实际业务中，咖啡价格应该是由配置表进行配置，或者调用接口获取等方式得到，此处为说明享元模式，将咖啡价格定为名称长度，只是一种简化
    def show(self):
        print "Coffee Name:%s Price:%s"%(self.name,self.price)
class CoffeeFactory():
    coffee_dict = {}
    def getCoffee(self, name):
        if self.coffee_dict.has_key(name) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]
    def getCoffeeCount(self):
        return len(self.coffee_dict)
class Customer:
    coffee_factory=""
    name=""
    def __init__(self,name,coffee_factory):
        self.name=name
        self.coffee_factory=coffee_factory
    def order(self,coffee_name):
        print "%s ordered a cup of coffee:%s"%(self.name,coffee_name)
        return self.coffee_factory.getCoffee(coffee_name)
class Shape:
    name=""
    param=""
    def __init__(self,*param):
        pass
    def getName(self):
        return self.name
    def getParam(self):
        return self.name,self.param

class Pen:
    shape=""
    type=""
    def __init__(self,shape):
        self.shape=shape
    def draw(self):
        pass

class Rectangle(Shape):
    def __init__(self,long,width):
        self.name="Rectangle"
        self.param="Long:%s Width:%s"%(long,width)
        print "Create a rectangle:%s"%self.param
class Circle(Shape):
    def __init__(self,radius):
        self.name="Circle"
        self.param="Radius:%s"%radius
        print "Create a circle:%s"%self.param

class NormalPen(Pen):
    def __init__(self,shape):
        Pen.__init__(self,shape)
        self.type="Normal Line"
    def draw(self):
        print "DRAWING %s:%s----PARAMS:%s"%(self.type,self.shape.getName(),self.shape.getParam())
class BrushPen(Pen):
    def __init__(self,shape):
        Pen.__init__(self,shape)
        self.type="Brush Line"
    def draw(self):
        print "DRAWING %s:%s----PARAMS:%s" % (self.type,self.shape.getName(), self.shape.getParam())


class MyIter(object):
    def __init__(self, n):
        self.index = 0
        self.n = n
    def __iter__(self):
        return MyIter(self.n)
        #return self
    def next(self):
        if self.index < self.n:
            value = self.index**2
            self.index += 1
            return value
        else:
            raise StopIteration()
def MyGenerater(n):
    index=0
    while index<n:
        yield index**2
        index+=1

class Visitor:
    name=""
    def setName(self,name):
        self.name=name
    def visit(self,medicine):
        pass
class Charger(Visitor):
    def visit(self,medicine):
        print "CHARGE: %s lists the Medicine %s. Price:%s"%(self.name,medicine.getName(),medicine.getPrice())
class Pharmacy(Visitor):
    def visit(self,medicine):
        print "PHARMACY:%s offers the Medicine %s. Price:%s"%(self.name,medicine.getName(),medicine.getPrice())

class Medicine:
    name=""
    price=0.0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def accept(self,visitor):
        pass

class Antibiotic(Medicine):
    def accept(self,visitor):
        visitor.visit(self)
class Coldrex(Medicine):
    def accept(self,visitor):
        visitor.visit(self)
class ObjectStructure:
    pass
class Prescription(ObjectStructure):
    medicines=[]
    def addMedicine(self,medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self,medicine):
        self.medicines.append(medicine)
    def visit(self,visitor):
        for medc in self.medicines:
            medc.accept(visitor)
def max_num(x,y,z):
    return max(max(x,y),z)
def max_num(x,y):
    return max(x,y)
class PlayContext():
    play_text = None

class Expression():
    def interpret(self, context):
        if len(context.play_text) == 0:
            return
        else:
            play_segs=context.play_text.split(" ")
            for play_seg in play_segs:
                pos=0
                for ele in play_seg:
                    if ele.isalpha():
                        pos+=1
                        continue
                    break
                play_chord = play_seg[0:pos]
                play_value = play_seg[pos:]
                self.excute(play_chord,play_value)
    def excute(self,play_key,play_value):
        pass

class NormGuitar(Expression):
    def excute(self, key, value):
        print "Normal Guitar Playing--Chord:%s Play Tune:%s"%(key,value)

class Observer:
    def update(self):
        pass
class AlarmSensor(Observer):
    def update(self,action):
        print "Alarm Got: %s" % action
        self.runAlarm()
    def runAlarm(self):
        print "Alarm Ring..."
class WaterSprinker(Observer):
    def update(self,action):
        print "Sprinker Got: %s" % action
        self.runSprinker()
    def runSprinker(self):
        print "Spray Water..."
class EmergencyDialer(Observer):
    def update(self,action):
        print "Dialer Got: %s"%action
        self.runDialer()
    def runDialer(self):
        print "Dial 119..."
class Observed:
    observers=[]
    action=""
    def addObserver(self,observer):
        self.observers.append(observer)
    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)
class smokeSensor(Observed):
    def setAction(self,action):
        self.action=action
    def isFire(self):
        return True
import random
class GameCharacter():
    vitality = 0
    attack = 0
    defense = 0
    def displayState(self):
        print 'Current Values:'
        print 'Life:%d' % self.vitality
        print 'Attack:%d' % self.attack
        print 'Defence:%d' % self.defense
    def initState(self,vitality,attack,defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
    def saveState(self):
        return Memento(self.vitality, self.attack, self.defense)
    def recoverState(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense
class FightCharactor(GameCharacter):
    def fight(self):
        self.vitality -= random.randint(1,10)

class Memento:
    vitality = 0
    attack = 0
    defense = 0
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
class stateAdmin:
    memento=""
class LiftState:
    context=""
    def setContext(self,context):
        self.context=context
    def open(self):
        pass
    def close(self):
        pass
    def run(self):
        pass
    def stop(self):
        pass
class OpenState(LiftState):
    def open(self):
        print "OPEN:The door is opened..."
        return self
    def close(self):
        print "OPEN:The door start to close..."
        print "OPEN:The door is closed"
        return StopState()
    def run(self):
        print "OPEN:Run Forbidden."
        return self
    def stop(self):
        print "OPEN:Stop Forbidden."
        return self
class CloseState(LiftState):
    def open(self):
        print "CLOSE:The door is opening..."
        return OpenState()
    def close(self):
        print "CLOSE:The door is closed..."
        return self
    def run(self):
        print "CLOSE:The lift start to run..."
        return RunState()
    def stop(self):
        return self
class RunState(LiftState):
    def open(self):
        print "RUN:Open Forbidden."
        return self
    def close(self):
        print "RUN:Close Forbidden."
        return self
    def run(self):
        print "RUN:The lift is running..."
        return self
    def stop(self):
        print "RUN:The lift start to stop..."
        print "RUN:The lift stopped..."
        return StopState()
class StopState(LiftState):
    def open(self):
        print "STOP:The door is opening..."
        print "STOP:The door is opened..."
        return OpenState()
    def close(self):
        print "STOP:Close Forbidden"
        return self
    def run(self):
        print "STOP:The lift start to run..."
        return RunState()
    def stop(self):
        print "STOP:The lift is stopped."
        return self
class Context:
    lift_state=""
    def getState(self):
        return self.lift_state
    def setState(self,lift_state):
        self.lift_state=lift_state
    def open(self):
        self.setState(self.lift_state.open())
    def close(self):
        self.setState(self.lift_state.close())
    def run(self):
        self.setState(self.lift_state.run())
    def stop(self):
        self.setState(self.lift_state.stop())
if __name__=="__main__":
    ctx = Context()
    ctx.setState(StopState())
    ctx.open()
    ctx.run()
    ctx.close()
    ctx.run()
    ctx.stop()
    '''
    game_chrctr = FightCharactor()
    game_chrctr.initState(100,79,60)
    game_chrctr.displayState()
    state_admin = stateAdmin()
    state_admin.memento = game_chrctr.saveState()
    game_chrctr.fight()
    game_chrctr.displayState()
    game_chrctr.recoverState(state_admin.memento)
    game_chrctr.displayState()

    alarm=AlarmSensor()
    sprinker=WaterSprinker()
    dialer=EmergencyDialer()

    smoke_sensor=smokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)


    if smoke_sensor.isFire():
        smoke_sensor.setAction("On Fire!")
        smoke_sensor.notifyAll()


    context = PlayContext()
    context.play_text = "C53231323 Em43231323 F43231323 G63231323"
    guitar=NormGuitar()
    guitar.interpret(context)

    print max_num(1,2,4)
    yinqiao_pill=Coldrex("Yinqiao Pill",2.0)
    penicillin=Antibiotic("Penicillin",3.0)
    doctor_prsrp=Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)

    charger=Charger()
    charger.setName("Doctor Strange")
    pharmacy=Pharmacy()
    pharmacy.setName("Doctor Wei")
    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharmacy)

    x_square=MyGenerater(10)
    for x in x_square:
        print x

    x_square=MyIter(10)
    for x in x_square:
        print x
    for x in x_square:
        print x

    lst=["hello Alice","hello Bob","hello Eve"]
    lst_iter=iter(lst)
    print lst_iter
    print lst_iter.next()
    print lst_iter.next()
    print lst_iter.next()
    print lst_iter.next()

    normal_pen=NormalPen(Rectangle("20cm","10cm"))
    brush_pen=BrushPen(Circle("15cm"))
    normal_pen.draw()
    brush_pen.draw()

    coffee_factory=CoffeeFactory()
    customer_1=Customer("A Client",coffee_factory)
    customer_2=Customer("B Client",coffee_factory)
    customer_3=Customer("C Client",coffee_factory)
    c1_capp=customer_1.order("cappuccino")
    c1_capp.show()
    c2_mocha=customer_2.order("mocha")
    c2_mocha.show()
    c3_capp=customer_3.order("cappuccino")
    c3_capp.show()
    print "Num of Coffee Instance:%s"%coffee_factory.getCoffeeCount()

    root = ConcreteCompany('HeadQuarter')
    root.add(HRDepartment('HQ HR'))
    root.add(FinanceDepartment('HQ Finance'))
    root.add(RdDepartment("HQ R&D"))

    comp = ConcreteCompany('East Branch')
    comp.add(HRDepartment('East.Br HR'))
    comp.add(FinanceDepartment('East.Br Finance'))
    comp.add(RdDepartment("East.Br R&D"))
    root.add(comp)

    comp1 = ConcreteCompany('Northast Branch')
    comp1.add(HRDepartment('Northeast.Br HR'))
    comp1.add(FinanceDepartment('Northeast.Br Finance'))
    comp1.add(RdDepartment("Northeast.Br R&D"))
    comp.add(comp1)

    comp2 = ConcreteCompany('Southeast Branch')
    comp2.add(HRDepartment('Southeast.Br HR'))
    comp2.add(FinanceDepartment('Southeast.Br Finance'))
    comp2.add(RdDepartment("Southeast.Br R&D"))
    comp.add(comp2)

    root.display(1)

    root.listDuty()

    emergency_facade=EmergencyFacade()
    emergency_facade.runAll()

    acpn_staff=ACpnStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print "A Staff Name:%s"%acpn_staff.getName()
    print "A Staff Phone:%s"%acpn_staff.getPhone()
    bcpn_staff=CpnStaffAdapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print "B Staff Name:%s"%bcpn_staff.getName()
    print "B Staff Phone:%s"%bcpn_staff.getPhone()

    customer_x=customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")
    customer_x.setEmail("customer_x@xmail.com")
    customer_x.setInfo("Welcome to our new party!")
    text_sender=textSender()
    text_sender.setCode(customer_x.getPhone())
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()
    mail_sender=emailSender()
    mail_sender.setCode(customer_x.getEmail())
    customer_x.setBrdWay(mail_sender)
    customer_x.sndMsg()


    line_manager = lineManager('LINE MANAGER')
    department_manager = departmentManager('DEPARTMENT MANAGER')
    general_manager = generalManager('GENERAL MANAGER')

    line_manager.setSuccessor(department_manager)
    department_manager.setSuccessor(general_manager)

    req = request()
    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 1 day off'
    req.number = 1
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 5 days off'
    req.number = 5
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 10 days off'
    req.number = 10
    line_manager.handleRequest(req)

    dish_list=["Yu-Shiang Shredded Pork","Sauteed Tofu, Home Style","Cucumber","Rice"]
    waiter_sys=waiterSys()
    main_food_sys=mainFoodSys()
    cool_dish_sys=coolDishSys()
    hot_dish_sys=hotDishSys()
    menu=menuAll()
    menu.loadMenu()
    for dish in dish_list:
        if menu.isCool(dish):
            cmd=coolDishCommand(cool_dish_sys,dish)
        elif menu.isHot(dish):
            cmd=hotDishCommand(hot_dish_sys,dish)
        elif menu.isMain(dish):
            cmd=mainFoodCommand(main_food_sys,dish)
        else:
            continue
        waiter_sys.setOrder(cmd)
    waiter_sys.notify()

    mobile_mediator=stockMediator()
    mobile_purchase=purchaseColleague(mobile_mediator)
    mobile_warehouse=warehouseColleague(mobile_mediator)
    mobile_sales=salesColleague(mobile_mediator)
    mobile_mediator.setPurchase(mobile_purchase)
    mobile_mediator.setWarehouse(mobile_warehouse)
    mobile_mediator.setSales(mobile_sales)

    mobile_warehouse.setThreshold(200)
    mobile_purchase.buyStuff(300)
    mobile_sales.sellStuff(120)

    coke_cola=coke()
    print "Name:%s"%coke_cola.getName()
    print "Price:%s"%coke_cola.getPrice()
    ice_coke=iceDecorator(coke_cola)
    print "Name:%s" % ice_coke.getName()
    print "Price:%s" % ice_coke.getPrice()
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello World!"
    info_server = infoServer()
    info_server_proxy = whiteInfoServerProxy(info_server)
    print info_server_proxy.recv(info_struct)
    info_server_proxy.show()
    info_server_proxy.addWhite(10010)
    print info_server_proxy.recv(info_struct)
    info_server_proxy.show()

    dog_layer=simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0,0,255,0])
    print "Original Background:",dog_layer.getBackgroud()
    print "Original Painting:",dog_layer.getContent()
    another_dog_layer=dog_layer.deep_clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint("Puppy")
    print "Original Background:", dog_layer.getBackgroud()
    print "Original Painting:", dog_layer.getContent()
    print "Copy Background:", another_dog_layer.getBackgroud()
    print "Copy Painting:", another_dog_layer.getContent()
    #web_a_query_dev=WebAStockQueryDevice()
    #web_a_query_dev.operateQuery("myStockB","myPwdA","12345")
    #web_a_query_dev.login("myStockA","myPwdA")
    #web_a_query_dev.setCode("12345")
    #web_a_query_dev.queryPrice()
    #web_a_query_dev.showPrice()



    order_builder=orderBuilder()
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())
    order_1=order_builder.build()
    order_1.show()

    spicy_chicken_burger=simpleFoodFactory.createFood(spicyChickenBurger)
    burger_factory=burgerFactory()
    snack_factorry=snackFactory()
    beverage_factory=beverageFactory()
    cheese_burger=burger_factory.createFood(cheeseBurger)
    print cheese_burger.getName(),cheese_burger.getPrice()
    chicken_wings=snack_factorry.createFood(chickenWings)
    print chicken_wings.getName(),chicken_wings.getPrice()
    coke_drink=beverage_factory.createFood(coke)
    print coke_drink.getName(),coke_drink.getPrice()
    #for i in range(3):
    #    print "Entity %d begin to run..."%i
    #    my_entity=VisitEntity()
    #    my_entity.setName("Entity_"+str(i))
    #    my_entity.start()
    '''




class fruit():
    shape=""
    color=""

class apple():
    shape="Round"
    color="Red"
class pear():
    shape=""
    color=""
class farmer:
    def plant(self,fruit):
        pass
if __name__=="__main__":
    f=farmer()
    f.plant(pear())















