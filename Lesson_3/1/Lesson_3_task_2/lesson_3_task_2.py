from smartphone import Smartpfone

catalog = []
phone1 = Smartpfone("Xiaomi", "Mi 12 Pro", "+7 965 543 32 21")
phone2 = Smartpfone("Samsung", "Galaxy S22", "+7 912 234 45 56")
phone3 = Smartpfone("Apple", "iPhone 15 Pro", "+7 923 567 21 45")
phone4 = Smartpfone("Google", "Pixel 5", "+7 910 610 23 81")
phone5 = Smartpfone("OnePlus", "11 Pro", "+7 987 237 63 98")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")