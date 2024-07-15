def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    if month in [3, 4, 5]:
        return "Весна"
    if month in [6, 7, 8]:
        return "Лето"
    if month in [9, 10, 11]:
        return "Осень"
    
print(month_to_season(1))
print(month_to_season(5))
print(month_to_season(8))
print(month_to_season(11))
print(month_to_season(19))