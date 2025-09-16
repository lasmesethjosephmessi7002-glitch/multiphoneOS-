# main.py
import tkinter as tk
from phone import Phone
from os_manager import OSManager

# Créer le gestionnaire
manager = OSManager()

# Ajouter des téléphones virtuels
manager.add_phone(Phone("Phone 1", ["Messages", "Camera", "Music"]))
manager.add_phone(Phone("Phone 2", ["Maps", "Browser", "Calculator"]))
manager.add_phone(Phone("Phone 3", ["Games", "Notes", "Gallery"]))

# Interface Tkinter
root = tk.Tk()
root.title("Multiphone OS Prototype")
root.geometry("400x300")
root.configure(bg="#f0f4f7")  # Fond clair agréable

# Label principal
label = tk.Label(root, text=manager.current.get_info(), font=("Arial", 14), bg="#f0f4f7", wraplength=380, justify="center")
label.pack(pady=20)

# Fonction pour changer de téléphone
def switch_phone(i):
    manager.switch_phone(i)
    label.config(text=manager.current.get_info())

# Frame pour les boutons
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=10)

# Création des boutons
for i in range(len(manager.phones)):
    btn = tk.Button(
        button_frame,
        text=f"Switch to Phone {i+1}",
        command=lambda i=i: switch_phone(i),
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        padx=10,
        pady=5
    )
    btn.pack(side="top", fill="x", pady=5, padx=50)

# Lancer l'interface
root.mainloop()
