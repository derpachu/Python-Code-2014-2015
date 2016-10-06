#computer project07 grade calculation

#list.sort() sorts based on first element so total points should be first
#use str.split() to clean up the file for processing
#REMEMBER WHEN FINISHED TO FIX LINE LENGTHS OF CODE/COMMENTS/DOCSTRINGS (79 characters)
import math

def cal_mean(data_list, file_pos):#just caluclates the mean using the position
    #specified in the list
    count = summation = 0
    for entry in data_list:
        count+=1
    for entry in data_list:
        entry[file_pos] = int(entry[file_pos])
        summation += entry[file_pos]
    mean = summation/count
    return mean
def cal_standard_deviation(data_list, file_pos):#just caluclates the standard
    #deviation using the position specified in the list
    """sqrt(sum(x-x(mean))^2/n-1)"""
    count = summation = 0
    for entry in data_list:
        count+=1
    for entry in data_list:#finds the sum of the (x-xmean)^2
        summation += (entry[file_pos]-cal_mean(data_list, file_pos))**2
    sd = math.sqrt(summation/count)
    return sd
def get_data(input_file):
    """'student' (represented by a 3 digit number)
    each student has 6 scores
    score 1-3 is test 1-3 (total 500)
    score 4 is in-class exercises (total 50)
    score 5 is computer projects (total 450)
    score 6 is lab exercises completed
    get_data = [['001',scores]['002',scores]]"""
    main_data_list = []
    for line in input_file:
        data_list = []#creates a secondary list ot be sorted later
        line = line.split()#cleans out formatting
        tp = float(line[1]) + float(line[2]) + float(line[3]) + \
             float(line[4])+ float(line[5])
        data_list.append(tp)
        data_list.append(line[0])#addes all the values in
        data_list.append(line[1])
        data_list.append(line[2])
        data_list.append(line[3])
        data_list.append(line[4])
        data_list.append(line[5])
        data_list.append(line[6])
        main_data_list.append(data_list)#addes them into the main list
    main_data_list.sort(reverse=True)#sorts from highest to lowest
    return main_data_list
def calculate_grades(main_data_list):
    """calculate_grade = addes total points and the grade out of 4.0 to the\
list
    total points possible = 1000
    scores 1-5 make up final grade
       4.0 = 90
       3.5 = 85
       3.0 = 80
       2.5 = 75
       2.0 = 70
       1.5 = 65
       1.0 = 60"""
    for entry in main_data_list:
        perc = entry[0]/1000
        perc = round(perc,2)#rounds it to be gradeable
        if perc >= 0.90:#sorts based on the grade bracket it belongs in
            entry.append(4.0)#each one adds the GPA to the end of the list
        elif perc >= 0.85:
            entry.append(3.5)
        elif perc >= 0.80:
            entry.append(3.0)
        elif perc >= 0.75:
            entry.append(2.5)
        elif perc >= 0.70:
            entry.append(2.0)
        elif perc >= 0.65:
            entry.append(1.5)
        elif perc >= 0.60:
            entry.append(1.0)
        else:
            entry.append(0.0)
    return None
def adjust_grades(main_data_list):
    """if student misses more than 2 labs then each lab past 2 deducts 0.5 \
from final score
    grades cannot be below 0.0"""
    for entry in main_data_list:
        lab_score = int(entry[7])
        #print(entry[7],end = " ")
        #print(entry[8])
        if lab_score <= 13: #checks to see if the lab score is below the\
            #grading threshhold
            deduction = (13-(lab_score+1))*0.5 #calculates how much to take off
            #print("\t",deduction)
            entry[8] -= deduction
            #print("\t\t",entry[8])
        if entry[8] < 0.0:#makes sure the grade cannot go below 0.0
            entry[8] = 0.0
    return None 
def display_grades(main_data_list):
    """prints
    statistics on all students
        means/standard deviations
            total points earned (float with one decimal)
            total points earned from in class exercises (float with one \
            decimal)
    correlation between in class exercise and total points
        for each "pair" x = in class points, y = total points
        needs means and standard deviations of each pair
        z = sums (x-x(mean))*(y-y(mean)) for all pairs
        r = 1/(n-1)*(z/(sdx*sdy)
    table of all students
        each student info will be
            format it so it displays
                ID number, course grade, total points earned, exam points, in \
                class points, project points, labs done
            the table will have column headers
            table will be formatted from highest total points to lowest total\
             points"""
    mean_tp = round(cal_mean(main_data_list, 0),1)#next 4 just refrence the
    #upper functions and prints them
    sd_tp = round(cal_standard_deviation(main_data_list, 0),1)
    mean_ip = round(cal_mean(main_data_list, 5),1)
    sd_ip = round(cal_standard_deviation(main_data_list, 5),1)
    print("mean of total points: ", mean_tp)
    print("standard deviation of total points: ", sd_tp)
    print("mean of inclass points: ", mean_ip)
    print("standard deviation of inclass points: ", sd_ip)
    count = z = x = r = y = 0#start of the correlations computation
    for entry in main_data_list:
        count+=1
    for entry in main_data_list:
        x += (entry[5]-mean_ip)
    for entry in main_data_list:
        y += (entry[0]-mean_tp)
    z = x*y#multiplies the summations of the two means
    r = (1/count)*(z/(sd_tp*sd_ip))#addes in the rest of the formula
    print("Corelation value: ", r)
    print("ID  GPA tpt tst ic cp  lp")#prints the header
    for entry in main_data_list:#goes through each entry in the list of lists
        #and displays the data inside
        test = int(entry[2]) + int(entry[3]) + int(entry[4])
        print("{:3} {:3} {:3} {:3} {:2} {:3} {:2}".format\
              (entry[1], entry[8], entry[0], test, entry[5], entry[6]\
               , entry[7]))
    return None
def main():
    file_name = input("please enter the file name: ")#gets the data file
    input_file = open(file_name, "r")
    student_data = get_data(input_file)#calls functions in order data list =
    #student data
    calculate_grades(student_data)
    adjust_grades(student_data)
    display_grades(student_data)
    input_file.close()
    return None
main()#executes it all
