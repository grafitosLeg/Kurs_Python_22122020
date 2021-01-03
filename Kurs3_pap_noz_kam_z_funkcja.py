#Gra papier, nozyczki, kamien z użyciem funcji - kod z głowy

#definicja graczy  - ustalamy licznik na 0

gracz1_wynik = 0
gracz2_wynik = 0

#definicja opcji z których gracze będą korzystać przy wyborze

opcje = ['kamien', 'nozyczki','papier']

#definicja funkcji pobierz wybór gracza 

def pobierz_wybor (gracz):
   while True:
       wybor_Gracz = input (f'{gracz} podaj wybor:   ')
       if wybor_Gracz in opcje:
          return wybor_Gracz 


#definicja funkcji w której sprawdzamy wyniki 

def sprawdz_wyniki (wybor_gracz1,wybor_gracz2):
    if wybor_gracz1 == 'papier' and wybor_gracz2 == 'kamien'\
    or wybor_gracz1 == 'nozyczki' and wybor_gracz2 == 'papier'\
    or wybor_gracz1 == 'kamien' and wybor_gracz2 == 'nozyczki':
        print ('Wygrał Gracz 1')
        return 1 
    
    elif wybor_gracz2 == wybor_gracz2:
        print ('REMIS')
        return 0    
    else:
         print ('Wygrał Gracz 2')
         return -1
    

#uruchamiamy funkcje
#gramy dopóki któryś z graczy nie wygra 3razy

while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_gracz1 = pobierz_wybor ('Gracz1')
    wybor_gracz2 = pobierz_wybor ('Gracz2')
    wynik = sprawdz_wyniki (wybor_gracz1, wybor_gracz2)



