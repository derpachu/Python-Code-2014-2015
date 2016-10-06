#0 terminates
#ignores negatives
#count odd
#count even
#count negatives
#count total
#sum of odd
#sum of even
#display the sums
#display the count

odd=even=neg=tot=sum1=sum2=0

a = int(input("Input an integer (0 terminates): "))

while a != 0:
    if a%2 == 0 and a>0:
        sum2 += a
        even += 1
        tot +=1
    elif a%2 != 0 and a>0:
        sum1 += a
        odd +=1
        tot +=1
    elif a<0:
        neg +=1
    a = int(input("Input an integer (0 terminates): "))

print ("Sum of odds: ", sum1)
print ("Sum of evens: ", sum2)
print ("odd count: ", odd)
print ("even count: ", even)
print ("total positive int count: ", tot)
print ("total negative int count: ", neg)
