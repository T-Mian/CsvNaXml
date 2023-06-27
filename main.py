"""
Tomasz Mianecki
versja_alfa_001
"""
#importy
import xml.etree.ElementTree as ET
from csv import DictReader

lista_kolumn_alfa = [
  "kod", "p", "flux", "sterowanie", "kodbarwy", "IP", "pled"
]

lista_kolumn_beta = [
  "kod", "p", "flux", "sterowanie", "kodbarwy", "IP", "IK", "pled"
]
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

lista_kolumn_dedykowana = []

# input od operatora okreslenie nazw
nazwa_pliku_csv = input("Podaj nazwe pliku csv:")
nazwa_ok_Q = input(
  "\n Czy nazwa rodziny jest zawarta w pliku csv enter 't'> Tak, lub 'n'> dla Nie : "
)
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

# komponenty dla xml'a
data = ET.Element(rodzina)
element1 = ET.SubElement(data, 'MODEL')
s_elem1 = ET.SubElement(element1, 'KOD')
s_elem2 = ET.SubElement(element1, 'MOC')
s_elem3 = ET.SubElement(element1, 'FLUX')
s_elem4 = ET.SubElement(element1, 'CONTROL')
s_elem5 = ET.SubElement(element1, 'IX')
s_elem6 = ET.SubElement(element1, 'RACCT')
s_elem7 = ET.SubElement(element1, 'ROZ')
s_elem8 = ET.SubElement(element1, 'INNE')

# zapis wartości tekstowej do elementu
#s_elem1.text = "King's Gambit Accepted"


# definicjia dla odczytu danych z pliku
def odczyt_danych_csv(plik_csv, list_zapisu):
  print("Start dla odczyt_danych_csv")
  list_wynik = []
  komponent = ""
  with open(plik_csv + '.csv', mode='r') as read_obj:
    csv_dict_reader = DictReader(read_obj, delimiter=';')
    for row in csv_dict_reader:
      for elem in list_zapisu:
        komponent += row[elem] + " @ "
      #print(komponent)
      list_wynik.append(komponent[:-3])
      komponent = ""
  list_wynik.pop(0)
  print("Funkcja odczyt_danych_csv wykonana poprawnie ", list_zapisu, "\n")
  print(list_wynik)


def dedekowane_dane_listy(lista):
  lista_kolumn_dedykowana.clear()
  print("Funkcja dedekowane_dane_listy start \n")
  print(
    "Wprowadż poniżej dane. Formuła: \n nazwa kolumn w csv, nastepnie znak '/' np:\n kod/psu/ppsu/kolor\n"
  )
  input_dla_listy = input("Enter :")
  lista_return = input_dla_listy.split("/")
  print(lista_return)
  lista.extend(lista_return)


def obrobienieDanych():
  return


def struktura_xml():
  return


print("\n Standard danych do pobrania z csv to 'Nova' czyli :\n",
      lista_kolumn_beta, "\n")
inpuT_funkcje = input(
  "\n Wprowadzić 'N' => dla 'Nova', 'B'=> dla csv bez 'IK', 'L'=> dla chęci wprowadzenia własnej listy :"
)
print("wybrana opcja :", inpuT_funkcje.upper())

if inpuT_funkcje.upper() == "N":
  odczyt_danych_csv(nazwa_pliku_csv, lista_kolumn_beta)
elif inpuT_funkcje.upper() == "B":
  odczyt_danych_csv(nazwa_pliku_csv, lista_kolumn_alfa)
elif inpuT_funkcje.upper() == "L":
  dedekowane_dane_listy(lista_kolumn_dedykowana)
  odczyt_danych_csv(nazwa_pliku_csv, lista_kolumn_dedykowana)

print("koniec programu")
