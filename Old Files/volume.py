def volume(x, y, z):
    volume = x*y*z
    return volume

lenghtx = input("How long is the x side? ")
lenghty = input("How long is the y side? ")
lenghtz = input("How long is the z side? ")

while lenghtz and lenghty and lenghtx:
    cube = volume(float(lenghtx), float(lenghty), float(lenghtz))
    print(f"The Volume of the Cube is: {cube}")
    lenghtx = input("How long is the x side? ")
    lenghty = input("How long is the y side? ")
    lenghtz = input("How long is the z side? ")

print("Thanks for calculating with us")