import xml.etree.ElementTree as ET
import tkinter as tk

def find_in_xml(what):
    zasoby_elements = root.findall(".//Zasoba")
    results_text.delete(1.0, tk.END)

    for zasoba_element in zasoby_elements:
        for element_path in elements:
            element = zasoba_element.find(element_path)

            if element is not None:
                to_find = str(element.text)

                if to_find.find(what.lower()) != -1 or to_find.find(what.upper()) != -1:
                    display_result(zasoba_element)
                    break
                else:
                    continue
            else:
                continue

def display_result(zasoba_element):
    katalog = zasoba_element.find(".//Katalog")
    popis = zasoba_element.find(".//Popis")
    wwwpopis = zasoba_element.find(".//WWWPopis")
    wwwpopis2 = zasoba_element.find(".//WWWPopis2")
    pozn = zasoba_element.find(".//Pozn")
    pozn1 = zasoba_element.find(".//Pozn1")
    pozn2 = zasoba_element.find(".//Pozn2")
    pozn3 = zasoba_element.find(".//Pozn3")

    result_text = f"Katalog: {katalog.text if katalog is not None else ''}\n  "
    result_text += f"Popis: {popis.text if popis is not None else ''}\n"
    result_text += f"wwwpopis: {wwwpopis.text if wwwpopis is not None else ''}\n"
    result_text += f"wwwpopis2: {wwwpopis2.text if wwwpopis2 is not None else ''}\n"
    result_text += f"Poznamka: {pozn.text if pozn is not None else ''}\n"
    result_text += f"Poznamka1: {pozn1.text if pozn1 is not None else ''}\n"
    result_text += f"Poznamka2: {pozn2.text if pozn2 is not None else ''}\n"
    result_text += f"Poznamka3: {pozn3.text if pozn3 is not None else ''}\n\n\n\n"
    string = "-" * 100
    result_text += string + "\n\n"

    results_text.insert(tk.END, result_text)
    update_count()

def search_button_click():
    user_input = entry.get()
    find_in_xml(user_input)

def count_search():
    results_text_content = results_text.get(1.0, tk.END)
    count = results_text_content.count("Poznamka3:")
    return f"{count} je pocet"

def update_count():
    count_label.config(text=count_search())


tree = ET.parse('zasoby.xml')
root = tree.getroot()

window = tk.Tk()
window.title("XML Search Tool")

window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

entry = tk.Entry(window, width=80, font=("Courier", 12))
entry_label = tk.Label(window, text="Zadej text který hledáš:", font=("Courier", 12))
entry_label.grid(row=0, column=0, pady=10)
entry.grid(row=0, column=1, pady=10)

elements = [".//WWWPopis", ".//WWWPopis2", ".//Pozn", ".//Pozn1", ".//Pozn2", ".//Pozn3"]

search_button = tk.Button(window, text="Search", command=search_button_click, height=4, width=20, bg='#0f0', font=("Courier", 10))
search_button.grid(row=2, column=0, columnspan=2, pady=10)

results_text = tk.Text(window, height=30, width=120, wrap=tk.WORD)
results_text.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky=tk.W)

scrollbar = tk.Scrollbar(window, command=results_text.yview)
scrollbar.grid(row=4, column=2, pady=10, sticky='ns')

results_text.config(yscrollcommand=scrollbar.set)

count_label = tk.Label(window, text=count_search())
count_label.grid(row=3, column=0, columnspan=2, padx=10)

font = ("Courier", 12)
results_text.configure(font=font)

window.mainloop()