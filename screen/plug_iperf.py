import customtkinter as ctk
import subprocess
import threading
from os import path

def run_iperf_server(textbox):
    subprocess.run(["/bin/bash", path.join("scripts", "create_namespace.sh")], check=True)
    
    process = subprocess.Popen(
            ["gnome-terminal", "--", "bash", "-c", "sudo ip netns exec lan iperf3 -s; exec bash"],  # Windows example
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
    for line in process.stdout:
        print(line, end="")
        textbox.insert("0.0", line + "\n")
        
    process.wait()

def open_plug_iperf_window(MainWindow):
    app = ctk.CTkToplevel(MainWindow)
    app.title("Consultor de IPs")
    app.geometry("500x500")
    app.resizable(False, False)  # Janela com tamanho fixo
    app.attributes("-topmost", True)
    textbox = ctk.CTkTextbox(app, width=500, height=500, corner_radius=10, font=("Consolas", 12))
    textbox.pack(pady=20)
    textbox.bind("<Button-1>", lambda e: "break")
    textbox.bind("<FocusIn>", lambda e: textbox.master.focus())
    
    threading.Thread(target=run_iperf_server, args=[textbox]).start()
    
    app.mainloop()
    
    