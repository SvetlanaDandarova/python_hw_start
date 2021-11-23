revenue = float(input('Введите размер выручки '))
cost = float(input('Введите размер издержек '))
result = revenue-cost
if result > 0:
    print(f" прибыль составляет {result}")
    print(f"рентабельность составила - {result/revenue:.2f}")
    persons = int(input('Введите количество работников '))
    print(f"Прибыль на одного работника - {result/persons:.2f}")
elif result < 0:
    print(f"Убыток составил - {result}")
else:
    print(f"Результат ноль - это точка безубыточности")