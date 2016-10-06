txt_file = open("text.txt")
out_file = open("newtext.txt","w")

for line in txt_file:
    for x in ":[":
        if x == ":":
            print(line,file=out_file,end="\n")
        elif x == "[":
            print(line,file=out_file,end="\n")

txt_file.close()
out_file.close()
