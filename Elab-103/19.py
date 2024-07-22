import math 
def sphere_volume(r):
    return 4/3*math.pi*(r**3)

def sphere_surface_area(r):
    return 4*math.pi*r*r

r = float(input('Enter sphere radius: '))
print('Sphere volume is', format(sphere_volume(r),'.2f'))
print('Sphere surface area is', format(sphere_surface_area(r),'.2f'))