def squares(x, y):
    """input start number and an end number"""
    total = 0
    z = 1
    while z <= y:
        total += x**2
        x += 1
        z += 1
    return total
def cubes(x, y):
    """input start number and an end number"""
    total = 0
    z = 1
    while z <= y:
        total += x**3
        x += 1
        z += 1
    return total
def main():
    command_input = input("please input a command ")
    command_input = command_input.lower()
    while command_input != "exit":
        if command_input == "squares":
            x = int(input("enter the start number "))
            y = int(input("number of iterations "))
            print(squares(x,y))
            command_input = input("please input a command ")
            command_input = command_input.lower()
        elif command_input == "cubes":
            x = int(input("enter the start number "))
            y = int(input("number of iterations "))
            print(cubes(x,y))
            command_input = input("please input a command ")
            command_input = command_input.lower()
        else:
            print("*** Invalid choice ***")
            command_input = input("please input a command ")
            command_input = command_input.lower()
    print("program halted")

main()
