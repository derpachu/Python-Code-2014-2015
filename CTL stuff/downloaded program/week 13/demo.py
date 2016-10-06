import point

def get_point(x, y):
    return point.Point(x, y)

def data():
    data = []
    z = True
    while z == True:
        x = input("Enter the x and y coordinates (or 'q' to quit): ")
        if x == "q":
            z = False
            continue
        try:
            x_coord = int(x[:1])
            y_coord = int(x[2:3])
            a = get_point(x_coord, y_coord)
            data.append(a)
        except ValueError:
            print("Illegal input: ", x)
    return data
def main():
    main_data = data()
    length = len(main_data)
    count = total = 0
    y = len(main_data)
    if y <= 5:
        for x in range(len(main_data)-1):
            print(main_data[x], end = "")
        print(main_data[len(main_data)-1])
    else:
        z = len(main_data)//5
        w = int(len(main_data)/5)
        for l in range(w):
            for v in range(4):
                print(main_data[v+(5*l)], end= "")
            print(main_data[v+(5*l)+1])
    
    for x in range(len(main_data)-1):
        count += 1
        temp_sum = main_data[x].distance(main_data[count])
        total += temp_sum
    print(total)
main()
