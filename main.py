"""
Tomasz Mianecki
Program do zmiany plików csv zawierajacych dane dla kart produktu
na pliki xml do użytku dla strony Globus Lighting wersja ang/fra
versja_alfa_1.2
"""
#importy
import xml.etree.ElementTree as ET
from csv import DictReader
import random

#flaga bool
flaga_ik = False
flaga_dedykowana_lista = False

# listy do urzycia
lista_kolumn_alfa = [
  "kod", "kodbarwy", "p", "flux", "sterowanie", "IP", "pled"
]
lista_subElementów_alfa = [
  "KOD", "RACCT", "MOC", "FLUX", "CONTROL", "IX", "ROZ"
]
lista_kolumn_beta = [
  "kod", "kodbarwy", "p", "flux", "sterowanie", "IP", "IK", "pled"
]
lista_kolumn_dedykowana = []

# dict z dodatkami do danych
dict_dorostki_danych = {
  "kod": 0,
  "rodzina": 0,
  "kodbarwy": 0,
  "ilosc": 0,
  "psu": 0,
  "ppsu": 0,
  "sterowanie": 0,
  "klasa": 0,
  "kolor": 0,
  "IP": "IP",
  "IK": "IK",
  "vin": "VAC",
  "hz": "Hz",
  "vs": 0,
  "zmienne": 0,
  "p": "W",
  "flux": "lm",
  "wyd": "lm/W",
  "pled": "°",
  "fluxled": "lm",
  "wydled": "lm/W",
  "cri": "Ra",
  "cct": "K",
  "barwa": 0,
  "masa": "±kg",
  "montaz": 0,
  "temperatury": 0,
  "dyfuzor": 0,
  "wymiary": "mm"
}

# input od operatora
nazwa_pliku_csv = input("Podaj nazwe pliku csv:")
nazwa_ok_Q = input(
  "\n Czy nazwa rodziny jest zawarta w pliku csv enter 't'> Tak, lub 'n'> dla Nie : "
)

# logika do obsługi inputu operatora
if nazwa_ok_Q.upper() == "T":
  rodzina = nazwa_pliku_csv[:-5]
  rodzina = rodzina.upper()
  print("\n", rodzina)
elif nazwa_ok_Q.upper() == "N":
  rodzina_input = input("Podaj prosze nazwę rodziny: ")
  rodzina = rodzina_input.upper()
  print("\n", rodzina)
elif nazwa_ok_Q.upper() == "Q":
  print("\n tryb testowy")
  rodzina = "test"
else:
  print("Wprowadzono nierozpoznawalną komende :", nazwa_ok_Q)
  exit()


# definicjia dla odczytu danych z pliku
def odczyt_danych_csv(plik_csv, list_zapisu):
  print("Start dla odczyt_danych_csv")
  list_wynik = []
  komponent = ""
  with open(plik_csv + '.csv', mode='r') as read_obj:
    csv_dict_reader = DictReader(read_obj, delimiter=';')
    for row in csv_dict_reader:
      for elem in list_zapisu:
        dodatek = dict_dorostki_danych.get(elem)
        element = row[elem]
        if dodatek == 0:
          komponent += element + " @ "
        elif dodatek in element:
          komponent += element + " @ "
        else:
          komponent += element + dodatek + " @ "
      #print("komponent",komponent)
      list_wynik.append(komponent[:-3])
      komponent = ""
  list_wynik.pop(0)
  print("Funkcja odczyt_danych_csv wykonana poprawnie ", list_zapisu, "\n")
  print("lista wynikowa", list_wynik)
  return list_wynik


# definicjia: tworzenie dedykowanej listy z inputu od operatora
def dedekowane_dane_listy():
  lista = ["kod", "kodbarwy", "p"]
  print(
    "Funkcja dedekowane_dane_listy start \n Na stałe wpisane są kod/kodbarwy/p"
  )
  print(
    "Wprowadż poniżej dane. Formuła: \n nazwa kolumn w csv, nastepnie znak '/' np:\n kod/psu/ppsu/kolor\n"
  )
  input_dla_listy = input("Enter :")
  lista_return = input_dla_listy.split("/")
  print("lista_return", lista_return)
  lista.extend(lista_return)
  print("lista dedykowana", lista)
  return lista


# definicjia: tworzenie pliku xml
def struktura_xml(lista):
  versja_Xml_input = input(
    "Podaj prosze wersję(liczba naturalna dodatnia od 0 do 2 147 483 647) pliku xml lub wpisz R=> dlarandomowego generowania: "
  )
  if versja_Xml_input.isdigit():
    versja_Xml = versja_Xml_input
  if versja_Xml_input.isalpha():
    versja_Xml = random.randint(0, 200)

  nazwa_pliku_xml = rodzina.lower() + "_BDXML" + "_versja_" + str(versja_Xml)
  data = ET.Element(rodzina)
  i_d = 1
  for x in lista:
    element1 = ET.SubElement(data, 'MODEL')
    element1.set("id", str(i_d))
    lista_alfa = str(x)
    lista_beta = lista_alfa.split(" @ ")
    for y in lista_beta:
      if "GL" in y:
        sub_elem = ET.SubElement(element1, 'KOD')
        sub_elem.text = y
      #print(lista_beta.index(y), y,type(y),len(y),y[-1])
      elif lista_beta.index(y) == 1:
        if len(y) == 3 and y[-1] == "0":
          racct = "Ra" + y[0] + "0 & " + y[1:] + "00K"
          sub_elem = ET.SubElement(element1, 'RACCT')
          sub_elem.text = racct
        else:
          sub_elem = ET.SubElement(element1, 'RACCT')
          sub_elem.text = y
      elif "W" in y and "GL" not in y:
        sub_elem = ET.SubElement(element1, 'MOC')
        sub_elem.text = y
      elif "lm" in y:
        sub_elem = ET.SubElement(element1, 'FLUX')
        sub_elem.text = y
      elif "°" in y:
        sub_elem = ET.SubElement(element1, 'ROZ')
        sub_elem.text = y
      elif y[0] == 'I':
        sub_elem = ET.SubElement(element1, y[0:2])
        sub_elem.text = y
      else:
        nazwa_elementu = 'elem_'
        liczba = lista_beta.index(y)
        if flaga_ik == False and flaga_dedykowana_lista == False:
          nazwa_elementu += lista_kolumn_alfa[liczba]
        elif flaga_dedykowana_lista:
          nazwa_elementu += lista_kolumn_dedykowana[liczba]
        elif flaga_ik:
          nazwa_elementu += lista_kolumn_beta[liczba]
        else:
          print("problem w struktura_xml dolny sektor if")
        sub_elem = ET.SubElement(element1, nazwa_elementu)
        sub_elem.text = y
    i_d += 1
    b_xml = ET.tostring(data,
                        encoding="utf-8",
                        method='xml',
                        xml_declaration=True)
  with open(nazwa_pliku_xml + ".xml", "wb") as f:
    f.write(b_xml)


# input określający jaką liste z kolumnami wybrać
print("\n Standard danych do pobrania z csv to 'Nova' czyli :\n",
      lista_kolumn_beta, "\n")
inpuT_funkcje = input(
  "\n Wprowadzić 'N' => dla 'Nova', 'B'=> dla csv bez 'IK', 'L'=> dla chęci wprowadzenia własnej listy :"
)
print("wybrana opcja :", inpuT_funkcje.upper())

# logika obsługi wybranych opcji
if inpuT_funkcje.upper() == "N":
  lista_wynikowa_odczytu = odczyt_danych_csv(nazwa_pliku_csv,
                                             lista_kolumn_beta)
  flaga_ik = True
elif inpuT_funkcje.upper() == "B":
  lista_wynikowa_odczytu = odczyt_danych_csv(nazwa_pliku_csv,
                                             lista_kolumn_alfa)
elif inpuT_funkcje.upper() == "L":
  flaga_dedykowana_lista = True
  lista_kolumn_dedykowana = dedekowane_dane_listy()
  lista_wynikowa_odczytu = odczyt_danych_csv(nazwa_pliku_csv,
                                             lista_kolumn_dedykowana)

# wywołanie funkcji tworzącej xml
struktura_xml(lista_wynikowa_odczytu)

# info o zakończeniu działania
print("koniec programu")
