import math

def  haversine(a1, a2, b1, b2):
    a_ = (a2 - a1)* math.pi/180.0
    b_ = (b2 - b1) * math.pi/180.0

    c = pow(math.sin(a_/2), 2) + math.cos(a1 * math.pi/180.0)*math.cos(a2 * math.pi/180.0)*pow(math.sin(b_/2), 2)
    return round(c*6371, 2)
def main():
    print("Enter coordinates of your locations")
    print("Location A: ")
    a1 = input("  latitude: ")
    a2 = input("  longtitude: ")
    print("Location B")
    b1 = input("  latitude: ")
    b2 = input("  longtitude: ")
    print((haversine(a1, a2, b1, b2)))
main()
