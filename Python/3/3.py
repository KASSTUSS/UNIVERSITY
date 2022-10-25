def get_int_vlan_map(file_name):
    try:
        config_file = open(file_name, 'r')
    except FileNotFoundError:
        print(f"File {file_name} is not found!")
        return False

    ints = list(filter(None, list(map(lambda int: [i for i in int.split()] if "interface" in int and "Ethernet" in int and "switchport" in int else '', config_file.read().replace("\n","").split("!")))))

    return tuple([dict([tuple([i[1],i[8]]) for i in list(filter(lambda int: int if "access" in int else '', ints))]), dict([tuple([i[1],[j for j in i[10].split(',')]]) for i in list(filter(lambda int: int if "trunk" in int else '', ints))])])

file = 'config_sw1.txt'
print(get_int_vlan_map(file))