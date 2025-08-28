import customtkinter as ctk
import subprocess
import threading
from os import path, getcwd

def openipview():
    import os

    # Função para consultar o IP de uma interface usando ifconfig
    def consultar_ip(interface):
        try:
            result = subprocess.run(
                ["ifconfig", interface],
                capture_output=True,
                text=True,
                timeout=3
            )
            if result.returncode == 0:
                output = result.stdout
                if 'inet ' in output:
                    ip_address = output.split('inet ')[1].split(' ')[0]
                    return f"{interface}: {ip_address}"
                else:
                    return f"{interface}: Sem IP atribuído"
            else:
                return f"{interface}: Não foi possível consultar"
        except subprocess.TimeoutExpired:
            return f"{interface}: Timeout (3s)"
        
    def consultar_ip_plug():
        try:
            result = subprocess.run(
                ["sudo", "ip", "netns", "exec", "lan", "ifconfig"],
                capture_output=True,
                text=True,
                timeout=3
            )
            if result.returncode == 0:
                output = result.stdout
                if 'inet ' in output:
                    ip_address = output.split('inet ')[1].split(' ')[0]
                    return f"Interface Plug: {ip_address}"
                else:
                    return f"Interface Plug: Sem IP atribuído"
            else:
                return f"Interface Plug: Não foi possível consultar"
        except subprocess.TimeoutExpired:
            return f"Interface Plug: Timeout (3s)"

    # Função para ler o arquivo e exibir os IPs
    def consultar_interfaces():
        with open(path.join(getcwd(), "scripts", "configuracoes.txt"), "r") as file:
            interfaces = [line.split(": ")[1].strip() for line in file.readlines()]
        
        output_textbox.delete(1.0, ctk.END)  # Limpa a área de texto antes de exibir novos resultados
        for interface in interfaces:
            result = consultar_ip(interface)
            output_textbox.insert(ctk.END, result + "\n")
        
        plug = consultar_ip_plug()
        output_textbox.insert(ctk.END, plug + "\n")

    # Configuração da interface gráfica
    app = ctk.CTk()
    app.title("Consultor de IPs")
    app.geometry("500x500")
    app.resizable(False, False)  # Janela com tamanho fixo

    # Estilizando o frame principal
    frame = ctk.CTkFrame(app, corner_radius=15)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Título centralizado com uma fonte maior e em negrito
    label = ctk.CTkLabel(frame, text="Consultar IPs das Interfaces", 
                         font=("Arial", 20, "bold"))
    label.pack(pady=20)

    # Área de saída de texto centralizada com bordas arredondadas
    output_textbox = ctk.CTkTextbox(frame, height=250, corner_radius=10)
    output_textbox.pack(pady=10, padx=20, fill="both", expand=True)

    # Botão de consulta centralizado com um design mais chamativo
    button = ctk.CTkButton(frame, text="Consultar", 
                           font=("Arial", 16), 
                           fg_color="#1a73e8", 
                           hover_color="#155ab6", 
                           command=lambda: threading.Thread(target=consultar_interfaces).start())
    button.pack(pady=20)

    app.mainloop()
