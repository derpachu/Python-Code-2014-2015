#project reads the geographic area and the mmr data
#   [:22] [67:72] [73:76]
#always reads from that file if it doesnt exist the project halts
#will ask for output file if it doesnt exist it is created
#   if it does exist then it will over right
#must contain the error rate
try:
    input_file = open("project05.data.txt", "r")
    output_file_name = str(input("Enter the Name of the Output File: "))
    output_file = open(output_file_name+".txt", "w")
    #opens all the files and finds the name

    for line in input_file:
        if line[:10] == "          ":
            continue #skips the first line
        country = str(line[:22].strip()) #assigns all the countries into it
        mmr = str(line[67:76].strip()) #records the mmr at that spot
        templete = "geography: {:22} mmr: {:6}"
        print(templete.format(country, mmr), file=output_file)

    input_file.close()
    output_file.close()
except FileNotFoundError:
    print("program halt") #kills the program if the input file is missing
