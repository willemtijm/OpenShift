'''
Created on Sep 30, 2020

@author: willem
'''
#importeren
import time
import random

#hoe heet je
print ()
naam = input ('Hoe heet je? ')
print ()
print ('Hello,', naam,'tijd om galgje te spelen ')
print ()

#welke woorden ga je gebruiken
woorden = ["strand", "zand", "stoel", "zee", "vakantie", "zomer", "python","wijn", "ijsje", "barbeque", "boek", "zon", "zwemmen", "uitrusten"]
galg = [
  "---------",
  "|       |",
  "|       O",
  "|       |",
  "|      -+-",
  "|       |",
  "|      / \\",
  "|",
  "|",
  "------------"
]
#wait for 1 second
time.sleep(1)

print ('We gaan beginnen ...')
time.sleep(0.5)
#het geheime woord wordt nu gehaald uit de lijst boven
woordkiezen = random.choice(woorden) ##kijk in de lijst bovenin
woord = (woordkiezen)   ##kies het woord
# print (woord) #laat bij het testen het woord zien

#maakt een lege variabele
guesses = ''

#je krijgt 10 kansen
turns = 10

#maakt een loop
#Kijkt hoeveel keer nog
while turns > 0:         

    #begin bij 0
    letters_not_guesed = 0             
    toonwoord=''

    #voor ieder karacter in het woord
    for char in woord:      

    #kijk of het karakter in het woord zit
        if char in guesses:    
    
        #laat het karakter zien
            toonwoord=toonwoord + (char)    

        else:
    
        #als het karakter er niet in zit, zet een streepje
            toonwoord=toonwoord + ('_')     
       
        #aantal keer mis + 1
            letters_not_guesed += 1    

    print ('Woord:',toonwoord, '. Al gegokte letters:', guesses)
    print () # emtpy line

    #als fail is gelijk aan 0
    #Je hebt gewonnen
    if letters_not_guesed == 0:
        print ()
        print ('...')
        #wait for 1 second
        time.sleep(1)        
        print ('Hoera,', naam, 'Je hebt gewonnen')

    # exit
        break              

    print

    #raad een letter
    #wait for 1 second
    time.sleep(1)   
    guess = input ('Raad een letter: ') 

    #zet het aantal keer gokken 
    guesses += guess                    

    #als het niet is gevonden in het woord
    if guess not in woord:  
 
     #Er gaat er steeds 1 af
        turns -= 1        

        # teken galg
        galgregel=turns
        nr_of_to_print_lines=(10-turns)
        while nr_of_to_print_lines>0:
          print (galg[galgregel])
          galgregel +=1 
          nr_of_to_print_lines -=1
        print ("")

    # print fout
        print ('Jammer, fout ...')
 
    #hoeveel keer nog
        print (naam, 'je hebt nog', + turns, 'levens') 

    #zet aantal keer naar 0
        if turns == 0:           
    
        # print je hebt verloren, 
            print ()
            print ('...')
            #wait for 1 second
            time.sleep(1)   
            print ('Jammer', naam, 'je hebt verloren, het woord was:', woord)