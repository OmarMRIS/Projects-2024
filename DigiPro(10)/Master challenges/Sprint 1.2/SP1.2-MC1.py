numbers = [1,2,3,4,5,6,7,8,9,10]
print(f"{'Number': ^10}{'|   Square number   |': ^20}{'Cube number': ^15}")
print(f"{'--------': ^10}{'--------------------': ^20}{'---------------': ^15}")

for number in numbers:
    square_number = number ** 2
    cube_number = number ** 3
    print(f"{number: ^10}{square_number: ^20}{cube_number: ^15}")