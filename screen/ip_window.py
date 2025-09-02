import customtkinter as ctk
import subprocess
import threading
from config.config import get_iperf_plug_server, load_interfaces

def openipview(MainWindow, button_ip):
    button_ip.configure(state="disabled")
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
                    output_textbox.insert(ctk.END, f"{interface}: {ip_address}" + "\n")
                else:
                    output_textbox.insert(ctk.END, f"{interface}: Sem IP atribuído" + "\n")
            else:
                output_textbox.insert(ctk.END, f"{interface}: Não foi possível consultar" + "\n")
        except subprocess.TimeoutExpired:
            output_textbox.insert(ctk.END, f"{interface}: Timeout (3s)" + "\n")
        
    def consultar_ip_plug(output_textbox):
        try:
            if get_iperf_plug_server():
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
                        output_textbox.insert(ctk.END, f"Interface Plug: {ip_address}" + "\n")
                    else:
                        output_textbox.insert(ctk.END, "Interface Plug: Sem IP atribuído" + "\n")
                else:
                    output_textbox.insert(ctk.END, "Interface Plug: Não foi possível consultar" + "\n")
        except subprocess.TimeoutExpired:
            output_textbox.insert(ctk.END, "Interface Plug: Timeout (3s)" + "\n")

    # Função para ler o arquivo e exibir os IPs
    def consultar_interfaces():
        interfaces_names = load_interfaces()
        output_textbox.delete(1.0, ctk.END)  # Limpa a área de texto antes de exibir novos resultados
        for interface in interfaces_names:
            consultar_ip(interface, output_textbox)
        
        consultar_ip_plug(output_textbox)

    # Configuração da interface gráfica
    app = ctk.CTkToplevel(MainWindow)
    app.title("Consultor de IPs")
    app.geometry("500x500")
    app.resizable(False, False)  # Janela com tamanho fixo
    app.attributes("-topmost", True)

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
    
    app.protocol("WM_DELETE_WINDOW", lambda: close_ip_window(app, button_ip))
    
    app.mainloop()

def close_ip_window(app, button_ip):
    button_ip.configure(state="normal")
    app.destroy()
    app = None