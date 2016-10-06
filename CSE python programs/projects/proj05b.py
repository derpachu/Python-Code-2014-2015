#ask for the input file name
    #will continue to prompt until a vlad name is given
#smallest mmr
#largest mmr
#nation rate
#michigan rate
#average rate
while True: #infinitly repeats until the break statment
    try:
        input_file_name = str(input("What is the name of the file? "))
        input_file = open (input_file_name, "r") #reads in the file

        total = mmr_add = 0 #sets constants in variables
        highest = 0.0
        lowest = 100.0
    
        for line in input_file: #scans every line
            if line[:10] == "          ":
                continue #deletes the first line
            country = str(line[:22].strip())
            mmr = float(line[67:71].strip())
            mmr_error = line[72:76].strip()
            #finds all important info and takes out spaces
            if mmr > highest: #checks if the score is higher than previous
                highest_country = country
                highest = mmr
                highest_error = mmr_error #records all info
            if mmr < lowest: #repeats with respect to lower
                lowest_country = country
                lowest = mmr
                lowest_error = mmr_error
            if "Michigan" in str(line): #finds Michigan
                michigan_stat = mmr
                michigan_error = mmr_error #records stats
            if "U.S. National" in str(line): #finds National
                US_national_stat = mmr
                US_national_stat_error = mmr_error #records stats
            mmr_add += mmr
            total += 1 #calculations 
        average = mmr_add/total #calculates average
        templete = "country with the {} rate: "
        print(templete.format("highest"),highest_country,"at",\
              highest,"+",highest_error)
        print(templete.format("lowest"),lowest_country,"at",\
              lowest,"+",lowest_error)
        print("Michigan's rate is:",michigan_stat,"+",michigan_error)
        print("National rate is:",US_national_stat,"+",\
              US_national_stat_error)
        print("Average rate is:",round(average,1)) #all the print statments

        input_file.close()
        break #if it is successful breaks the repeat

    except FileNotFoundError:
        print("Invalid Input (did you add the .txt?)") #just error text
