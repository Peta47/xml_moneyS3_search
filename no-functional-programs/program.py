import xml.etree.ElementTree as ET

tree = ET.parse('money-zasoby-vzor.xml')
root = tree.getroot()


def find(where, what):

    zasoby_elements = root.findall(".//Zasoba")

    for zasoba_element in zasoby_elements:
        zkrat_element = zasoba_element.find(where)
        
        if zkrat_element is not None:
            to_find = str(zkrat_element.text)
            
            if to_find.find(what) != -1:
                katalog = zasoba_element.find(".//Katalog")
                if katalog is not None:
                    try:
                        katalog_value = str(katalog.text)
                        print(f"katalog : {katalog_value}")
                    except AttributeError:
                        print("Chyba při čtení hodnoty Katalog.")
                else:
                    print("Katalog nenalezen.")

                popis = zasoba_element.find(".//Popis")
                if popis is not None:
                    try:
                        popis_value = str(popis.text)
                        print(f"popis : {popis_value}")
                    except AttributeError:
                        print("Chyba při čtení hodnoty Popis.")
                else:
                    print("Popis nenalezen.")

                popis1 = zasoba_element.find(".//Popis1")
                if popis1 is not None:
                    try:
                        popis1_value = str(popis1.text)
                        print(f"popis1 : {popis1_value}")
                    except AttributeError:
                        print("Chyba při čtení hodnoty Popis1.")
                else:
                    print("Popis1 nenalezen.")

                popis2_element = zasoba_element.find(".//Popis2")
                if popis2_element is not None:
                    try:
                        popis2 = str(popis2_element.text)
                        print(f"popis2 : {popis2}")
                    except AttributeError:
                        print("Chyba při čtení hodnoty Popis2.")
                else:
                    print("Popis2 nenalezen.")

                popis3 = zasoba_element.find(".//Popis3")
                if popis3 is not None:
                    try:
                        popis3_value = str(popis3.text)
                        print(f"popis3 : {popis3_value}")
                    except AttributeError:
                        print("Chyba při čtení hodnoty Popis3.")
                else:
                    print("Popis3 nenalezen.")
                print("")

            else:
                continue
        else:
            continue

WWWPopis = ".//WWWPopis"
WWWPopis2 = ".//WWWPopis2"
Pozn = ".//Pozn"
Pozn1 = ".//Pozn1"
Pozn2 = ".//Pozn2"
Pozn3 = ".//Pozn3"

user_input = input("zadej text:\n")

print(f"looking for {user_input} in {WWWPopis}\n")
find(WWWPopis, user_input)

print(f"looking for {user_input} in {WWWPopis2}\n")
find(WWWPopis2, user_input)

print(f"looking for {user_input} in {Pozn}\n")
find(Pozn, user_input)

print(f"looking for {user_input} in {Pozn1}\n")
find(Pozn1, user_input)

print(f"looking for {user_input} in {Pozn2}\n")
find(Pozn2, user_input)

print(f"looking for {user_input} in {Pozn3}\n")
find(Pozn3, user_input)

input("pres ENTER to EXIT")