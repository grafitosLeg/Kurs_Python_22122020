#Gra papier, nozyczki, kamien
#import getpass  - maskowanie inputa

import getpass

gracz1_wynik = 0
gracz2_wynik = 0

opcje = ['kamien', 'papier', 'nozyczki']

#gra jest rozgrywana do 3 wygranych rozgrywek przez dowolnego gracza
#włączona logika poprawności wprowadzonego inputa

while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_gracza_jest_poprawny = True
    while wybor_gracza_jest_poprawny:
      wybor_Gracz1 = getpass.getpass('Gracz 1 podaj wybor: ')
      if wybor_Gracz1 in opcje:
         wybor_gracza_jest_poprawny = False 

    wybor_gracza_jest_poprawny = True
    while wybor_gracza_jest_poprawny:
      wybor_Gracz2 = input('Gracz 2 podaj wybor: ')
      if wybor_Gracz2 in opcje:
         wybor_gracza_jest_poprawny = False 
    
  
    if wybor_Gracz1 == 'papier' and wybor_Gracz2 == 'kamien'\
    or wybor_Gracz1 == 'kamien' and wybor_Gracz2 == 'nozyczki'\
    or wybor_Gracz1 == 'nozyczki' and wybor_Gracz2 == 'papier':
        print ('Gracz 1 wygrał')
        gracz1_wynik += 1 
    
    #jednakowy wybór == remis
    elif wybor_Gracz1 == wybor_Gracz2:
        print ('Remis')

    else:
      print('Gracz 2 wygrał')
      gracz2_wynik += 1  

if gracz1_wynik > gracz2_wynik:
  print ('Całą grę wygrał Gracz1')
else:
  print ('Całą grę wygrał Gracz2') 