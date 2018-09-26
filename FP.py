from numpy import pi

def get_circle_area(r):
  a=r**2*pi
  return a

radius=10
result=get_circle_area(radius)

if radius>5 & radius<15:
  print("Hellow World!")
elif radius<5 | radius>10:
  print("xx")

print(f"the area is {result}")

for i in range(5):
  print(i)
  if i==3:
    break
else:
  print("done")

if radius==10:
  pass # pass的意思就是啥也不做，但又不能啥也不写
else:
  print("done")
