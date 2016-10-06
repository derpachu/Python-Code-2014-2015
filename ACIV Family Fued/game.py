def strike1():
    print(
        """xxxxxxxxx               xxxxxxxxx
 xxxxxxxxx             xxxxxxxxx
  xxxxxxxxx           xxxxxxxxx
   xxxxxxxxx         xxxxxxxxx
    xxxxxxxxx       xxxxxxxxx
     xxxxxxxxx     xxxxxxxxx
      xxxxxxxxx   xxxxxxxxx
       xxxxxxxxx xxxxxxxxx
        xxxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxx
       xxxxxxxxx xxxxxxxxx
      xxxxxxxxx   xxxxxxxxx
     xxxxxxxxx     xxxxxxxxx
    xxxxxxxxx       xxxxxxxxx
   xxxxxxxxx         xxxxxxxxx
  xxxxxxxxx           xxxxxxxxx
 xxxxxxxxx             xxxxxxxxx
xxxxxxxxx               xxxxxxxxx""")

def strike2():
    print(
        """xxxxxxxxx               xxxxxxxxxxxxxxxxxx               xxxxxxxxx
 xxxxxxxxx             xxxxxxxxx  xxxxxxxxx             xxxxxxxxx 
  xxxxxxxxx           xxxxxxxxx    xxxxxxxxx           xxxxxxxxx  
   xxxxxxxxx         xxxxxxxxx      xxxxxxxxx         xxxxxxxxx
    xxxxxxxxx       xxxxxxxxx        xxxxxxxxx       xxxxxxxxx    
     xxxxxxxxx     xxxxxxxxx          xxxxxxxxx     xxxxxxxxx     
      xxxxxxxxx   xxxxxxxxx            xxxxxxxxx   xxxxxxxxx      
       xxxxxxxxx xxxxxxxxx              xxxxxxxxx xxxxxxxxx       
        xxxxxxxxxxxxxxxxx                xxxxxxxxxxxxxxxxx        
        xxxxxxxxxxxxxxxxx                xxxxxxxxxxxxxxxxx        
       xxxxxxxxx xxxxxxxxx              xxxxxxxxx xxxxxxxxx       
      xxxxxxxxx   xxxxxxxxx            xxxxxxxxx   xxxxxxxxx      
     xxxxxxxxx     xxxxxxxxx          xxxxxxxxx     xxxxxxxxx      
    xxxxxxxxx       xxxxxxxxx        xxxxxxxxx       xxxxxxxxx     
   xxxxxxxxx         xxxxxxxxx      xxxxxxxxx         xxxxxxxxx    
  xxxxxxxxx           xxxxxxxxx    xxxxxxxxx           xxxxxxxxx  
 xxxxxxxxx             xxxxxxxxx  xxxxxxxxx             xxxxxxxxx 
xxxxxxxxx               xxxxxxxxxxxxxxxxxx               xxxxxxxxx""")

def strike3():
        print(
        """xxxxxxxxx               xxxxxxxxxxxxxxxxxx               xxxxxxxxxxxxxxxxxx               xxxxxxxxx
 xxxxxxxxx             xxxxxxxxx  xxxxxxxxx             xxxxxxxxx  xxxxxxxxx             xxxxxxxxx 
  xxxxxxxxx           xxxxxxxxx    xxxxxxxxx           xxxxxxxxx    xxxxxxxxx           xxxxxxxxx  
   xxxxxxxxx         xxxxxxxxx      xxxxxxxxx         xxxxxxxxx      xxxxxxxxx         xxxxxxxxx   
    xxxxxxxxx       xxxxxxxxx        xxxxxxxxx       xxxxxxxxx        xxxxxxxxx       xxxxxxxxx     
     xxxxxxxxx     xxxxxxxxx          xxxxxxxxx     xxxxxxxxx          xxxxxxxxx     xxxxxxxxx     
      xxxxxxxxx   xxxxxxxxx            xxxxxxxxx   xxxxxxxxx            xxxxxxxxx   xxxxxxxxx      
       xxxxxxxxx xxxxxxxxx              xxxxxxxxx xxxxxxxxx              xxxxxxxxx xxxxxxxxx       
        xxxxxxxxxxxxxxxxx                xxxxxxxxxxxxxxxxx                xxxxxxxxxxxxxxxxx        
        xxxxxxxxxxxxxxxxx                xxxxxxxxxxxxxxxxx                xxxxxxxxxxxxxxxxx        
       xxxxxxxxx xxxxxxxxx              xxxxxxxxx xxxxxxxxx              xxxxxxxxx xxxxxxxxx       
      xxxxxxxxx   xxxxxxxxx            xxxxxxxxx   xxxxxxxxx            xxxxxxxxx   xxxxxxxxx      
     xxxxxxxxx     xxxxxxxxx          xxxxxxxxx     xxxxxxxxx          xxxxxxxxx     xxxxxxxxx     
    xxxxxxxxx       xxxxxxxxx        xxxxxxxxx       xxxxxxxxx        xxxxxxxxx       xxxxxxxxx    
   xxxxxxxxx         xxxxxxxxx      xxxxxxxxx         xxxxxxxxx      xxxxxxxxx         xxxxxxxxx   
  xxxxxxxxx           xxxxxxxxx    xxxxxxxxx           xxxxxxxxx    xxxxxxxxx           xxxxxxxxx  
 xxxxxxxxx             xxxxxxxxx  xxxxxxxxx             xxxxxxxxx  xxxxxxxxx             xxxxxxxxx 
xxxxxxxxx               xxxxxxxxxxxxxxxxxx               xxxxxxxxxxxxxxxxxx               xxxxxxxxx""")

def get_data(file):
    game_data = []
    for line in file:
        entry = []
        if line[0] == "a":
            question = str(line[2:])
            question = question.replace("\n","")
            game_data.append(question)
        else:
            rank = line[0]
            answer = line[2:5]
            pts = int(line[6:8])
            entry.append(rank)
            entry.append(answer)
            entry.append(pts)
            game_data.append(entry)
    return game_data

def display_game(data,display_data):      
    for entry in display_data:
        print(entry)

def game(data,multiplier):
    display_data = []
    answer = []
    val = []
    score = 0
    hidden = "*******"
    for i in range(len(data)-2):
        display_data.append(hidden)
    display_data.append("'best of' (not worth any points)")
    display_data.append(hidden)
    question = data.pop(0)
    print(question)
    display_game(data,display_data)
    for entry in data:
        answer_choice = str(entry[1])
        pt_val = int(entry[2])
        pt_val *= multiplier
        answer.append(answer_choice)
        val.append(pt_val)

    win = 0
    strikes = 0
    while win < len(data)-1:
        guess = str(input("Survey Says(remember the space): "))
        if guess in answer:
            position = answer.index(guess)
            if val[position] == 0:
                display_data.insert(position+1,guess)
                display_data.pop(position+2)
            else:
                display_data.insert(position, guess)
                display_data.pop(position+1)
                score += val[position]
            win += 1
            display_game(data,display_data)
            continue
        else:
            strikes += 1
        if strikes == 1:
            strike1()
        if strikes == 2:
            strike2()
        if strikes == 3:
            strike3()
            print("other team has a chance to steal")
            guess = str(input("Survey Says(remember the space): "))
            if guess in answer:
                position = answer.index(guess)
                if val[position] == 0:
                    display_data.insert(position+1,guess)
                    display_data.pop(position+2)
                else:
                    display_data.insert(position, guess)
                    display_data.pop(position+1)
                    score += val[position]
                display_game(data,display_data)
                break
            else:
                strike1()
                break
    print("score total is: ", score)
    print("round over")

def main():
    num = input("number of games? ")
    if num == str(3):
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,1)
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,2)
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,3)
    if num == str(5):
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,1)
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,1)
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,1)
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,2)
        file_name = str(input("which question "))+".txt"
        file = open(file_name, "r")
        data = get_data(file)
        game(data,5)

main()
