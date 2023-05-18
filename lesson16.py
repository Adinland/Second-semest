print("\tЗадание 1")

class cashbox():
    cash = 0
    def top_up(self, x):
        self.cash += x
    def count_1000(self):
        arg = self.cash // 1000
        hundreds = ''
        if arg % 10 == 0 or arg % 10 >= 5 or arg % 10 <= 9:
            hundreds = "тысяч"
        elif arg % 10 == 1:
            hundreds = "тысяча"
        elif arg % 10 > 1 or arg % 10 <=4:
            hundreds = "тысячи"
        print(f"В кассе {arg} {hundreds}")
    def take_away(self, x):
        if x <= self.cash:
            self.cash -= x
        else:
            print("Ошибка, в кассе недостаточно денег!")

cb = cashbox()
cb.top_up(29000)
cb.count_1000()
cb.take_away(12000)
cb.count_1000()

print("\tЗадание 2")

class turtle():
    x = 0
    y = 0
    s = 1
    def go_up(self):
        self.y += self.s
    def go_down(self):
        self.y -= self.s
    def go_left(self):
        self.x -= self.s
    def go_right(self):
        self.x += self.s
    def evolve(self):
        self.s += 1
    def degrade(self):
        if self.s <= 0:
            print("Ошибка!")
        else:
            self.s -= 1
    def count_moves(self, x, y):
        return (abs(self.x - x) / self.s) + (abs(self.y - y) / self.s)

t = turtle()
print(f"Черепашка дойдёт за {t.count_moves(3, 5)} шажочков")
t.evolve()
t.count_moves(3, 5)
print(f"Черепашка дойдёт за {t.count_moves(3, 5)} шажочков")