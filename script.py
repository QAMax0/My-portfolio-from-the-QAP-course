money = float(input())
# 1-й способ через цикл

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
values_per_cent = list(per_cent.values())
depo = [i * (money/100) for i in values_per_cent]
print(list(map(int, depo)))
Deposits_max = max(list(map(int, depo)))

print('Максимальная сумма, которую вы можете заработать —', Deposits_max)

# 2-й способ через get()

A = per_cent.get('ТКБ')
TKB = money * A/100
B = per_cent.get('СКБ')
SKB = money * B/100
C = per_cent.get('ВТБ')
VTB = money * C/100
D = per_cent.get('СБЕР')
SBERBANK = money * D/100
deposit = [TKB, SKB, VTB, SBERBANK]

print(list(map(int, deposit)))
print(f'Максимальная сумма, которую вы можете заработать — {max(list(map(int, deposit)))}')
