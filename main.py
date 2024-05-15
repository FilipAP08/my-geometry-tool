import math

#import pyfiglet
import os
import time

pi = 3.141592653589793238462643383279502884197169399375105820

#menu startowe
def menu():
  os.system("cls")
  #baner = pyfiglet.figlet_format("PRZYBORNIK GEOMETRYCZNY")
  #print(baner)

  print(" ____  ____   _______   ______   ___  ____  _   _ ___ _  __")
  print(r"|  _ \|  _ \ |__  /\ \ / / __ ) / _ \|  _ \| \ | |_ _| |/ /")
  print(r"| |_) | |_) |  / /  \ V /|  _ \| | | | |_) |  \| || || ' / ")
  print(r"|  __/|  _ <  / /_   | | | |_) | |_| |  _ <| |\  || || . \ ")
  print(r"|_|   |_| \_\/____|  |_| |____/ \___/|_| \_\_| \_|___|_|\_\ ")
  print()
  print("  ____ _____ ___  __  __ _____ _____ ______   ______ ______   ___   __")
  print(r" / ___| ____/ _ \|  \/  | ____|_   _|  _ \ \ / / ___|__  / \ | \ \ / /")
  print(r"| |  _|  _|| | | | |\/| |  _|   | | | |_) \ V / |     / /|  \| |\ V / ")
  print(r"| |_| | |__| |_| | |  | | |___  | | |  _ < | || |___ / /_| |\  | | |  ")
  print(r" \____|_____\___/|_|  |_|_____| |_| |_| \_\|_| \____/____|_| \_| |_|  ")
  print()

  print("0 - Zamknij program")
  print("1 - Pola powiechrzni figur")
  print("2 - Objętości brył")
  print("3 - Kąty płaskie")
  print()

  #sprawdzanie wyborów użytkownika
  wybor = (input("Wybierz opcję... "))

  if wybor == "0":
    exit()
  elif wybor == "1":
    menu1()
  elif wybor == "2":
    menu2()
  elif wybor == "3":
    menu3()
  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    menu()


################################################################################################################################


#dostępne opcje objętości
def menu2():
  os.system("cls")
  print("OBJETOSCI BRYL")
  print()
  print("0 - Wstecz")
  print("1 - Objętość kuli")
  print("2 - Objętość sześćianu")
  print("3 - Objętość prostopadłościanu")
  print("4 - Objętość walca")
  print("5 - Objętość ostrosłupa")
  print("6 - Objętość stożka")
  print()

  #sprawdzanie wyborów użytkownika
  wybor = (input("Wybierz opcję... "))

  if wybor == "0":
    menu()
  elif wybor == "1":
    kula()
  elif wybor == "2":
    szescian()
  elif wybor == "3":
    prostopadloscian()
  elif wybor == "4":
    walec()
  elif wybor == "5":
    ostroslup()
  elif wybor == "6":
    stozek()
  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    menu()


################################################################################################################################


#obj kula
def kula1():
  os.system("cls")
  rSTR = (input("Wpisz wartość r: "))
  r = 0.0
  
  try:
    r = float(rSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    kula1()
  
  if r <= 0:
    print("BŁĄD!")
    print("promień nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    kula1()
    
  else:
    x = (4 / 3) * pi * (r * r * r)
    print(x)
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    kula()


#menu kula
def kula():
  os.system("cls")

  print("r - promień kuli (połowa średnicy)")
  print("r ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    kula1()

  elif wybor1 == "2":
    menu2()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    kula()


################################################################################################################################


#obj sześcian
def szescian1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0
  
  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    szescian1()

  if a <= 0:
    print("BŁĄD!")
    print("bok nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    szescian1()
  else:
    x = a * a * a
    print(x)
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    szescian()


#menu sześcian
def szescian():
  os.system("cls")

  print("a - bok sześcianu")
  print("a ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    szescian1()

  elif wybor1 == "2":
    menu2()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    szescian()


################################################################################################################################69


#obj prostopadłościan
def prostopadloscian1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0

  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    prostopadloscian1()
  
  if a <= 0:
    print("BŁĄD!")
    print("bok nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    prostopadloscian1()
    
  else:
    bSTR = (input("Wpisz wartość b: "))
    b = 0.0
    
    try:
      b = float(bSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      prostopadloscian1()
    
    if b <= 0:
      print("BŁĄD!")
      print("bok nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      prostopadloscian1()
    else:
      cSTR = (input("Wpisz wartość c: "))
      c = 0.0

      try:
        c = float(cSTR)
      except ValueError:
        print("niepoprawnie podano liczbe")
        time.sleep(3)
        prostopadloscian1()
        
      if c <= 0:
        print("BŁĄD!")
        print("bok nie może mieć 0 lub ujemnej długości")
        time.sleep(3)
        prostopadloscian1()
        
      else:
        x = a * b * c
        print(x)
        time.sleep(1)
        input('Wciśnij ENTER aby kontynuować...')
        prostopadloscian()


#menu prostopadłościan
def prostopadloscian():
  os.system("cls")

  print("a,b,c - boki prostopadłościanu")
  print("a,b,c ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    prostopadloscian1()

  elif wybor1 == "2":
    menu2()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    prostopadloscian()


################################################################################################################################


#obj walec
def walec1():
  os.system("cls")
  rSTR = (input("Wpisz wartość r: "))
  r = 0.0

  try:
    r = float(rSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    walec1()
  
  if r <= 0:
    print("BŁĄD!")
    print("promień nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    walec1()
    
  else:
    hSTR = (input("Wpisz wartość h: "))
    h = 0.0

    try:
      h = float(hSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      walec1()
    
    if h <= 0:
      print("BŁĄD!")
      print("wysokość nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      walec1()
    else:
      x = pi * (r * r) * h
      print(x)
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      walec()


#menu walec
def walec():
  os.system("cls")

  print("r - promień podstawy walca (połowa średnicy)")
  print("h - wysokość walca")
  print("r,h ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    walec1()

  elif wybor1 == "2":
    menu2()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    walec()


################################################################################################################################69


#obj ostroslup
def ostroslup1():
  os.system("cls")
  r = (input("Wpisz wartość Pp: "))
  rSTR = 0.0

  try:
    r = float(rSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    ostroslup1()
  
  if Pp <= 0:
    print("BŁĄD!")
    print("pole nie może mieć 0 lub ujemnej wartości")
    time.sleep(3)
    ostroslup1()
    
  else:
    hSTR = (input("Wpisz wartość h: "))
    h = 0.0

    try:
      h = float(hSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      walec1()
    
    if h <= 0:
      print("BŁĄD!")
      print("wysokość nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      ostroslup1()
    else:
      x = 1 / 3 * (Pp * h)
      print(x)
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      ostroslup()


#menu ostroslup
def ostroslup():
  os.system("cls")

  print("Pp - pole podstawy ostrosłupa")
  print("h - wysokość ostrosłupa")
  print("Pp,h ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = input("Wybierz opcję... ")

  if wybor1 == "1":
    ostroslup1()

  elif wybor1 == "2":
    menu2()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    ostroslup()


################################################################################################################################69


#obj
def stozek1():
  os.system("cls")
  rSTR = (input("Wpisz wartość r: "))
  r = 0.0

  try:
    r = float(rSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    stozek1()
  
  if r <= 0:
    print("BŁĄD!")
    print("promień nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    stozek1()
    
  else:
    hSTR = (input("Wpisz wartość h: "))
    h = 0.0

    try:
      h = float(hSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      walec1()
      
    if h <= 0:
      print("BŁĄD!")
      print("wysokość nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      stozek1()
    
    else:
      x = 1 / 3 * (pi * r * r) * h
      print(x)
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      stozek()


#menu stozek
def stozek():
  os.system("cls")

  print("r - promień podstawy stożka (połowa średnicy)")
  print("h - wysokość stożka")
  print("r,h ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    stozek1()

  elif wybor1 == "2":
    menu2()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    stozek()


################################################################################################################################
################################################################################################################################


#dostępne opcje pola
def menu1():
  os.system("cls")
  print("POLA FIGUR")
  print()

  print("0 - Wstecz")
  print("1 - Twierdzenie Pitagorasa")
  print("2 - Pole trójkąta")
  print("3 - Pole kwadratu")
  print("4 - Pole prostokąta")
  print("5 - Pole równoległoboku")
  print("6 - Pole trapezu")
  print("7 - Pole koła")
  print()

  #sprawdzanie wyborów użytkownika
  wybor = (input("Wybierz opcję... "))

  if wybor == "0":
    menu()
  elif wybor == "1":
    pitagoras()
  elif wybor == "2":
    trojkat()
  elif wybor == "3":
    kwadrat()
  elif wybor == "4":
    prostokat()
  elif wybor == "5":
    rownoleglobok()
  elif wybor == "6":
    trapez()
  elif wybor == "7":
    kolo()
  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    menu()


################################################################################################################################


#oblicznie Twierdzenia Pitagorasa 1
def pitagoras1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0

  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    pitagoras1()
  
  if a <= 0:
    print("BŁĄD!")
    print("bok nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    pitagoras1()
    
  else:
    bSTR = (input("Wpisz wartość b: "))
    b = 0.0

    try:
      b = float(bSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      pitaogras1()
    
    if b <= 0:
      print("BŁĄD!")
      print("bok nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      pitagoras1()
      
    else:
      x = math.sqrt(a * a + b * b)
      y = a * a + b * b
      print(" ")
      print(x)
      print("(Pierwiastek kwadratowy z: " + str(y) + ")")
      print(" ")
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      pitagoras()


#oblicznie Twierdzenia Pitagorasa 2
def pitagoras2():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0

  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    pitagoras2()
  
  if a <= 0:
    print("BŁĄD!")
    print("bok nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    pitagoras2()
    
  else:
    cSTR = (input("Wpisz wartość c: "))
    c = 0.0
    try:
      c = float(cSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      pitagoras2()
      
    if c <= 0:
      print("BŁĄD!")
      print("bok nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      pitagoras2()
    else:
      x = math.sqrt(c * c - a * a)
      y = c * c - a * a
      print(" ")
      print(x)
      print("(Pierwiastek kwadratowy z: " + str(y) + ")")
      print(" ")
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      pitagoras()


#oblicznie Twierdzenia Pitagorasa 3
def pitagoras3():
  os.system("cls")
  bSTR = (input("Wpisz wartość b: "))
  b = 0.0
  try:
    b = float(bSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    tome.sleep(3)
    pitagoras3()
  
  if b <= 0:
    print("BŁĄD!")
    print("bok nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    pitagoras3()
  
  else:
    cSTR = (input("Wpisz wartość c: "))
    c = 0.0
    try:
      c = float(cSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      pitagoras3()
    
    if c <= 0:
      print("BŁĄD!")
      print("bok nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      pitagoras3()
    
    else:
      x = math.sqrt(c * c - b * b)
      y = c * c - b * b
      print(" ")
      print(x)
      print("(Pierwiastek kwadratowy z: " + str(y) + ")")
      print(" ")
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      pitagoras()


#menu Twierdzenia Pitagorasa
def pitagoras():
  os.system("cls")

  print("a, b - długości przyprostokątnych")
  print("c - długość przeciwprostokątnej")
  print("X - niewiadoma")
  print("a,b,c,X ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - a^2 + b^2 = X")
  print("2 - a^2 + X = c^2")
  print("3 - X + b^2 = c^2")
  print("4 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    pitagoras1()

  elif wybor1 == "2":
    pitagoras2()

  elif wybor1 == "3":
    pitagoras3()

  elif wybor1 == "4":
    menu1()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    pitagoras()


################################################################################################################################


#pole trójkąta
def trojkat1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0

  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    trojkat1()
  
  if a <= 0:
    print("BŁĄD!")
    print("podstawa nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    trojkat1()
  else:
    hSTR = (input("Wpisz wartość a: "))
    h = 0.0
    
    try:
      h = float(hSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      trojkat1()
    
    if h <= 0:
      print("BŁĄD!")
      print("wysokość nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      trojkat1()
    else:
      x = 0.5 * (a * h)
      print(x)
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      trojkat()


#menu trójkąt
def trojkat():
  os.system("cls")

  print("a - podstawa trójkąta")
  print("h - wysokość")
  print("a,h ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    trojkat1()

  elif wybor1 == "2":
    menu1()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    trojkat()


################################################################################################################################


#pole kwadratu - bok
def kwadrat1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0
  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    kwadrat1()
  
  if a <= 0:
    print("BŁĄD!")
    print("bok nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    kwadrat1()
    
  else:
    x = a * a
    print(x)
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    kwadrat()


#pole kwadratu - przekątna
def kwadrat2():
  os.system("cls")
  dSTR = (input("Wpisz wartość d: "))
  d = 0.0

  try:
    d = float(dSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    kwadrat2()
  
  if d <= 0:
    print("BŁĄD!")
    print("przekątna nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    kwadrat2()
  else:
    a = math.sqrt(d * d / 2)
    x = a * a
    print(x)
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    kwadrat()


#menu kwadrat
def kwadrat():
  os.system("cls")

  print("a - długość boku kwadratu")
  print("d - długość przekątnej kwadratu")
  print("a,d ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("Oblicz pole:")
  print("1 - na podstawie boku kwadratu")
  print("2 - na podstawie przekątnej kwadratu")
  print("3 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    kwadrat1()

  elif wybor1 == "2":
    kwadrat2()

  elif wybor1 == "3":
    menu1()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    kwadrat()


################################################################################################################################


#pole prostokąta
def prostokat1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0
  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    prostokat1()

  if a <= 0:
    print("BŁĄD!")
    print("bok nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    prostokat1()
  else:
    bSTR = (input("Wpisz wartość b: "))
    b = 0.0
    try:
      b = float(bSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      prostokat1()
      
    if b <= 0:
      print("BŁĄD!")
      print("bok nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      prostokat1()
    else:
      x = a * b
      print(x)
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      prostokat()


#menu prostokąt
def prostokat():
  os.system("cls")

  print("a - krótszy bok prostokąta")
  print("b - dłuższy bok prostokąta")
  print("a,b ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    prostokat1()

  elif wybor1 == "2":
    menu1()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    prostokat()


################################################################################################################################


#pole równoległoboku
def rownoleglobok1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0
  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    rownoleglobok1()
    
  if a <= 0:
    print("BŁĄD!")
    print("podstawa nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    rownoleglobok1()
    
  else:
    hSTR = (input("Wpisz wartość h: "))
    h = 0.0
    try:
      h = float(hSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      rownoleglobok1()
      
    if h <= 0:
      print("BŁĄD!")
      print("wysokość nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      rownoleglobok1()
    else:
      x = a * h
      print(x)
      time.sleep(1)
      input('Wciśnij ENTER aby kontynuować...')
      rownoleglobok()


#menu równoległobok
def rownoleglobok():
  os.system("cls")

  print("a - podstawa równoległoboku")
  print("h - wysokość równoległoboku")
  print("a,h ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    rownoleglobok1()

  elif wybor1 == "2":
    menu1()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    rownoleglobok()


################################################################################################################################69


#pole trapezu
def trapez1():
  os.system("cls")
  aSTR = (input("Wpisz wartość a: "))
  a = 0.0
  try:
    a = float(aSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    trapez1()
    
  if a <= 0:
    print("BŁĄD!")
    print("podstawa nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    trapez1()
  else:
    bSTR = (input("Wpisz wartość b: "))
    b = 0.0
    try:
      b = float(bSTR)
    except ValueError:
      print("niepoprawnie podano liczbe")
      time.sleep(3)
      trapez1()
      
    if b <= 0:
      print("BŁĄD!")
      print("podstawa nie może mieć 0 lub ujemnej długości")
      time.sleep(3)
      trapez1()
      
    else:
      hSTR = (input("Wpisz wartość h: "))
      h = 0.0
      try:
        h = float(bSTR)
      except ValueError:
        print("niepoprawnie podano liczbe")
        time.sleep(3)
        trapez1()
        
      if h <= 0:
        print("BŁĄD!")
        print("wysokość nie może mieć 0 lub ujemnej długości")
        time.sleep(3)
        trapez1()
      else:
        x = ((a + b) * h) / 2
        print(x)
        time.sleep(1)
        input('Wciśnij ENTER aby kontynuować...')
        trapez()


#menu trapez
def trapez():
  os.system("cls")

  print("a - krótsza podstawa trapezu")
  print("b - dłuższa podstawa trapezu")
  print("h - wysokość trapezu")
  print("a,b,h ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    trapez1()

  elif wybor1 == "2":
    menu1()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    trapez()


################################################################################################################################69


#pole koła
def kolo1():
  os.system("cls")
  rSTR = (input("Wpisz wartość r: "))
  r = 0.0
  try:
    r = float(rSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    kolo1()
    
  if r <= 0:
    print("BŁĄD!")
    print("promień nie może mieć 0 lub ujemnej długości")
    time.sleep(3)
    kolo1()
  else:
    x = 3.14159265 * (r * r)
    print(x)
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    kolo()


#menu kolo
def kolo():
  os.system("cls")

  print("r - promień koła (połowa średnicy)")
  print("r ≠ 0")
  print()
  print("Należy podać same liczby dodatnie, bez symbolu jednostek")
  print(
      "Jako znaku części dziesiętnej należy użyć kropki (.), a nie przecinka(,)"
  )
  print()
  print("1 - Dalej")
  print("2 - powrót")
  print()
  wybor1 = (input("Wybierz opcję... "))

  if wybor1 == "1":
    kolo1()

  elif wybor1 == "2":
    menu1()

  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    kolo()


################################################################################################################################
################################################################################################################################

def menu3():
  os.system("cls")
  print("KĄTY PŁASKIE")
  print()
  print("0 - Wstecz")
  print("1 - Suma kątów wewnętrznych wielokąta")
  print("2 - Miara kąta wewnętrznego wielokąta foremnego")
  print("3 - Miara kąta zewnętrznego wielokąta foremnego")

  #sprawdzanie wyborów użytkownika
  wybor = (input("Wybierz opcję... "))

  if wybor == "0":
    menu()
  elif wybor == "1":
    katy_wewn()
  elif wybor == "2":
    kat_wewn_forem()
  elif wybor == "3":
    kat_zewn_forem()
  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    menu3()


################################################################################################################################


#suma kątów wewnętrznych wielokąta
def katy_wewn():
  os.system("cls")
  print("n - ilość wierzchołków wielokąta")
  print("n ≥ 3")
  print()
  print("0 - powrót")
  print("1 - Dalej")
  wybor = (input("Wybierz opcję... "))

  if wybor == "0":
    menu3()
  elif wybor == "1":
    katy_wewn1()
  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    katy_wewn()


def katy_wewn1():
  os.system("cls")
  nSTR = (input("Wpisz wartość n: "))
  n = 0.0
  try:
    n = int(nSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    katy_wewn1()
    
  if n < 3:
    print("BŁĄD!")
    print("podano niepoprawną ilkość wierzchołków")
    time.sleep(3)
    katy_wewn1()
  else:
    x = 180 * (n - 2)
    print("Suma kątów dla podanego n: " + str(x))
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    katy_wewn()


################################################################################################################################
#miara kąta wewnętrznego wielokąta foremnego


def kat_wewn_forem():
  os.system("cls")
  print("n - ilość wierzchołków wielokąta")
  print("n ≥ 3")
  print()
  print("0 - powrót")
  print("1 - Dalej")
  wybor = (input("Wybierz opcję... "))

  if wybor == "0":
    menu3()
  elif wybor == "1":
    kat_wewn_forem1()
  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    kat_wewn_forem()


def kat_wewn_forem1():
  os.system("cls")
  nSTR = (input("Wpisz wartość n: "))
  n = 0.0
  try:
    n = int(nSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    kat_wewn_forem1()
    
  if n < 3:
    print("BŁĄD!")
    print("podano niepoprawną ilkość wierzchołków")
    time.sleep(3)
    kat_wewn_forem1()
  else:
    x = 180 * (n - 2) / n
    print("Pojedyńczy kąt wewnętrzny dla podanego n: " + str(x))
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    kat_wewn_forem()

  ################################################################################################################################


#miara kąta zewnętrznego wielokąta foremnego
def kat_zewn_forem():
  os.system("cls")
  print("n - ilość wierzchołków wielokąta")
  print("n ≥ 3")
  print()
  print("0 - powrót")
  print("1 - Dalej")
  wybor = (input("Wybierz opcję... "))

  if wybor == "0":
    menu3()
  elif wybor == "1":
    kat_zewn_forem1()
  else:
    print("BŁĄD!")
    print("Wybrano opcję, która nie istnieje!")
    time.sleep(2)
    kat_zewn_forem()

def kat_zewn_forem1():
  os.system("cls")
  nSTR = (input("Wpisz wartość n: "))
  n = 0.0
  try:
    n = int(nSTR)
  except ValueError:
    print("niepoprawnie podano liczbe")
    time.sleep(3)
    kat_zewn_forem1()
  if n < 3:
    print("BŁĄD!")
    print("podano niepoprawną ilkość wierzchołków")
    time.sleep(3)
    kat_zewn_forem1()
  else:
    x = 720 / n
    print("Pojedyńczy kąt zewnętrzny dla podanego n: " + str(x))
    time.sleep(1)
    input('Wciśnij ENTER aby kontynuować...')
    kat_zewn_forem()

#wywołanie głównego programu
menu()
