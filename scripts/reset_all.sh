#!/bin/bash

# Caminho para o arquivo de configuração
current_dir=$(pwd) 
config_file="$current_dir/scripts/configuracoes.txt"

interface_ac=$(grep "Interface AC:" "$config_file" | cut -d':' -f2 | xargs)
interface_ax=$(grep "Interface AX:" "$config_file" | cut -d':' -f2 | xargs)
interface_usb=$(grep "Interface USB:" "$config_file" | cut -d':' -f2 | xargs)
interface_lan=$(grep "Interface LAN:" "$config_file" | cut -d':' -f2 | xargs)

sudo ifconfig ${interface_ax} up
sudo ifconfig ${interface_ac} up
sudo ifconfig ${interface_usb} up 
echo "interface"