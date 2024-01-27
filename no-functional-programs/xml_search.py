import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk

def find_in_xml(where, what):
    zasoby_elements = root.findall(".//Zasoba")
    results_text.delete(1.0, tk.END)

    for zasoba_element in zasoby_elements:
        zkrat_element = zasoba_element.find(where)

        if zkrat_element is not None:
            to_find = str(zkrat_element.text)

            if to_find.find(what) != -1:
                display_result(zasoba_element)
            else:
                continue
        else:
            continue

def display_result(zasoba_element):
    katalog = zasoba_element.find(".//Katalog")
    popis = zasoba_element.find(".//Popis")
    popis1 = zasoba_element.find(".//Popis1")
    popis2 = zasoba_element.find(".//Popis2")
    popis3 = zasoba_element.find(".//Popis3")

    result_text = f"Katalog: {katalog.text if katalog is not None else 'Nenalezen'}\n"
    result_text += f"Popis: {popis.text if popis is not None else 'Nenalezen'}\n"
    result_text += f"Popis1: {popis1.text if popis1 is not None else 'Nenalezen'}\n"
    result_text += f"Popis2: {popis2.text if popis2 is not None else 'Nenalezen'}\n"
    result_text += f"Popis3: {popis3.text if popis3 is not None else 'Nenalezen'}\n\n"

    results_text.insert(tk.END, result_text)

def search_button_click():
    user_input = entry.get()
    find_in_xml(selected_element.get(), user_input)

tree = ET.parse('money-zasoby-vzor.xml')
root = tree.getroot()

window = tk.Tk()
window.title("XML Search Tool")

entry = tk.Entry(window, width=30)
entry_label = tk.Label(window, text="Zadej text který hledáš:")
entry_label.grid(row=0, column=0, pady=10)
entry.grid(row=0, column=1, pady=10)

elements = [".//WWWPopis", ".//WWWPopis2", ".//Pozn", ".//Pozn1", ".//Pozn2", ".//Pozn3"]
selected_element = ttk.Combobox(window, values=elements, state="readonly")
selected_element.set(elements[0])  
element_label = tk.Label(window, text="Vyber XML element:")
element_label.grid(row=1, column=0, pady=10)
selected_element.grid(row=1, column=1, pady=10)

search_button = tk.Button(window, text="Search", command=search_button_click)
search_button.grid(row=2, column=0, columnspan=2, pady=10)

results_text = tk.Text(window, height=10, width=50)
results_text.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
