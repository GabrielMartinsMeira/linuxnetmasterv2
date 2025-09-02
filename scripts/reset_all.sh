#!/bin/bash

# Caminho para o arquivo de configuração
current_dir=$(pwd) 
config_file="$current_dir/config/configuracoes.conf"

# Ler os valores do arquivo de configuração
interface_ac=$(grep "interface_ac =" "$config_file" | cut -d'=' -f2 | xargs)
interface_ax=$(grep "interface_ax =" "$config_file" | cut -d'=' -f2 | xargs)
interface_usb=$(grep "interface_usb =" "$config_file" | cut -d'=' -f2 | xargs)

sudo ifconfig ${interface_ax} up
sudo ifconfig ${interface_ac} up
sudo ifconfig ${interface_usb} up 
echo "interface"