def editDistance(S1, S2):   #Method for finding the minimum number of operations required to convert one string into another
    d = [[0 for x in range(len(S2)+1)] for y in range(len(S1)+1)]
    print(d)
    for i in range(len(S1)+1):          #Creating the first ROW in the array from 0 to the length of the word S2
        d[i][0] = i
    for j in range(len(S2)+1):          #Creating the first COLUMN in the array from 0 to the length of the word
        d[0][j] = j
    print(d)
    for j in range(len(S2)):
        for i in range(len(S1)):
            if S1[i] == S2[j]:      #Comparing the characters in each of the words with each other
                d[i+1][j+1] = d[i][j]
            else:                   #If the character are not equal, take the smallest value +1
                d[i+1][j+1] = 1 + min(d[i][j+1], d[i+1][j], d[i][j])
    print(d, "\n")
    c = d[len(S1)][len(S2)]
    S = []
    i = (len(S1)-1)
    j = (len(S2)-1)
    print_ED_array(d, S1, S2)

    while c > 0:
        if S1[i] == S2[j]:
            i -= 1
            j -= 1
        else:
            c -= 1
            A = [d[i][j+1], d[i+1][j], d[i][j]]
            m = minInd(A)
            if m == 0:
                S.append("Delete: " + S1[i])
                i -= 1
            else:
                if m == 1:
                    S.append("Insert: " + S2[j])
                    j -= 1
                else:
                    S.append( "Replace: " + S1[i] + " by " + S2[j])
                    i -= 1
                    j -= 1
    print("To convert ", S1, " into ", S2)
    for k in range(len(S)):
        print(S[k])

    return d[len(S1)][len(S2)]


def print_ED_array(d ,S1 , S2): #Method for printing the edit Distance array
    S1 = "" + S1
    S2 = "" + S2
    print("Edit distance Matrix:")
    for i in range(len(S2)):
        print(" ", end=S2[i])
    print()
    for i in range(len(S1)):
        print(S1[i], end=" ")
        for j in range(len(d[i])):
            print(d[i][j], end=" ")
        print()
    print()


def minInd(A):
    smallest = 0
    for i in range(1, len(A)):
        if A[i] < A[smallest]:
            smallest = i
    return smallest


def display_menu():        #   Method for displaying the mennu

    global count
    menu = {}
    menu['1'] = "HARD-CODED"
    menu['2'] = "READING FILE"
    menu['3'] = "INPUT YOUR OWN WORDS!"
    menu['4'] = "Exit"
    while True:
        options = menu.keys()

        for entry in options:
            print(entry, ".- ", menu[entry])
        selection = input("Please Select:")
        if selection == '1':
            while True:
                S1 = "DOG"
                S2 = "PUG"
                d = editDistance(S1, S2)
                print("\nEdit Distance: ", S1, " to ", S2, " = ", d)
                selection = input("Press 0 to go back to the menu: ")
                if selection == '0':
                    break
                else:
                    print("Unknown Option Selected!")
        elif selection == '2':
            while True:
                words_file = open("words", "r")
                words_list = words_file.read().split("\n")
                S1 = words_list[0]
                S2 = words_list[1]
                d = editDistance(S1,S2)
                print("\nEdit Distance: ", S1, " to ", S2, " = ", d)
                selection = input("Press 0 to go back to the menu: ")
                if selection == '0':
                    break
                else:
                    print("Unknown Option Selected!")
        elif selection == '3':
            while True:
                S1 = input("Enter the first word: ")
                S2 = input("Enter the second word: ")
                d = editDistance(S1, S2)
                print("\nEdit Distance: ", S1, " to ", S2, " = ", d)
                selection = input("Press 0 to go back to the menu: ")
                if selection == '0':
                    break
                else:
                    print("Unknown Option Selected!")
        elif selection == '4':
            print("Bye")
            break
        else:
            print("Unknown Option Selected!")



if __name__ == '__main__':
    display_menu()
