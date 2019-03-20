import random
import time

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board):
    board=('','|1        ','|2       ','|3       |', \
       '|4        ','|5       ','|6       |', \
       '|7        ','|8       ','|9       |' )


    print('+---------------------------+')
    print(board[7]+board[8]+board[9])
    print('|         |        |        |')
    print('|         |        |        |')
    print('+---------------------------+')
    print(board[4]+board[5]+board[6])
    print('|         |        |        |')
    print('|         |        |        |')
    print('+---------------------------+')
    print(board[1]+board[2]+board[3])
    print('|         |        |        |')
    print('|         |        |        |')
    print('+---------------------------+')

 
    #εμφάνισε την κατάσταση της τρίλιζας
     

def choose_first():
     
    x=random.randint(1,2)
    if x==1:
     return('Παίκτης 1')
    elif x==2:
     return('Παίκτης 2')
    #κλήρωση για το ποιος θα παίξει πρώτος
    # επιστρέφει είτε 'Παίκτης 1' είτε 'Παίκτης 2'
    

def display_score(score):
     print('Το τελικό score είναι:')
     print("Παίκτης 1:",score)
     print("Παίκτης 2:",score)
    #Τυπώνει το τελικό σκορ
    

def place_marker(board, marker, position):
     board=[1 for x in board[position] if marker=='X']    
     board=[1 for x in board[position] if marker=='O']      
     pass
    #Τοποθετεί στη θέση position του board τον marker
    
def win_check(board,mark): 
    #επιστρέφει True αν το σύμβολο mark έχει σχηματίσει τρίλιζα
    pass

def board_check(board):
    #επιστρέφει False αν υπάρχουν ακόμη κενά τετράγωνα
    #και True στην αντίθετη περίπτωση.
    pass 
 
def player_choice(board, turn):
     position=input('Ποια θέση επιλέγεις από 1 έως 9;')
     return position
    #Ο Παίκτης turn επιλέγει τετράγωνο
    #Επιστρέφει έναν ακέραιο στο διάστημα [1,9]
    #Εδώ θα γίνει και ο έλεγχος αν υπάρχει ήδη τιμή μέσα στο τετράγωνο
    

def replay(): 
    y=input('Θα ξαναπαίξουμε; ΝΑΙ ή ΟΧΙ')
    if y==ΝΑΙ:
        return True
    elif y==ΟΧΙ:
        return False
    else:
        y=input('Απάντησε με NAI ή ΟΧΙ')
  # Ρωτάει τον χρήστη αν θέλει να ξαναπαίξει και επιστρέφει True αν ναι.

def next_player(turn):
    if turn=='Παίκτης 1':
         return ('Παίκτης 2')
    else:
          return ('Παίκτης 1')
    
    #επιστρέφει τον επόμενο παίκτη που πρέπει να παίξει
    
def main():
    score = {"Παίκτης 1": 0, "Παίκτης 2":0} # λεξικό με το σκορ των παικτών
    print('Αρχίζουμε!\nΓίνεται κλήρωση ', end = '')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    # η μεταβλητή turn αναφέρεται στον παίκτη που παίζει
    turn = choose_first() 
    print("\nΟ " + turn + ' παίζει πρώτος.')
    # η μεταβλητή first αναφέρεται στον παίκτη που έπαιξε πρώτος
    first = turn 
    game_round = 1 # γύρος παιχνιδιού
    while True:
        # Καινούργιο παιχνίδι
        # Δημιουργία λίστας 10 στοιχείων βλέπε μάθημα 2 σελ.7 σημειώσεων
        theBoard = [' '] * 10 
        # Αφήστε το πρώτο στοιχείο δηλαδή το theBoard[0] κενό έτσι ώστε 
        # το index να αντιστοιχεί στην ονοματοδότηση των τετραγώνων 
        game_on = True  #ξεκινάει το παιχνίδι
        while game_on:
            display_board(theBoard) #Εμφάνισε την τρίλιζα
            # ο παίκτης turn επιλέγει θέση
            position = player_choice(theBoard, turn) 
            # τοποθετείται η επιλογή του
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]): # έλεγχος αν νίκησε
                display_board(theBoard)
                print('Νίκησε ο '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            # έλεγχος αν γέμισε το ταμπλό χωρίς νικητή
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else: # αλλιώς συνεχίζουμε με την κίνηση του επόμενου παίκτη
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            turn = next_player(first) 
            first = turn
main()
