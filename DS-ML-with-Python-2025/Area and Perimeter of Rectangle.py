def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

print("Area =", area(l, w))
print("Perimeter =", perimeter(l, w))
