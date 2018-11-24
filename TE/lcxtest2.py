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

#如何读取CSV数据
import csv
with open('test.xls','wb') as f:
    writer = csv.writer(f)
    writer.writerow('asdf')









