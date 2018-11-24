import threading
import time
#这里使用__new__来实现单例模式

class Singleton(object):#抽象单例模式
    '''
        目的：不管什么情况下实例只有一个
    '''
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):#类没有实例的情况下，生成一个实例
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls,*args,**kw)
        return cls._instance#有实例的情况下返回这个实例

#总线
class Bus(Singleton):#Bus 继承了Singleton所以Bus就是一个单例模式
    lock = threading.RLock()#保证在一个时候只能有一个进程或者一个县城或者一个实体去使用它
    def sendData(self,data):
        self.lock.acquire()#锁定
        time.sleep(3)
        print('Sending Signal Data...',data)
        self.lock.release()#释放锁

#线程对象，为更加说明单例的含义，这里讲Bus对象实例化写在了run里
class VisitEntity(threading.Thread):#多线程访问实体，threading中必须有一个run函数，形成多线程
    my_buy = ""
    name = ""
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):#run函数必须实现
        self.my_buy = Bus()
        self.my_buy.sendData(self.name)

if __name__ == '__main__':
    for i in range(3):
        print("Entity %d begin to run ...")
        my_entity = VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()#把线程跑起来






