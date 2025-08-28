import customtkinter as ctk
import tkinter as tk
import subprocess
import asyncio
from PIL import Image
from os import path, getcwd
from screen.config import open_new_window
from screen.ips import openipview

# Configurações iniciais
ctk.set_appearance_mode("dark")  # Modo escuro
#ctk.set_default_color_theme("red")  # Tema vermelho

def iperf():
    try:
        # Executa o comando para abrir o terminal e listar o conteúdo
        subprocess.run(["gnome-terminal", "--", "bash", "-c", "iperf3 -s; exec bash"], check=True)
        print("Terminal GNOME iniciado com o comando `ls`.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
        
def iperf_plug(MainWindow):
    try:
        subprocess.run(["/bin/bash", path.join(getcwd(), "scripts", "create_namespace.sh")], check=True)
        print("Criando namespaces")
        process = subprocess.Popen(
                ["gnome-terminal", "--wait", "--", "bash", "-c", "sudo ip netns exec lan iperf3 -s; exec bash"],  # Windows example
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
        for line in process.stdout:
            print(line, end="")
            
        process.wait()
        print("Terminal Fechado")
        subprocess.run(["/bin/bash", path.join(getcwd(), "scripts", "disable_namespace.sh")], check=True)
        
        #subprocess.run(["gnome-terminal", "--", "bash", "-c", "sudo ip netns exec lan iperf3 -s; exec bash"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")

# Janela principal
root = ctk.CTk()
root.title("LinuxNetMaster")
root.geometry("1000x700")
root.configure(bg="#000000")

# Nao deixa redimencionar a tela
root.resizable(False, False)

# Carregar as imagens
#folder_image_path = "img/AQlogo.png"
image_path = ctk.CTkImage(light_image=Image.open(path.join(getcwd(), "img", "AQlogo.png")), size=(40, 40))

#folder_image_chave = "img/chave.png"
image_chave = ctk.CTkImage(light_image=Image.open(path.join(getcwd(), "img", "chave.png")), size=(35, 35))

#folder_image_iperf = "img/iperf.png"
image_iperf = ctk.CTkImage(light_image=Image.open(path.join(getcwd(), "img", "iperf.png")), size=(35, 30))

#folder_image_iperf_plug = "img/plug.png"
image_iperf_plug = ctk.CTkImage(light_image=Image.open(path.join(getcwd(), "img", "plug.png")), size=(55, 55))

#folder_ips = "img/IPs.png"
image_ips = ctk.CTkImage(light_image=Image.open(path.join(getcwd(), "img", "IPs.png")), size=(25, 45))

# Frame superior
top_frame = ctk.CTkFrame(root, fg_color='#65B46B', corner_radius=0, height=100)
top_frame.pack(side=ctk.TOP, fill='x', expand=False)

# Adicionando elementos na barra superior
img_label = ctk.CTkLabel(top_frame, image=image_path, text="", text_color='black', font=("Arial", 16, "bold"))
img_label.pack(side=ctk.LEFT, padx=20, pady=10)

software_name_label = ctk.CTkLabel(top_frame, text="Linux Net Master", text_color='white', font=("Tahoma", 20, "bold"))
software_name_label.pack(side=ctk.LEFT, padx=20, pady=10)

# Frame esquerdo para os botões
left_frame = ctk.CTkFrame(root, fg_color='#585858', corner_radius=0, width=70)
left_frame.pack(side=ctk.LEFT, fill=ctk.Y, padx=0, pady=0)

# Botões na barra lateral esquerda
button_conf = ctk.CTkButton(left_frame, image=image_chave, text="", command=open_new_window, width=10, height=40, fg_color='#585858', text_color='black', hover_color="#727171", corner_radius=8)
button_conf.pack(pady=25, padx=10)

button_iperf = ctk.CTkButton(left_frame, image=image_iperf, text="", command=iperf, width=10, height=40, fg_color='#585858', text_color='black', hover_color='#727171', corner_radius=8)
button_iperf.pack(pady=25, padx=10)

button_iperf = ctk.CTkButton(left_frame, image=image_iperf_plug, text="", command=lambda *args: iperf_plug(root), width=0, height=0, fg_color='#585858', text_color='black', hover_color='#727171', corner_radius=8)
button_iperf.pack(pady=25, padx=10)

button_ip = ctk.CTkButton(left_frame, image=image_ips, text="", command=openipview, width=10, height=40, fg_color='#585858', text_color='black', hover_color='#727171', corner_radius=8)
button_ip.pack(pady=25, padx=10)

# Frame central para os elementos principais
center_frame = ctk.CTkFrame(root, fg_color='#474747', corner_radius=0)
center_frame.pack(side=ctk.TOP, pady=0, fill='both', expand=True)


# Adicionando caixas de texto
texts = [                                                                                          
    "Placa AC", "Placa AX", "Placa AC USB"
]

# Função para desabilitar as interfaces de rede
def disable(i):
    try:
        # Executa o script disable_interfaces.sh
        subprocess.run(["/bin/bash", path.join("scripts", "disable_interfaces.sh"), str(i)], check=True)
        print("Desabilitando interfaces...", i)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")
    

 # Função para reset das interfaces de rede
def reset():
    try:
        # Executa o script reset_script.sh
        subprocess.run(["/bin/bash", path.join("scripts", "reset_all.sh"), str(i)], check=True)
        print("Resetando interfaces...")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")
        
def change_box_color(box_frame, color):
    box_frame.configure(fg_color=color)



row = 0
column = 0
box_frames = []  # Lista para armazenar os frames
selected_box = [None]  # Usando lista mutável para referência
buttons = []

for i, text in enumerate(texts):
    if column == 3:  # Ajusta para 3 colunas
        row += 1
        column = 0

    box_frame = ctk.CTkFrame(center_frame, fg_color='#BDBDBD', width=230, height=350, corner_radius=20)
    box_frame.grid(row=row, column=column, padx=(80, 0), pady=(120, 0))
    box_frames.append(box_frame)  # Adiciona o frame à lista

    label = ctk.CTkLabel(box_frame, text=text, fg_color='white', text_color='black', font=("Arial", 12), corner_radius=17, height=40, width=100)
    label.pack(fill=ctk.X, pady=(20, 20), padx=(10, 10))
    #label.pack(fill=ctk.X, pady=(10, 90), padx=(10, 10))
    

    
    # Botoes antigos sem alteração da cor na tela.
    
    #button = ctk.CTkButton(box_frame, text="Reset", command=lambda i=i+1: reset(i), width=100, height=30, fg_color='white', text_color='black')
    #button.pack(pady=0)

    #button = ctk.CTkButton(box_frame, text="Execute", command=lambda i=i+1: disable(i), width=100, height=30)
    #button.pack(pady=8)
    
    # Botão de Reset que altera a cor e chama a função reset(i)
    #reset_button = ctk.CTkButton(
    #    box_frame, 
    #    text="Reset", 
    #    command=lambda i=i+1, box=box_frame: [reset(i), change_box_color(box, '#00c4ff')], 
    #    width=100, 
    #    height=30, 
    #    fg_color='white', 
    #    text_color='black'
    #)
    #reset_button.pack(pady=0)

    # Botão de Execute que altera a cor e chama a função disable(i)
    def on_execute(selected_idx=i):
        if selected_box[0] == selected_idx:
            # Se já está selecionado, reseta todos
            for frame in box_frames:
                change_box_color(frame, '#BDBDBD')
            for button in buttons:
                button.configure(fg_color="#329932", hover_color='#227422', text="Habilitar interface", state="normal")
                
            selected_box[0] = None
            reset()
            
        else:
            for idx, frame in enumerate(box_frames):
                if idx == selected_idx:
                    change_box_color(frame, '#BDBDBD')  # Cor padrão
                    buttons[selected_idx].configure(fg_color="#C23434", hover_color="#971818", text="Desabilitar interface")
                    
                else:
                    change_box_color(frame, "#585858")  # Cinza escuro
                    buttons[idx].configure(state='disabled')
                    
            selected_box[0] = selected_idx
            disable(selected_idx + 1)

    execute_button = ctk.CTkButton(
        box_frame, 
        text="Habilitar interface", 
        command=on_execute, 
        width=150, 
        height=30,
        fg_color='#329932', 
        hover_color='#227422', 
        text_color='white',
        font=("Arial", 12, "bold"),
        corner_radius=10
    )
    execute_button.pack(pady=(50, 0))
    buttons.append(execute_button)
    
    label_id = ctk.CTkLabel(box_frame, text=["ID:", (i+1)], fg_color='#BDBDBD', text_color='black', font=("Arial", 14), corner_radius=30, height=30, width=180)
    label_id.pack(fill=ctk.X, pady=(10, 10), padx=(10, 10))

    column += 1


root.mainloop()