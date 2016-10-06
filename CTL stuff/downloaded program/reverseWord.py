# Find the reverse of a word by the following algorithm:
#
# Step 0: Request a string value from a user and assign it to variable word
# Step 1: Assign the length of this string to variable n 
# Step 2: Assign the empty string to variable result
# Step 2: Repeat n times:
#    Sub-step (i): Add the last character of word to the end of result
#    Sub-step (ii): Drop the last character in word
# Step 4: Print the value of result
#

# Modify your program so that it prints both the original word and the
# reverse of the word, appropriately labelled, and both on the same line

input1 = original = input ("Enter a String: ")
n = len(input1)
counter = 0
result = ""
while counter < n:
    result += input1[-1]
    input1 = input1[:-1]
    counter += 1
print(original + result)
