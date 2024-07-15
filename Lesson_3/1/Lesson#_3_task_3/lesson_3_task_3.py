from Address import Address
from Mailing import Mailing

to_address = Address("601240", "Владимир", "Верхняя-Дуброва", "13Б", "221")
from_address = Address("231678", "Суздаль", "Ленина", "11", "93")
mailing = Mailing(to_address, from_address, 500, "FDS345")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house}, {mailing.from_address.apartment} "
      f" в {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street},"
      f" {mailing.from_address.house}, {mailing.from_address.apartment}. Стоимость {mailing.cost} рублей. ")