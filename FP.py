# -*- coding: UTF-8 -*-
# 输入

str=input("可读取python表达式：")
print(str)

#open文件
fo=open("Test.txt","w")
fo.write("创建新文本并写入")
print("文件名为：",fo.name)
print("文件的打开模式 ：",fo.mode)
print("文件是否关闭：",fo.closed)
fo.close()

wait=input("Press Enter")

fo=open("Test.txt","r")
pos = fo.tell()
print("文件的位置：",pos)
readstr=fo.read(2)
print("前两字为：",readstr)
fo.close()

wait=input("Press Enter")

fo=open("Test.txt","a")
fo.write(",test append\n")
pos=fo.tell()
print("当前指针的位置",pos)
fo.close()
print("rewrited")

wait=input("Press Enter")

fo=open("Test.txt","r")
readstr=fo.read(10)
print("在设置移动后指针的位置读取2位：",readstr)
pos=fo.seek(0,0)
readstr=fo.read(2)
print("指针设为开头后读取2位：",readstr)
fo.close()
print(fo.closed)

wait=input("End")
