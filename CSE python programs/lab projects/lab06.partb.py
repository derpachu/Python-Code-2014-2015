NewFile = str(input("Enter name of the file and text: "))
x=0
Title=NewInput=FinalText=""
while NewInput != ".":
    NewInput = str(input())
    if NewInput != ".":
        if x==0:
            Title = NewFile
            Title = Title+".txt"
        x=x+1
        FinalText = FinalText+NewInput

new_file = open(Title, "w")
print(FinalText, file=new_file)
new_file.close()
