#!/bin/bash

current_dir=$(pwd)  # get current working directory
config_file="$current_dir/config/configuracoes.conf"

interface_lan=$(grep "interface_lan = " "$config_file" | cut -d'=' -f2 | xargs)

sudo ip netns add lan
sudo ip link set ${interface_lan} netns lan
sudo ip netns exec lan ip link set ${interface_lan} up
sudo ip netns exec lan dhclient
echo "Rede AC 2.4 Plug Configurada"