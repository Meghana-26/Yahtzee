from random import randint

# Instructions to player

print("The Scores for each category : \n")
print("1.Upper Section :\n-->Ones(1): Score will be sum of all one's\n-->Twos(2): Score will be sum of all two's\n-->Threes(3): Score will be sum of all three's\n-->Fours(4): Score will be sum of all four's\n-->Fives(5): Score will be sum of all five's\n-->Sixs(6): Score will be sum of all six's\n-->Bonous : (If the total score of the upper part is greater or equal to 63)\nBonus of be 35 points is added.\n")
print("2.Lower Section :\n-->3 of a kind(3x): (if the dice show at least 3 of the same number)\nScore will be total of all dices\n-->4 of a kind(4x): (if the dice show at least 4 of the same number)\nScore will be total of all dices\n-->Full House(f): (if 3 dices show the same number and other two should show same number)\nScore will be 25 points\n-->Small Straight(ss): (if any sequence of four numbers)\nScore will be 30 points\n-->Large Straight(ls): (if any sequence of five numbers)\nScore will be 40 points\n-->YAHTZEE(y): (if 5 are same number)\nScore will be 50 points\n-->Chance(c): \nScore will be total of all dices\n-->Yahtzee Bonus(yb): (From the 2nd Yahtzee in the same game)\nBonus of 100 points are added for each Yahtzee.\n")

# Rolling of Dices

def roll1():
    dice = []
    for _ in range(5):
        dice.append(randint(1,6))
    return dice
    
def roll():
    return randint(1,6)
    
def display_values_on_dice(dice):
    for die in dice:
        print(str(die) + ' ', end="")
    print("\n")
   
    
#upper section functions

def ones(dice):
    total = sum([num for num in dice if num == 1])
    return total
    

def twos(dice):
    total = sum([num for num in dice if num == 2])
    return total
 
    
def threes(dice):
    total = sum([num for num in dice if num == 3])
    return total

   
def fours(dice):
    total = sum([num for num in dice if num == 4])
    return total

    
def fives(dice):
    total = sum([num for num in dice if num == 5])
    return total
    
def sixes(dice):
    total = sum([num for num in dice if num == 6])
    return total
      
#lower section functions
    
def three_of_a_kind(dice):
    total = sum(dice) 
    if(four_of_a_kind(dice)) :
        return total
    else:
        dice.sort()
        if (len(set(dice)) == 3 ) and (dice[0] == dice[2] or dice[1] == dice[3] or dice[2] == dice[4]):
            return total
        return 0
    
def four_of_a_kind(dice):
    total = sum(dice)
    dice.sort()
    if dice[0] == dice[3] or dice[1] == dice[4]:
        return total
    return 0
    
def small_straight(dice):
    dice = list(set(dice))
    dice.sort()
    string = "".join(list(map(str, dice)))
    if( "1234" in string or "2345" in string or "3456" in string):
        return 30
    
    return 0

def large_straight(dice):
    dice.sort()
    string = "".join(list(map(str, dice)))
    if(string == "12345" or string == "23456"):
        return 40
    return 0
   
def full_house(dice):
    dice.sort()
    if (len(set(dice))) != 2:
        return 0
    else:
        if(dice.count(dice[0]) == 2 or dice.count(dice[0])== 3):
            return 25
        return 0

def chance(dice):
    total = sum(dice)
    return total

def check_yahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    return 0


 # function for reroll

def reroll(dice):
    positions = list(map(int, input("What are the positions of dice you want to reroll: ").strip().split(" ")))[:]
    for i in positions:
        dice[i-1] = roll()
    print("After reroll the dice are: ")
    display_values_on_dice(dice)

def final_score(player):
    upper_score = 0
    lower_score = 0
    for key in score_board[player]:
        if key in ["1","2","3","4","5","6"]:
            upper_score += score_board[player][key]
        else:
            lower_score += score_board[player][key]
    if(upper_score >= 63):
        upper_score += 35
    total_score = upper_score + lower_score
    return total_score

def winner(scores_of_all_players):
    sorted_dict = {dict_key: dict_value for dict_key, dict_value in sorted(scores_of_all_players.items(), key=lambda item: item[1], reverse = True)}
    score_list = sorted(list(scores_of_all_players.values()))
    winner_count = score_list.count(score_list[0])
    i = 0
    print("Winners are: ")
    for key in sorted_dict:
        if(i < winner_count):
            print(key)
            i += 1
        else:
            break

    
def score(choice, dice):
    choice_list = {
    "1"   : ones(dice),
    "2"   : twos(dice),
    "3"   : threes(dice),
    "4"   : fours(dice),
    "5"   : fives(dice),
    "6"   : sixes(dice),
    "3x"  : three_of_a_kind(dice),
    "4x"  : four_of_a_kind(dice),
    "ss"  : small_straight(dice),
    "ls"  : large_straight(dice),
    "f"   : full_house(dice),
    "y"   : check_yahtzee(dice),
    "c"   : chance(dice)
    }
    return choice_list[choice]


    
#score_board = {bindu:{c:35, 1:3,... }, ....}

def rolling(name, turn):
    bonus = 0
    print("\n")
    print(f"Its {name}'s -----------> turn{turn+1}")
    roll_values = roll1()
    print("The values on 5 dice in first roll are: ")
    display_values_on_dice(roll_values)
    option = input("Do you want to reroll (y/n/q): ")
    if option == "q":
        quit()
    while(option != "y" and option != "n"):
        print("Incorrect option!!!")
        option = input("Do you want to reroll (y/n/q): ")
    if(option == "q"):
        quit()
    if(option == "y"):
        reroll(roll_values)
        option = input("Do you want to reroll(y/n/q): ")
        if option == "q":
            quit()
        while(option != "y" and option != "n"):
            print("Incorrect option!!!")
            option = input("Do you want to reroll (y/n/q): ")
        if (option == "q"):
            quit()
        if(option == "y"):
            reroll(roll_values)
            choice = input("Select the category to store in your scoreboard: ")
            while((choice not in selection_list)):
                choice = input("Chose wrong, Enter category: ")
            while(choice in score_board[name]):
                if( choice == 'y'):
                    bonus += 100
                else:
                    print("This is already chosen")
                    choice = input("Select another category: ")
            if(choice == 'y'):
                score_board[name][choice] = score(choice, roll_values) + bonus
            else:
                score_board[name][choice] = score(choice, roll_values)
        else:
            choice = input("Select the category to store in your scoreboard: ")
            while(choice not in selection_list):
                choice = input("Chose wrong, Enter category : ")
            while (choice in score_board[name]):
                if(choice == 'y'):
                    bonus += 100
                else:
                    print("This is already chosen")
                    choice = input("Select another category: ")
            if(choice == 'y'):
                score_board[name][choice] = score(choice, roll_values) + bonus
            else:
                score_board[name][choice] = score(choice, roll_values)
    else:
        choice = input("Select the category to store in your scoreboard: ")
        while((choice not in selection_list)):
            choice = input("Chose wrong, Enter category: ")
        while(choice in score_board[name]):
            if(choice == 'y'):
                bonus += 100
            else:
                print("This is already chosen")
                choice = input("Select another category: ")
        if(choice == 'y'):
            score_board[name][choice] = score(choice, roll_values) + bonus
        else:
            score_board[name][choice] = score(choice, roll_values)


def game(num_of_players):
    players = list(map(str, input(f"Enter names of {num_of_players} players: ").strip().split(" ")))[:]
    while(len(players) != num_of_players):
        players.extend(list(map(str, input("Enter names of other players: ").strip().split(" ")))[:])
    for player in players:
        score_board[player] = {}
    for turn_count in range(13):
        for player in players:
            rolling(player, turn_count)
        print(score_board)
    scores_of_all_players = {}
    for player in players:
        scores_of_all_players[player] = final_score(player)
    print("Final Scores of all players : ",scores_of_all_players) 
    winner(scores_of_all_players)  
    
selection_list = ["1","2","3","4","5","6","3x","4x","ss","ls","c","y","yb","f"]
num_of_players = int(input("Enter number of players: "))
score_board = {}
game(num_of_players)
