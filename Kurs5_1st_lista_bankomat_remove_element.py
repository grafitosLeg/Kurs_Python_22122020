tranzakcje = []

WYBOR = None

while WYBOR != '0':
    print('0 wybor operacji\n1 wpłać kasę\n2 wypłać kasę\n3 sprawdź saldo\n4 uznania')
    WYBOR = input ('Wybierz opcje:  ')
    if WYBOR == '1':
        kwota = input ('Podaj kwotę do wpłaty:  ')
        tranzakcje.append (int(kwota))
    elif WYBOR == '2':
        kwota = input ('Podaj kwotę do wypłaty:  ')
        tranzakcje.append (-int(kwota))
    elif WYBOR == '3':
        #saldo = 0
        #for kwota in tranzakcje:
          #saldo += kwota
          #saldo = sum (tranzakcje)
          #print (saldo)
    #z uzyciem funkcji sum
        #saldo = sum (tranzakcje)
        #print(saldo)
    #z uzyciem f-stringa
        print (f'saldo = {sum (tranzakcje)}')
    elif WYBOR == '4':
      #uznania = 0
      for kwota in tranzakcje:
        #if kwota > 0:
           #uznania += kwota
        if kwota < 0:
          tranzakcje.remove (kwota)
      
      print (f'uznania = {sum(tranzakcje)}')
    print (tranzakcje) 