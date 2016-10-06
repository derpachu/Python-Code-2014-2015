maxm = -1
num = 0
avg = float(0)
total  = 0
score_str = input("Enter score number " + str(num) \
                  + " (or a negative score to terminate): ")
score = int(score_str)

while score > 0:
    if score > maxm:
        maxm = score
    print("Maximum score so far:", maxm)
    
    num += 1
    total += score
    score_str = input("Enter score number " + str(num) \
                      + " (or a negative score to terminate): ")
    score = int(score_str)
    

avg = total/num
print("\nThe maximum score:", maxm)
print("\nThe number of scores:", num)
print("\nThe average is:", avg)
