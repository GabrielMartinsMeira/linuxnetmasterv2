from configparser import ConfigParser
from os import path, getcwd

def update_conf_file():
    config = ConfigParser()
    config.read(path.join(getcwd(), "config","configuracoes.conf"))
    return config

def get_iperf_plug_server():
    config = update_conf_file()
    is_running_plug = config.getboolean("General", "plug_iperf_server")
    return is_running_plug

def set_iperf_plug_server(bool):
    config = update_conf_file()
    config.set("General", "plug_iperf_server", bool)
    with open(path.join(getcwd(), "config", "configuracoes.conf"), "w") as configfile:
        config.write(configfile)
        
def load_interfaces():
    interfaces_names = []
    config = update_conf_file()
    for interface in config.options("Interfaces"):
        interfaces_names.append(config.get("Interfaces", interface))
    return interfaces_names

def write_interfaces(interfaces_names):
    config = update_conf_file()
    for index, interface in enumerate(config.options("Interfaces")):
        config.set("Interfaces", interface, interfaces_names[index])
        with open(path.join(getcwd(), "config", "configuracoes.conf"), "w") as configfile:
            config.write(configfile)