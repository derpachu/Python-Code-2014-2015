#project 08
#build a system where people can manage employees and their data
#dependant on prefixes
#takes a list of commands from the transaction file
#reads the old tile
#outputs to the new file after all transactions have taken place
#REMEMBER TO MAKE THE LINES SHORTER TO FIT CODING STANDARD 79

def build_list(file):
    """ input: file to get all the employees
        output: dictionary of all employees and info"""
    dictionary = {}
    for line in file:#goes through every line removing formatting and adding
        #things into a dictionary with employee ID as the key
        edited_line = line.strip().split()
        print(edited_line)
        if len(edited_line) == 5:
            name = edited_line[3]+" "+edited_line[4]
        if len(edited_line) == 6:
            name = edited_line[3]+" "+edited_line[4]+" "+edited_line[5]
        dictionary[int(edited_line[0])] = [name, edited_line[2], \
                                           edited_line[1]]
    return dictionary

def report_by_number(dictionary, out_file):
    """ input: dictionary, file to write to
        output: none (executed for side effect)"""
    sorted_dictionary = sorted(dictionary)#sorts the dictionary into a list
    template = "{:5}   {:20}       {:15}  {}"#formats it
    print(template.format("ID", "name", "department", "salary"), \
          file = out_file)#headers
    for key in sorted_dictionary:#prints every entry in the list into the template
        print(template.format(key, dictionary[key][0], dictionary[key][2], \
                              dictionary[key][1]), file = out_file)
        
def report_by_name(dictionary, out_file):
    """ inputs: dictionary and the file to be printed to
        outputs: none executed for side effect)"""
    main_list = []
    for key in dictionary:#creates a list that swaps the ID and the Name
        #position into a list
        secondary_list = []
        for entry in dictionary[key]:#puts the list of entries into the
            #larger list
            secondary_list.append(entry)
        secondary_list.append(key)
        main_list.append(secondary_list)
    sorted_list = sorted(main_list)#sortes everything
    template = "{:20}   {:5}       {:15}  {}"
    print(template.format("name", "ID", "department", "salary"), \
          file = out_file)#same as above
    for name in sorted_list:
        print(template.format(name[0], name[1], name[2], name[3]), \
              file = out_file)#prints with correct formatting
def update_department(dictionary, ID_number, new_department):
    """ inputs: the dictionary to be modified, the employee ID to be \
modified, and the new department number
        outputs: none (executed for side effect)"""
    dictionary[ID_number][2] = new_department #just reassigns the given value
    #into the list, nothing returned
    
def update_salary(dictionary, ID_number, new_salary):
    """ inputs: the dictionary to be modified, the employee ID to be modified,\
and the new salary
        outputs: none (executed for side effect)"""
    dictionary[ID_number][1] = new_salary #same above only with the salary
    #value
    
def remove_employee(dictionary, ID_number):
    """ inputs: dictionary, employee ID to be removed
        outputs: none (executed for side effect)"""
    del dictionary[ID_number] #deletes the given entry
    
def insert_employee(dictionary, ID_number, department, salary, name):
    """ inputs: dictionary to be modified, ID of new employee, new ID, \
New department, salary, and name
        output: none (executed for side effect)"""
    dictionary[ID_number] = [name, salary, department] #just addes a new entry
    #into the dictionary

def menu_selection(file, dictionary, report_file):
    """ input: transaction file
        output: none (executed for side effect)"""
    for line in file:#reades the line in the file
        try:#checks to make sure that the command in valid
            line = line.strip("\n") #removes the main formatting
            selection = line[:6] #reads the first word and makes a decsion
            #based on that word
            if selection == "report":#two options from this word
                report = line[10:14]
                if report == "name":
                    report_by_name(dictionary, report_file)#each entry is
                    #called based on key words
                elif report == "numb":
                    report_by_number(dictionary, report_file)
                else:#if something is misspelled after report, shows a message
                    #and moves on
                     print("error: invalid report")
                     continue
            elif selection == "update":#two options from this word
                update = line[7:11]
                if update == "sala":
                    ID = int(line[15:20])#every function call after this uses
                    #string slicing to get the values needed in the function
                    salary = int(line[22:])
                    update_salary(dictionary, ID, salary)
                elif update == "depa":
                    ID = int(line[19:24])
                    new_depart = line[26:28]
                    update_department(dictionary, ID, new_depart)
                else:#if something is misspelled after update, shows a message
                    #and moves on
                    print("error: invalud update")
                    continue
            elif selection == "remove":#only one option from this word
                ID = int(line[17:22])
                remove_employee(dictionary,ID)
            elif selection == "insert":#only one option from this word
                ID = int(line[17:22])
                depart = int(line[23:26])
                salary = int(line[27:33])
                name = line[35:]
                insert_employee(dictionary, ID, depart, salary, name)
            else:#if something is misspelled for the first word, shows a
                #message and moves on
                print("error: invalid first word")
                continue
        except ValueError:#if there is too many spaces then shows this error
            print("error: too many spaces somewhere")
            continue
        
            
    
def main():
    """ calls everything in order
        inputs: None
        outputs: None (executed for side effect)"""
    try:
        file_prefix = str(input("prefix: "))#gets the correct prefix
        in_file = open(file_prefix+".employees.old.txt", "r")#opens nesccessary
        #files and creates the ones to output the data into
        out_file = open(file_prefix+".employees.new.txt", "w")
        report_file = open(file_prefix+".report.txt", "w")
        command_file = open(file_prefix+".transactions.txt", "r")
        data = build_list(in_file)#creates the dictionary of all employees
        #with the info
        menu_selection(command_file, data, report_file)#reads through the
        #transaction and executes the correct funciton
        for entry in data:
            print(entry, data[entry], file = out_file)#prints out the finished
            #dictionary into the new file
        in_file.close()#closes all files
        out_file.close()
        report_file.close()
        command_file.close()
    except FileNotFoundError:
        print("Original employee file doesnt exist.")
    
main()
