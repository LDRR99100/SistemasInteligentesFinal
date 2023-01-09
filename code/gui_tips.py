from tkinter import *

root = Tk()
root.title("Programa ABC")
actual_row = 2
actual_column = 1
# ****************** WIDGETS ******************
# Label
new_label = Label(root, text="Hello Wool")

# Entry
# Parámetros variables:
# int -> height, width, borderwidth, columnspan...
# string -> fg, bg, ...
new_input_field = Entry(root, width=50, borderwidth=5)

# Button
# A la llamada de Button(...) se pueden añadir parámetros:
#   (1) padx o pady para aumentar el tamaño del botón
#   (2) status=DISABLED o ENABLED para anular o activar el acceso
#   (3) command=function donde function es la función a ejecutarse tras hacer click en él
#   (4) fg="color" y bg="color" para los colores de la letra y fondo, respectivamente

def click_accept():
    new_label = Label(root, text=new_input_field.get())
    new_label.grid(row=actual_row, column=actual_column)
    #actual_row += 1

def click_erase():
    new_input_field.insert(0, "")

accept_button = Button(root, text="Accept", command=click_accept)
erase_button = Button(root, text="Erase", command=click_erase)

new_input_field.grid(row=0, column=0)
accept_button.grid(row=1, column=0)
erase_button.grid(row=2, column=0)
# Pack hace que el objeto se mantenga en el centro de la ventana
# NOTA: Pack da problemas si se usa junto a GRID
#new_label.pack()

# ****************** GRID ******************
new_label_one = Label(root, text="Bye Wool")
new_label_one.grid(row=5, column=5)
new_label.grid(row=10, column=10)

root.mainloop()