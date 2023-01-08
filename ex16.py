class Metric:

    def __init__(self, metr):
        self.metr = metr  # имя человека
        self.fut = 0 # возраст человека


t = Metric(int(input("Введите метры:")))
print("Количество метров:", t.metr)
t.fut = 3.28
print("Кеф умножения =", t.fut)
print("Метры в футах:", t.metr*t.fut)
