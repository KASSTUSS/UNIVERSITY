"""Задания выполнил студент группы МС-32 Чвалов Кастусь Русланович"""

"""
EX 3.1
-------
Обработать строку NAT таким образом, чтобы в имени интерфейса вместо
FastEthernet было GigabitEthernet.
"""
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('Fast','Gigabit')
print(NAT)


"""
EX 3.2
-------
Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат
XXXX.XXXX.XXXX
"""
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':','.')
print(MAC)


"""
EX 3.3
-------
Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']
"""
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print(CONFIG.split()[-1].split(','))


"""
EX 3.4
-------
Из строк command1 и command2 получить список VLANов, которые есть и в команде
command1 и в команде command2.
Для данного примера, результатом должен быть список: [1, 3, 100] Этот список
содержит подсказку по типу итоговых данных.
"""
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
print(list(set(command1.split()[-1].split(',')) & set(command2.split()[-1].split(','))))


"""
EX 3.5
-------
Список VLANS это список VLANов, собранных со всех устройств сети, поэтому в
списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по
возрастанию номеров.
"""
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(list(set(VLANS))))


"""
EX 3.6
-------
Обработать строку ospf_route и вывести информацию в виде:
Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0

"""
inf = ['Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:','Last update:','Outbound Interface:']
ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route_list = ospf_route.replace(',','').split()
ospf_route_list[2] = ospf_route_list[2].strip('[]')

print('\n'.join([''.join([f'{x:24}' for x in r]) for r in list(zip(inf,ospf_route_list))]))



"""
EX 3.7
-------
Преобразовать MAC-адрес в двоичную строку (без двоеточий).

"""
MAC = 'AAAA:BBBB:CCCC'
MAC = ''.join(bin(int(x,16))[2:].zfill(8) for x in MAC.split(':'))

print(MAC)


"""
EX 3.8
-------
Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод
столбцами, таким образом:
    -первой строкой должны идти десятичные значения байтов
    -второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
    -столбцами
    -ширина столбца 10 символов
Пример вывода:
10       1        1        1
00001010 00000001 00000001 00000001

"""
IP = '192.168.3.1'
res = ''.join([f'{x:10}' for x in IP.split('.')])+'\n'+ ' '.join(bin(int(x,16))[2:].zfill(9) for x in IP.split('.'))

print(res)


"""
EX 3.9
-------
Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в
списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в
конкретном списке) и проверить на двух списках, которые указаны и на разных
элементах.

"""
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

def lastElem(list, elem):
    return len(list)-1-list[::-1].index(elem)

print(lastElem(num_list,10), ' ', lastElem(word_list,'python'))
