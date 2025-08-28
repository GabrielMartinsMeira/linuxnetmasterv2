#!/bin/bash

# Caminho para o arquivo de configuração
current_dir=$(pwd)  # get current working directory
config_file="$current_dir/scripts/configuracoes.txt"
# config_file="/home/tibo/Documentos/LinuxNetMaster/scripts/configuracoes.txt"

# Ler os valores do arquivo de configuração
interface_ac=$(grep "Interface AC:" "$config_file" | cut -d':' -f2 | xargs)
interface_ax=$(grep "Interface AX:" "$config_file" | cut -d':' -f2 | xargs)
interface_usb=$(grep "Interface USB:" "$config_file" | cut -d':' -f2 | xargs)
interface_lan=$(grep "Interface LAN:" "$config_file" | cut -d':' -f2 | xargs)

echo ${interface_ac}, ${interface_ax}, ${interface_usb}
# Definição passada como argumento
definicao="$1"

function desabilitar_IEEE_802_11b_g_n_only_2_4 {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
    echo "Rede AC Somente 2.4 Configurada"
}

function desabilitar_IEEE_802_11b_g_n_2_4_usb {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_ac} down
    echo "Rede USB Configurada" 
}

function desabilitar_IEEE_802_11a_g_n_ac_2_4_plug {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
    sudo ip netns add lan
    sudo ip link set ${interface_lan} netns lan
    sudo ip netns exec lan ip link set ${interface_lan} up
    sudo ip netns exec lan dhclient
    echo "Rede AC 2.4 Plug Configurada"
}

function desabilitar_IEEE_802_11a_b_g_n_ac_2_4 {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
    echo "Rede AC 2.4 Configurada"
}

function desabilitar_IEEE_802_11a_b_g_n_ac_5g {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
    echo "Rede AC 5GHZ Configurada"
}

function desabilitar_IEEE_802_11a_b_g_n_ac_ax_5g {
    sudo ifconfig ${interface_ac} down
    sudo ifconfig ${interface_usb} down
    echo "Rede AX 5Ghz Configurada"
}

case "$definicao" in 

    1)
    desabilitar_IEEE_802_11b_g_n_only_2_4
    ;;

    2)
    desabilitar_IEEE_802_11b_g_n_2_4_usb
    ;;

    3)
    desabilitar_IEEE_802_11a_g_n_ac_2_4_plug
    ;;

    4)
    desabilitar_IEEE_802_11a_b_g_n_ac_2_4
    ;;

    5)
    desabilitar_IEEE_802_11a_b_g_n_ac_5g
    ;;

    6)
    desabilitar_IEEE_802_11a_b_g_n_ac_ax_5g
    ;;

esac