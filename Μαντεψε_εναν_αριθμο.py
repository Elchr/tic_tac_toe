import random
x=random.randint(1,100)
print("--------ΜΑΝΤΕΨΕ ΕΝΑΝ ΑΡΙΘΜΟ--------")
y=int(input('Θέλεις να παίξουμε; Πάτα 1 για να παίξουμε ή 2 για έξοδο.\n'))
tries=0
if y==2:
    print('Bye!')

elif y==1:
    num=0
    while num!=x:
        
        num=(input('Mάντεψε έναν ακέραιο αριθμό 1-100 (ή πάτα 999 για έξοδο):\t'))
        if not num.isdigit():
           print("Λάθος εισαγωγή")
           continue
        else:
            num=int(num)
            if num==999:
                      print("Τέλος παιχνιδιού")
                      break
        
            if num<1 or num>100:
                      print("Πρόσεχε! Ο αριθμός δεν είναι μέσα στα όρια. ")
                      continue
            if num>x:
                      print('OXI είναι μικρότερος')
                      tries=tries+1
                      continue
            if num<x :
                      print('OXI είναι μεγαλύτερος')
                      tries=tries+1
                      continue
        
        
    else: 
        print('\n Το βρήκατε σωστά μετά από {} προσπάθειες.\n'.format(tries+1))
        print('Συγχαρητήρια!!!')
      
           
else:
 print('Εrror. Δοκίμασε πάλι από την αρχή')
    
