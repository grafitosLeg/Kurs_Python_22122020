#Gra papier, nozyczki, kamien z użyciem funcji i słownika

from time import sleep
print ("Gra Papier, Kamien, Nożyczki")
sleep(3)

gracz1_wynik = 0
gracz2_wynik = 0

opcje = ['kamien', 'papier', 'nozyczki']

#gra jest rozgrywana do 3 wygranych rozgrywek przez dowolnego gracza
#włączona logika poprawności wprowadzonego inputa

#funkcja pobierająca wybór od graczy 
def pobierz_wybor(gracz):
    while True:
        wybor_Gracz = input(f'{gracz} podaj wybor: ')
        if wybor_Gracz in opcje:
             return wybor_Gracz


#funkcja sprawdzająca wyniki
def sprawdz_wyniki (wybor_Gracz1, wybor_Gracz2):
    if wybor_Gracz1 == wybor_Gracz2:
      print('REMIS')
      return 0

    
#słownik z którego pobierane są klucze z tupli 
    wynik = {
        ('papier','kamien') :1,
        ('kamien','nozyczki') :1,
        ('nozyczki','papier') :1 
    }

#return wynik z tupli dostępnych w słowników, w przypadku braku dostępnych zwróć wartość -1 
    return wynik.get ((wybor_Gracz1,wybor_Gracz2),  -1)

#graj dopóki któryś z graczy nie osiągnie 3 wygranych ruchów
while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_Gracz1 = pobierz_wybor ('Gracz1')
    wybor_Gracz2 = pobierz_wybor ('Gracz2')
    wynik = sprawdz_wyniki (wybor_Gracz1, wybor_Gracz2)

    if wynik == 1:
       print ('Wygrał Gracz1')
       gracz1_wynik += 1

    elif wynik == -1:
       print ('Wygrał Gracz2')
       gracz2_wynik += 1
  

if gracz1_wynik > gracz2_wynik:
  print ('Całą grę wygrał Gracz1')
else:
  print ('Całą grę wygrał Gracz2')  

