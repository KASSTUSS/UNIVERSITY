# -*- coding: utf-8 -*-
'''
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


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
    matched_inteface = False
    
    for line in config_file:
        try:
            match_ip = re.search('\d+[.]\d+[.]\d+[.]\d+\s\d+[.]\d+[.]\d+[.]\d+', line)
            match_inteface = re.search('^interface', line)

            if match_inteface:
                matched_inteface = True

            if match_ip and matched_inteface:
                one_result = match_ip.group().split(' ')
                result.append((one_result[0], one_result[1]))

            if re.search('^!', line):
                matched_inteface = False

        except(IndexError):
            continue
    
    return result

print(get_ip_from_cfg('config_r1.txt'))