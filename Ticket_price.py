# Задача на расчёт стоимости билетов исходя из данных на входе (возраста и количества билетов).
Number_of_tickets = int(input())
ticket_price = 0
discounted_ticket_prices = None

for i in range(Number_of_tickets):
    Age = int(input())
    if Age < 18:
        ticket_price += 0
    elif 18 <= Age < 25:
        ticket_price += 990
    elif Age >= 25:
        ticket_price += 1390

if Number_of_tickets <= 3:
    print(f'Сумма к оплате = {ticket_price} руб.')
else:
    discounted_ticket_prices = ticket_price - (ticket_price * 0.1)  # Скидка 10% если купил > 3 билетов
    print(f'Сумма к оплате = {discounted_ticket_prices} руб.')
