import xml.etree.cElementTree as ET
import csv

tree = ET.parse('DLTINS_20210117_01of01.xml')
root = tree.getroot()
xml_data_to_csv = open('Out.csv', 'w')
list_head = []
Csv_writer = csv.writer(xml_data_to_csv)
count = 0
for element in root.findall("FinInstrmGnlAttrbts"):
    List_nodes = []
# Get head by tag
    if count == 0:
        Id = element.find('Id').tag
        list_head.append(Id)

        FullNm = element.find('FullNm').tag
        list_head.append(FullNm)

        ClssfctnTp = element.find('ClssfctnTp').tag
        list_head.append(ClssfctnTp)
        Csv_writer.writerow(list_head)
        count = +1

    # get child node
Id = element.find('Id').text
List_nodes .append(Id)

FullNm = element.find('FullNm').text
List_nodes .append(FullNm)

ClssfctnTp = element.find('ClssfctnTp').text
List_nodes .append(ClssfctnTp)

Csv_writer.writerow(List_nodes)
xml_data_to_csv.close()
