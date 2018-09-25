from numpy import pi

def get_circle_area(r):
  a=r**2*pi
  return a


radius=10
result=get_circle_area(radius)

print(f"the area is {result}")
