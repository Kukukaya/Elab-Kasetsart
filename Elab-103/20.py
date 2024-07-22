def compute_rectangle_area(a, b):
    return a*b

def compute_surface_area(x, y, z):
    return 2*compute_rectangle_area(x, y)+2*compute_rectangle_area(z, y)+2*compute_rectangle_area(x, z)

def compute_volume(x, y, z):
    return x*y*z

w = float(input('Enter width: '))
l = float(input('Enter length: '))
h = float(input('Enter height: '))

print(f"For [{format(w, '.2f')} x {format(l, '.2f')} x {format(h, '.2f')}] cuboid:")
print(f"Surface area = {format(compute_surface_area(w, l, h), '.3f')}")
print(f"Volume = {format(compute_volume(w, l, h), '.3f')}")

w*=2
l*=2
h*=2
print("\nAfter doubling each side,")

print(f"For [{format(w, '.2f')} x {format(l, '.2f')} x {format(h, '.2f')}] cuboid:")
print(f"Surface area = {format(compute_surface_area(w, l, h), '.3f')}")
print(f"Volume = {format(compute_volume(w, l, h), '.3f')}")