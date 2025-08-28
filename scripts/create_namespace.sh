current_dir=$(pwd)  # get current working directory
config_file="$current_dir/scripts/configuracoes.txt"
#config_file="/home/tibo/Documentos/LinuxNetMaster/scripts/configuracoes.txt"

interface_ax=$(grep "Interface AX:" "$config_file" | cut -d':' -f2 | xargs)
interface_usb=$(grep "Interface USB:" "$config_file" | cut -d':' -f2 | xargs)
interface_lan=$(grep "Interface LAN:" "$config_file" | cut -d':' -f2 | xargs)



sudo ifconfig ${interface_ax} down
sudo ifconfig ${interface_usb} down
sudo ip netns add lan
sudo ip link set ${interface_lan} netns lan
sudo ip netns exec lan ip link set ${interface_lan} up
sudo ip netns exec lan dhclient
echo "Rede AC 2.4 Plug Configurada"