#This program employs the game of tic-tac-toe
#Without using any imported modules
#Except time, for better execution effect


import time
print("Welcome to Tic-tac-toe!\n")
print("The spot numbering has been done as follows: \n") #Spot Numbering Nomenclature
print("1  |  2  |  3")
print("---|-----|---")
print("4  |  5  |  6")
print("---|-----|---")
print("7  |  8  |  9")
time.sleep(1)

print("The game starts: ")
ListStoredValues = [0,0,0,0,0,0,0,0,0]

def NumberToSymbol(number):
    if number == 0:
        return " "
    elif number == 1:
        return "X"
    elif number == -1:
        return "O"



def ShowTable():
    print(f"{NumberToSymbol(ListStoredValues[0])}  |  {NumberToSymbol(ListStoredValues[1])}  |  {NumberToSymbol(ListStoredValues[2])}")
    print("---|-----|---")
    print(f"{NumberToSymbol(ListStoredValues[3])}  |  {NumberToSymbol(ListStoredValues[4])}  |  {NumberToSymbol(ListStoredValues[5])}")
    print("---|-----|---")
    print(f"{NumberToSymbol(ListStoredValues[6])}  |  {NumberToSymbol(ListStoredValues[7])}  |  {NumberToSymbol(ListStoredValues[8])}")

def showPossibleSpots():
    PossibleSpots = []
    for i in range(len(ListStoredValues)):
        if ListStoredValues[i] == 0:
            PossibleSpots.append(i+1)
    return PossibleSpots



while True:
    #Execution of X takes place first
    print("\nIt is X's turn")
    while True:
        position = int(input(f"Enter the position, among the following given, at which you want to enter {showPossibleSpots()}: "))
        if position in showPossibleSpots():
            break
        print("Enter correct number!")
    
    ListStoredValues[position - 1] = 1
    ShowTable()
    time.sleep(1)

    #Execution of O takes place now
    print("\nIt is O's turn")
    while True:
        position = int(input(f"Enter the position, among the following given, at which you want to enter {showPossibleSpots()}: "))
        if position in showPossibleSpots():
            break
    
    ListStoredValues[position - 1] = -1
    ShowTable()
    time.sleep(1)

    if (ListStoredValues[0] == ListStoredValues[1] == ListStoredValues[2] == 1) or (ListStoredValues[3] == ListStoredValues[4] == ListStoredValues[5] == 1)\
    or (ListStoredValues[6] == ListStoredValues[7] == ListStoredValues[8] == 1) or (ListStoredValues[0] == ListStoredValues[4] == ListStoredValues[8] == 1)\
    or (ListStoredValues[0] == ListStoredValues[3] == ListStoredValues[6] == 1) or (ListStoredValues[1] == ListStoredValues[4] == ListStoredValues[7] == 1)\
    or (ListStoredValues[2] == ListStoredValues[5] == ListStoredValues[8] == 1) or (ListStoredValues[2] == ListStoredValues[4] == ListStoredValues[6] == 1):
        print("\nX WINS!")
        print("\nThank You for playing the game!")
        break

    if (ListStoredValues[0] == ListStoredValues[1] == ListStoredValues[2] == -1) or (ListStoredValues[3] == ListStoredValues[4] == ListStoredValues[5] == -1)\
    or (ListStoredValues[6] == ListStoredValues[7] == ListStoredValues[8] == -1) or (ListStoredValues[0] == ListStoredValues[4] == ListStoredValues[8] == -1)\
    or (ListStoredValues[0] == ListStoredValues[3] == ListStoredValues[6] == -1) or (ListStoredValues[1] == ListStoredValues[4] == ListStoredValues[7] == -1)\
    or (ListStoredValues[2] == ListStoredValues[5] == ListStoredValues[8] == -1) or (ListStoredValues[2] == ListStoredValues[4] == ListStoredValues[6] == -1):
        print("\nO WINS!")
        print("\nThank You for playing the game!")
        break



    if showPossibleSpots == []:
        print("\nIT IS A TIE!")
        print("\nThank You for playing the game!")
        break
        



