#!/bin/bash

# Caminho para o arquivo de configuração
current_dir=$(pwd)
config_file="$current_dir/config/configuracoes.conf"

# Ler os valores do arquivo de configuração
interface_lan=$(grep "interface_lan =" "$config_file" | cut -d'=' -f2 | xargs)

sudo ip netns exec lan ip link set ${interface_lan} netns 1
sudo ip -all netns delete
echo "Namespace Deletado"