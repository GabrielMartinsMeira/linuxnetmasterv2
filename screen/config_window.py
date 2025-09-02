import customtkinter as ctk
from config.config import load_interfaces, write_interfaces

def open_new_window(MainWindow, button_conf):
    interfaces = ["Interface_AC", "Interface_AX", "Interface_USB", "Interface_LAN"]
    
    button_conf.configure(state="disabled")
    # Janela principal
    root = ctk.CTkToplevel(MainWindow)
    root.title("Configuração")
    root.geometry("400x450")
    root.configure(fg="#ffffff")
    root.attributes("-topmost", True)
    
    # Não deixa redimencionar a tela
    root.resizable(False, False)
    
    # Função para carregar as informações do arquivo
    def carregar_informacoes():
        interfaces_names = load_interfaces()
        for index, interface_entry in enumerate(interfaces_entries):
            interface_entry.insert(0, interfaces_names[index])

    # Função para salvar as informações em um arquivo
    def salvar_informacoes():
        interfaces_names = []
        for interface_entry in interfaces_entries:
            interface_name = interface_entry.get()
            interfaces_names.append(interface_name)
            
        write_interfaces(interfaces_names)
        print("Informações salvas com sucesso!")
        button_conf.configure(state="normal")
        root.destroy()
    # Frame para as entradas
    frame = ctk.CTkFrame(root, corner_radius=10, fg_color="#D9D9D9")
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Entradas de texto
    interface_ac = ctk.CTkLabel(frame, text="Interface AC:", text_color="#000000")
    interface_ac.pack(pady=5)
    entry_interface_ac = ctk.CTkEntry(frame)
    entry_interface_ac.pack(pady=5)

    interface_ax = ctk.CTkLabel(frame, text="Interface AX:", text_color="#000000")
    interface_ax.pack(pady=5)
    entry_interface_ax = ctk.CTkEntry(frame)
    entry_interface_ax.pack(pady=5)

    interface_usb = ctk.CTkLabel(frame, text="Interface USB:", text_color="#000000")
    interface_usb.pack(pady=5)
    entry_interface_usb = ctk.CTkEntry(frame)
    entry_interface_usb.pack(pady=5)
    
    interface_lan = ctk.CTkLabel(frame, text="Interface LAN:", text_color="#000000")
    interface_lan.pack(pady=5)
    entry_interface_lan = ctk.CTkEntry(frame)
    entry_interface_lan.pack(pady=5)

    interfaces_entries = [entry_interface_ac, entry_interface_ax, entry_interface_usb, entry_interface_lan]
    
    # Botão de salvar
    save_button = ctk.CTkButton(frame, text="Salvar", command=salvar_informacoes)
    save_button.pack(pady=20)

    # Carregar informações do arquivo ao iniciar
    
    carregar_informacoes()
    root.protocol("WM_DELETE_WINDOW", lambda: close_config_window(root, button_conf))
    
    # Iniciar o loop principal
    root.mainloop()

def close_config_window(root, button_conf):
    button_conf.configure(state="normal")
    root.destroy()
    root = None

