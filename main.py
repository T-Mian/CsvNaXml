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
lista_kolumn_alfa_info = ["0|0", "0|W", "0|lm", "0|0", "0|0", "0|IP", "0|°"]

lista_kolumn_beta = [
  "kod", "p", "flux", "sterowanie", "kodbarwy", "IP", "IK", "pled"
]
lista_kolumn_beta_info = [
  "0|0", "0|W", "0|lm", "0|0", "0|0", "0|IP", "0|IK", "0|°"
]

lista_kolumn_dedykowana = []
lista_kolumn_dedykowana_info = []

# input od operatora okreslenie nazw
nazwa_pliku_csv = input("Podaj nazwe pliku csv:")
nazwa_ok_Q = input(
  "Czy nazwa rodziny jest zawarta w pliku csv enter t> Tak, lub n> dla Nie : ")
if nazwa_ok_Q.upper() == "T":
  rodzina = nazwa_pliku_csv[:-5]
  rodzina = rodzina.upper()
  print(rodzina)
elif nazwa_ok_Q.upper() == "N":
  rodzina_input = input("Podaj prosze nazwę rodiny: ")
  rodzina = rodzina_input.upper()
  print(rodzina)
elif nazwa_ok_Q.upper() == "Q":
  print("tryb testowy")
  rodzina = "test"

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
      list_wynik.append(komponent)
      komponent = ""
  list_wynik.pop(0)
  print("Funkcja odczyt_danych_csv wykonana poprawnie")

def dedekowane_dane_listy():
  return



def obrobienieDanych():
  return


def struktura_xml():
  return


print("\n Standard danych do pobrania z csv to 'Nova' czyli :\n",lista_kolumn_beta,"\n")
inpuT_funkcje = input("\n Wprowadzić 'N' => dla 'Nova', 'B'=> dla csv bez 'IK', 'L'=> dla chęci wprowadzenia własnej listy :")
print("wybrana opcja :", inpuT_funkcje.upper())

#odczyt_danych_csv(nazwa_pliku_csv, lista_kolumn_beta)
