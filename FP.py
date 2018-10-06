import os

fo=open("Test.txt","w")
fo.write("Create a file")
fo.flush()
fo.close()

print("done")
mid=input(":")

fo=open("Test.txt","r")
str=fo.read(5)
print("read the line : ",str)
fo.close()

print("done")
mid=input("change the file name right?:")


os.rename("Test.txt","change.txt")
fo=open("change.txt","r")
print("file name : ",fo.name)

print("done")
mid=input("deleta the file right?:")

try:
  os.remove("Test.txt")
  print("del done")
except OSError:
  print("Error : No sach file")
else:
  print("done")

print("catched the error")

pos=os.getcwd()
print(pos)


