# app_ui.py
import tkinter as tk
from tkinter import messagebox
from api import get_pokemon_data, get_pokemon_moves, get_pokemon_types, get_pokemon_stats


def get_pokemon_info():
    pokemon = entry.get().strip().lower()
    if not pokemon:
        messagebox.showerror("Error", "Por favor, ingresa el nombre de un Pokémon.")
        return

    # Obtener los datos del Pokémon usando la función del otro archivo
    data = get_pokemon_data(pokemon)
    
    if data is None:
        messagebox.showerror("Error", f"No se encontró el Pokémon '{pokemon}'.")
        return

    # Limpiar el texto existente
    text_output.delete("1.0", tk.END)

    # Mostrar el moveset
    moves = get_pokemon_moves(data)
    text_output.insert(tk.END, f"POKEMON MOVESET FOR {pokemon.upper()}\n")
    for move in moves:
        text_output.insert(tk.END, f"- {move}\n")

    # Mostrar el tipo
    types = get_pokemon_types(data)
    text_output.insert(tk.END, f"\nPOKEMON TYPE FOR {pokemon.upper()}\n")
    for type_ in types:
        text_output.insert(tk.END, f"- {type_}\n")

    # Mostrar las estadísticas
    stats = get_pokemon_stats(data)
    text_output.insert(tk.END, f"\nPOKEMON STATS FOR {pokemon.upper()}\n")
    for stat_name, stat_value in stats.items():
        text_output.insert(tk.END, f"- {stat_name}: {stat_value}\n")

# Crear la ventana principal
root = tk.Tk()
root.title("Pokémon Info App")

# Entrada para el nombre del Pokémon
frame = tk.Frame(root)
frame.pack(pady=10)
label = tk.Label(frame, text="Ingresa el nombre del Pokémon:")
label.pack(side=tk.LEFT, padx=5)
entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=5)
button = tk.Button(frame, text="Buscar", command=get_pokemon_info)
button.pack(side=tk.LEFT, padx=5)

# Área de salida de texto
text_output = tk.Text(root, width=50, height=20, wrap="word", borderwidth=2, relief="solid")
text_output.pack(padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
