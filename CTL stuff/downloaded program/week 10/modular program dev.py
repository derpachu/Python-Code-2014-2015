def get_file():
    file = open("grades.txt", "r")
    data = {}
    for line in file:
        line = line.strip()
        line = line.split(",")
        key = line[0]
        value = list()
        for val in line[1:]:
            value.append(int(val))
        data[key] = value
    file.close
    return data

def print_scores(database):
##    template = "{:10}\t{:2}\t{:2}\t{:2}\t{:2}"
##    print(template.format("Assignment",1,2,3,4))
##    header = database["Points"]
##    print(template.format("Total Points",header[0],header[1],header[2],header[3]))
##    print("-"*50)
    scores = database["Points"]
    num_scores = len(scores)
    count = 0
    print("Assignment", end = "")
    while count < num_scores:
        print("\t",count, end = "")
        count += 1
    print("\nTotal Points", end = "")
    for score in scores:
        print("\t",score, end = "")
    print()
    print("-"*50)
    #x = database["Points"]
    del database["Points"]
    for entry in database:
        count = 0
        print(entry, end = "\t\t ")
        test = database[entry]
        while count < num_scores:
            print(test[count],end = "\t ")
            count += 1
        print()

def get_score(x, y):
    str_y = str(y)
    while True:
        score = input("Enter a new score, or 'return' for the score "+str_y+": ")
        if score == "":
            return y
        else:
            try:
                score = int(score)
                if 0 <= score <= x:
                    return score
                else:
                    print("Illegal score ", score, "must be between 0 and ", x)
            except ValueError:
                print("Invalid input")
                score = int(input("Enter a new score, or 'return' for the score "+str_y+": "))

def update_student(database,stu_num):
    print("Entering scores for ", stu_num)
    scores = database["Points"]
    num_scores = len(scores)
    count = 0
    while count < num_scores:
        max_score = scores[count]
        default_score = database[stu_num]
        default = default_score[count]
        str_count = str(count+1)
        print("Assignment "+str_count+": Possible points ", max_score, ", Current score ", default)
        score = get_score(max_score, default)
        default_score[count] = score
        count +=1

students = get_file()
update_student(students, "A650111")
print_scores(students)
