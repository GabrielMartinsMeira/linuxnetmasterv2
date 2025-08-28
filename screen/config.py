import customtkinter as ctk
import tkinter as tk
from PIL import Image
from os import path, getcwd

def open_new_window():
    import customtkinter as ctk

    # Configurações iniciais
    #ctk.set_appearance_mode("light")
    #ctk.set_default_color_theme("blue")

    # Janela principal
    root = ctk.CTk()
    root.title("Configuração")
    root.geometry("400x450")
    root.configure(fg="#ffffff")
    
    # Não deixa redimencionar a tela
    root.resizable(False, False)

    # Função para carregar as informações do arquivo
    def carregar_informacoes():
        if path.exists(path.join(getcwd(), "scripts", "configuracoes.txt")):
            with open(path.join(getcwd(), "scripts", "configuracoes.txt"), "r") as file:
                lines = file.readlines()
                if len(lines) >= 4:
                    entry1.insert(0, lines[0].strip().split(": ")[1])
                    entry2.insert(0, lines[1].strip().split(": ")[1])
                    entry3.insert(0, lines[2].strip().split(": ")[1])
                    entry4.insert(0, lines[3].strip().split(": ")[1])

    # Função para salvar as informações em um arquivo
    def salvar_informacoes():
        item1 = entry1.get()
        item2 = entry2.get()
        item3 = entry3.get()
        item4 = entry4.get()

        with open(path.join(getcwd(), "scripts", "configuracoes.txt"), "w") as file:
            file.write(f"Interface AC: {item1}\n")
            file.write(f"Interface AX: {item2}\n")
            file.write(f"Interface USB: {item3}\n")
            file.write(f"Interface LAN: {item4}\n")
        print("Informações salvas com sucesso!")
        root.destroy()
    # Frame para as entradas
    frame = ctk.CTkFrame(root, corner_radius=10, fg_color="#D9D9D9")
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Entradas de texto
    label1 = ctk.CTkLabel(frame, text="Interface AC:", text_color="#000000")
    label1.pack(pady=5)
    entry1 = ctk.CTkEntry(frame)
    entry1.pack(pady=5)

    label2 = ctk.CTkLabel(frame, text="Interface AX:", text_color="#000000")
    label2.pack(pady=5)
    entry2 = ctk.CTkEntry(frame)
    entry2.pack(pady=5)

    label3 = ctk.CTkLabel(frame, text="Interface USB:", text_color="#000000")
    label3.pack(pady=5)
    entry3 = ctk.CTkEntry(frame)
    entry3.pack(pady=5)
    
    label4 = ctk.CTkLabel(frame, text="Interface LAN:", text_color="#000000")
    label4.pack(pady=5)
    entry4 = ctk.CTkEntry(frame)
    entry4.pack(pady=5)

    # Botão de salvar
    save_button = ctk.CTkButton(frame, text="Salvar", command=salvar_informacoes)
    save_button.pack(pady=20)

    # Carregar informações do arquivo ao iniciar
    carregar_informacoes()

    # Iniciar o loop principal
    root.mainloop()
