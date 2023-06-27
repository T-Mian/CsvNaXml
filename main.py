"""
Tomasz Mianecki
versja_alfa_001
"""
#importy
import xml.etree.ElementTree as ET
from csv import DictReader
import random

flaga_ik = False
flaga_dedykowana_lista=False
lista_kolumn_alfa = [
  "kod", "p", "flux", "sterowanie", "kodbarwy", "IP", "pled"
]
lista_kolumn_beta = [
  "kod", "p", "flux", "sterowanie", "kodbarwy", "IP", "IK", "pled"
]

lista_kolumn_dedykowana = []

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
lista_xmla = []

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
        dodatek = dict_dorostki_danych.get(elem)
        element = row[elem]
        if dodatek == 0:
          komponent += element + " @ "
        elif dodatek in element:
          komponent += element + " @ "
        else:
          komponent += element + dodatek + " @ "
      #print(komponent)
      list_wynik.append(komponent[:-3])
      komponent = ""
  list_wynik.pop(0)
  print("Funkcja odczyt_danych_csv wykonana poprawnie ", list_zapisu, "\n")
  #print(list_wynik)
  return list_wynik


def dedekowane_dane_listy(lista):
  lista_kolumn_dedykowana.clear()
  print("Funkcja dedekowane_dane_listy start \n")
  print(
    "Wprowadż poniżej dane. Formuła: \n nazwa kolumn w csv, nastepnie znak '/' np:\n kod/psu/ppsu/kolor\n"
  )
  input_dla_listy = input("Enter :")
  lista_return = input_dla_listy.split("/")
  #print(lista_return)
  lista.extend(lista_return)


def struktura_xml(lista):
  versja_Xml_input=input("Podaj prosze wersję(liczba naturalna dodatnia od 0 do 2 147 483 647) pliku xml lub wpisz R=> dlarandomowego generowania: ")
  if versja_Xml_input.isdigit():
    versja_Xml=versja_Xml_input
  if versja_Xml_input.isalpha():
    versja_Xml=random.randint(0,200)
    
  nazwa_pliku_xml = rodzina.lower()+"BDXML"+"_versja_"+str(versja_Xml)
  data = ET.Element(rodzina)
  i_d = 1
  for x in lista:
    element1 = ET.SubElement(data, 'MODEL')
    s_elem_kod = ET.SubElement(element1, 'KOD')
    s_elem_moc = ET.SubElement(element1, 'MOC')
    s_elem_flux = ET.SubElement(element1, 'FLUX')
    s_elem_cont = ET.SubElement(element1, 'CONTROL')
    s_elem_ix = ET.SubElement(element1, 'IX')
    s_elem_racct = ET.SubElement(element1, 'RACCT')
    s_elem_roz = ET.SubElement(element1, 'ROZ')
    s_elem_inne = ET.SubElement(element1, 'INNE')
    element1.set("type", str(i_d))
    alfa = str(x)
    beta = alfa.split(" @ ")
    s_elem_kod.text = beta[0]
    s_elem_moc.text = beta[1]
    s_elem_flux.text = beta[2]
    s_elem_cont.text = beta[3]
    if flaga_ik:
      s_elem_ix.text = beta[5] + " & " + beta[6]
      str_gamma = str(beta[4])
      str_ra = "Ra" + str_gamma[0] + "0"
      str_cct = " & " + str_gamma[1:] + "00K"
      s_elem_racct.text = str_ra + str_cct
      s_elem_roz.text = beta[7]
      s_elem_inne.text = "null"
    else :
        s_elem_ix.text = beta[5]
        str_gamma = str(beta[4])
        str_ra = "Ra" + str_gamma[0] + "0"
        str_cct = " & " + str_gamma[1:] + "00K"
        s_elem_racct.text = str_ra + str_cct
        s_elem_roz.text = beta[6]
        s_elem_inne.text = "null"
    
    i_d += 1
    b_xml = ET.tostring(data,encoding="utf-8",method='xml',xml_declaration=True)
  with open(nazwa_pliku_xml+".xml", "wb") as f:
    f.write(b_xml)


print("\n Standard danych do pobrania z csv to 'Nova' czyli :\n",
      lista_kolumn_beta, "\n")
inpuT_funkcje = input(
  "\n Wprowadzić 'N' => dla 'Nova', 'B'=> dla csv bez 'IK', 'L'=> dla chęci wprowadzenia własnej listy :"
)
print("wybrana opcja :", inpuT_funkcje.upper())

if inpuT_funkcje.upper() == "N":
  lista_wynikowa_odczytu = odczyt_danych_csv(nazwa_pliku_csv,
                                             lista_kolumn_beta)
  flaga_ik = True
elif inpuT_funkcje.upper() == "B":
  lista_wynikowa_odczytu = odczyt_danych_csv(nazwa_pliku_csv,
                                             lista_kolumn_alfa)
elif inpuT_funkcje.upper() == "L":
  dedekowane_dane_listy(lista_kolumn_dedykowana)
  lista_wynikowa_odczytu = odczyt_danych_csv(nazwa_pliku_csv,
                                             lista_kolumn_dedykowana)

#print(lista_wynikowa_odczytu)
struktura_xml(lista_wynikowa_odczytu)
print("koniec programu")
