import xml.etree.ElementTree as ET
import csv 

nazwa_pliku_csv = input("Enter nazwa pliku csv:")
nazwa_rodziny = input("Enter nazwa rodziny:")
rodzina = nazwa_rodziny.upper()

data = ET.Element(rodzina)
element1 = ET.SubElement(data, 'MODEL')
s_elem1 = ET.SubElement(element1, 'KOD')
s_elem2 = ET.SubElement(element1, 'MOC')
s_elem3 = ET.SubElement(element1, 'FLUX')
s_elem4 = ET.SubElement(element1, 'CONTROL')
s_elem5 = ET.SubElement(element1, 'IX')
s_elem6 = ET.SubElement(element1, 'RACCT')
s_elem7 = ET.SubElement(element1, 'INNE')

def struktura_xml():
  return


def odczyt_danych_csv(plik_csv):
  # otworzenie pliku
  with open(plik_csv+'.csv', mode ='r')as file:    
  # odczytanie pliku
    csvFile = csv.reader(file) 
    
  # wynik czytania na console 
    for lines in csvFile: 
      print(lines)
    