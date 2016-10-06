#ask for the name of the input file, keeps trying until a valid input is made
#names will be the first 20 characters
#2 scores will be recorded afterwards separated by numerous spaces
#the program will read in the inputs and store the data in tuples
    #formatted:
    #name
    #exam 1 score (int)
    #exam 2 score (int)
    #exam average (float)
#outputs all the data sorted alphabetically
#average of all scores on exam 1
#average of all scores on exam 2
#one fraction of accuracy
def main(x):
    while True:
        try:
            file_name = str(x)
            file = open(file_name+".txt", "r")

            i=count=0
            names_list = []
            name_list = []
            exam_score = []
            exam_score_1 = []
            exam_score_2 = []
            average_1=0
            average_2=0
            
            for line in file:
                names = line[:20]
                exam_scores = line[21:]
                exam_score.append(exam_scores.split())
                names = names.strip()
                names_list.append(names)
                count+=1
            for score1 in exam_score:
                exam_score_1.append(exam_score[i][0])
                i+=1
            i=0
            for score2 in exam_score:
                exam_score_2.append(exam_score[i][1])
                i+=1
            for x in range(i):
                name = (names_list[x], exam_score_1[x], exam_score_2[x])
                name_list.append(name)
            name_list.sort()
            for data in name_list:
                print(data)
            for average1 in exam_score_1:
                average_1 += int(average1)
            for average2 in exam_score_2:
                average_2 += int(average2)
            average1 = average_1/count
            average2 = average_2/count
            average1 = round(average1,1)
            average2 = round(average2,1)
            print("average score for exam 1: ", average1)
            print("average score for exam 2: ", average2)
            
            file.close()
            break
        except FileNotFoundError:
            print("error")
main("scores(08)")
