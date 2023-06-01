# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

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
    is_matched_inteface = False
    matched_inteface = ''

    
    for line in config_file:
        try:
            match_ip = re.search('\d+[.]\d+[.]\d+[.]\d+\s\d+[.]\d+[.]\d+[.]\d+', line)
            match_inteface = re.search('^interface', line)

            if match_inteface:
                is_matched_inteface = True
                matched_inteface = line.split(' ')[1][:-1]

            if match_ip and is_matched_inteface:
                one_result = match_ip.group().split(' ')
                result.append((matched_inteface, (one_result[0], one_result[1])))

            if re.search('^!', line):
                is_matched_inteface = False

        except(IndexError):
            continue
    
    return dict(result)

print(get_ip_from_cfg('config_r1.txt'))