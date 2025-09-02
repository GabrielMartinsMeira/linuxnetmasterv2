#!/bin/bash

# Caminho para o arquivo de configuração
current_dir=$(pwd)
config_file="$current_dir/config/configuracoes.conf"

# Ler os valores do arquivo de configuração
interface_ac=$(grep "interface_ac =" "$config_file" | cut -d'=' -f2 | xargs)
interface_ax=$(grep "interface_ax =" "$config_file" | cut -d'=' -f2 | xargs)
interface_usb=$(grep "interface_usb =" "$config_file" | cut -d'=' -f2 | xargs)
interface_lan=$(grep "interface_lan =" "$config_file" | cut -d'=' -f2 | xargs)

echo ${interface_ac}, ${interface_ax}, ${interface_usb}
# Definição passada como argumento
definicao="$1"

# Function for AC interface
function disable_ax_usb {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
    echo "Rede AC Somente 2.4 Configurada"
}

# Function for AX interface
function disable_ac_usb {
    sudo ifconfig ${interface_ac} down
    sudo ifconfig ${interface_usb} down
    echo "Rede AX 5Ghz Configurada"
}

# Function for USB interface
function disable_ac_ax {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_ac} down
    echo "Rede USB Configurada" 
}

case "$definicao" in 

    1)
    disable_ax_usb
    ;;

    2)
    disable_ac_usb
    ;;

    3)
    disable_ac_ax
    ;;

esac