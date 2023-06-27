"""
Tomasz Mianecki
versja_alfa_001
"""
#importy
import xml.etree.ElementTree as ET
from csv import DictReader

lista_kolumn_alfa=["kod","p","flux","sterowanie","kodbarwy","IP","pled"]
lista_kolumn_beta=["kod","p","flux","sterowanie","kodbarwy","IP","IK","pled"]

# input od operatora
nazwa_pliku_csv = input("Podaj nazwe pliku csv:")
nazwa_ok_Q = input("Czy nazwa rodziny jest zawarta w pliku csv enter t> Tak, lub n> dla Nie : ")
if nazwa_ok_Q.upper()=="T":
  rodzina= nazwa_pliku_csv[:-5]
  rodzina.upper()
  print(rodzina)
elif nazwa_ok_Q.upper()=="N":
  rodzina_input=input("Podaj prosze nazwę rodiny: ")
  rodzina=rodzina_input.upper()
  print(rodzina)
elif nazwa_ok_Q.upper()=="Q":
  print("tryb testowy")
  rodzina="test"



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

def struktura_xml():
  return


def odczyt_danych_csv(plik_csv):
  list_wynik = []
  with open(plik_csv + '.csv', mode='r') as read_obj:
    csv_dict_reader = DictReader(read_obj, delimiter=';')
    for row in csv_dict_reader:
      list_wynik.append(row['kod'] + " @ " + row["p"] + " W" + " @ " +
                       row["flux"] + " lm " + "@ " + row["sterowanie"] +
                       " @ " + row["kodbarwy"] + " @ " + row['IP'] + " @ " +
                       row["pled"] + "°")
  list_wynik.pop(0)
  for x in list_wynik:
    print(x)
  


odczyt_danych_csv(nazwa_pliku_csv)
