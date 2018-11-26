 # 如何设置文件的缓冲open函数的bufferring 全缓冲n>1 行缓冲1 无缓冲0

with open('lcx.txt','w',buffering=1024) as f:
     f.write('abc')
     f.write('='*1024)

# with open('lcx.txt', 'w',buffering=1) as f:
#      f.write('abc\n')
#
# with open('lcx.txt', 'w',buffering=0) as f:
#      f.write('a')

#如何将文件映射到内存 mmap模块的mmap()函数
import mmap

with open('demo.bin','r+b') as f:
    m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
    m[10:20]

# 如何访问文件状态 标准库os模块下的三个系统调用stat,fstat,lstat获取文件状态，中os.path下的一些函数更简洁
import os,time
print(os.stat('lcx.txt'))
# 文件类型
os.path.isdir('lcx.txt') #是否是目录
os.path.isfile('lcx.txt') #是否是文件
os.path.islink('lcx.txt') #是否链接文件
os.path.getatime('lcx.txt') #访问时间
os.path.getsize('lcx.txt') #文件大小
os.path.getmtime('lcx.txt')  #创建时间

# 如何使用临时文件
from tempfile import TemporaryFile,NamedTemporaryFile
tf = TemporaryFile('w+') #只能本进程访问 无路径
tf.write('hello'*100)
tf.seek(0)
print(tf.read(20))

f1=NamedTemporaryFile()  #有文件路径，可以多个进程同时访问


# 如何读写excel
import xlrd

book = xlrd.open_workbook('test1.xlsx')
sheet = book.sheet_by_index(0) #获取对应的sheet
print('总行数：',sheet.nrows)
print('总列数：',sheet.ncols)

cell= sheet.cell(1,0)
print("某单元格的值：",cell.value)
print("某行的值:",sheet.row_values(1))
print("某行的值中从某位置开始:",sheet.row_values(1,1))
print("某行的值中从某位置开始:",sheet.row_values(1,1))

import xlwt
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('testshell')
#==========
#coding:utf8
import xlrd,xlwt
rbook = xlrd.open_workbook('test1.xlsx')
rsheet = rbook.sheet_by_index(0)

nc=rsheet.ncols
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,'总分',None)

for row in range(1,rsheet.nrows):
    t= sum(rsheet.row_values(row,1))
    rsheet.put_cell(row,nc,xlrd.XL_CELL_NUMBER,t,None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)

style = xlwt.easyxf("align:vertical center,horizontal center") #对齐方式
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)

wbook.save('write.xlsx')

#如何为创建大量实例节省内存  定义类的__slots__属性,它是用来声明属性名字的列表
import sys
class Player(object):
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

class Player2(object):
    __slots__ = ['uid','name','stat','level']  ##关闭动态绑定字典
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

p1 = Player('0001','Jim')
p2 = Player2('OOO1','Jim')

print(set(dir(p1)) - set(dir(p2)))
print(p1.__dict__)  #为实例动态绑定的一个字典,占用内存
print(sys.getsizeof(p1.__dict__))

#如何让对象支持上下文管理 需定义实例的__enter__,__exit__方法,它们分别在with开始和结束时被调用














