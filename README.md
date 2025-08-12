# Linux Net Master

Linux Net Master é uma interface gráfica desenvolvida em Python usando `customtkinter` para gerenciar interfaces de rede em sistemas Linux. O software permite executar scripts de rede, comandos no terminal, e visualizar informações sobre as interfaces de rede disponíveis.

## Funcionalidades

- **Execução de Comandos no Terminal**: 
  - `iperf`: Inicia um servidor iperf3 em uma nova instância do terminal GNOME.
  - `iperf_plug`: Inicia um servidor iperf3 dentro de um namespace de rede específico usando `sudo ip netns exec`.

- **Gerenciamento de Interfaces de Rede**:
  - Desabilitar interfaces de rede através do script `disable_interfaces.sh`.
  - Resetar interfaces de rede através do script `reset_all.sh`.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **customtkinter**: Biblioteca para construção da interface gráfica.
- **tkinter**: Utilizada em conjunto com o customtkinter.
- **subprocess**: Executa comandos do sistema e scripts.
- **Pillow (PIL)**: Manipulação de imagens usadas na interface.
  
## Pré-requisitos

- Python 3.x instalado no sistema.
- Instalação das dependências listadas no arquivo `requirements.txt`.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/darckness/LinuxNetMaster.git
