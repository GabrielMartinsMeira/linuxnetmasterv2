#!/bin/bash

# Caminho para o arquivo de configuração
current_dir=$(pwd)
config_file="$current_dir/scripts/configuracoes.txt"

interface_lan=$(grep "Interface LAN:" "$config_file" | cut -d':' -f2 | xargs)

sudo ip netns exec lan ip link set ${interface_lan} netns 1
sudo ip -all netns delete
echo "Namespace Deletado"