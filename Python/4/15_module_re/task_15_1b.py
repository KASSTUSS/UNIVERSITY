# -*- coding: utf-8 -*-
'''
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом, чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re

def get_ip_from_cfg(file_name):
    try:
        config_file = open(file_name, 'r')
    except FileNotFoundError:
        print(f"File {file_name} is not found!")
        return False
    
    result = list()
    is_matched_inteface = False
    matched_inteface = ''
    matched_ip = list()

    
    for line in config_file:
        try:
            match_ip = re.search('\d+[.]\d+[.]\d+[.]\d+\s\d+[.]\d+[.]\d+[.]\d+', line)
            match_inteface = re.search('^interface', line)

            if match_inteface:
                is_matched_inteface = True
                matched_inteface = line.split(' ')[1][:-1]

            if match_ip and is_matched_inteface:
                one_result = match_ip.group().split(' ')
                matched_ip.append((one_result[0], one_result[1]))

            if re.search('^!', line):
                if len(matched_ip) > 0:
                    result.append((matched_inteface, matched_ip))
                is_matched_inteface = False
                matched_ip = list()
                

        except(IndexError):
            continue
    
    return dict(result)

print(get_ip_from_cfg('config_r2.txt'))