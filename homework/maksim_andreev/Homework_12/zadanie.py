class Flowers:
    def __init__(self, name, color, old, price, lifespan):
        self.name = name
        self.color = color
        self.old = old
        self.price = price
        self.lifespan = lifespan


class Rose(Flowers):
    def __init__(self, color, old, price, lifespan):
        super().__init__("Роза", color, old, price, lifespan)

    def __str__(self):
        return f'Цветок: {self.name},Свежесть: {self.old}, Цена: {self.price}, Время жизни: {self.lifespan}'


class Chamomile(Flowers):
    def __init__(self, color, old, price, lifespan):
        super().__init__("Ромашка", color, old, price, lifespan)

    def __str__(self):
        return f'Цветок: {self.name},Свежесть: {self.old}, Цена: {self.price}, Время жизни: {self.lifespan}'


class Bouquet:
    def __init__(self):
        self.flow_set = []

    def add_flower(self, flower):
        self.flow_set.append(flower)

    def calc_price_all(self):
        price_all = 0
        for flower in self.flow_set:
            price_all += flower.price
        return price_all

    def calc_average_lifetime(self):
        total_lifetime = 0
        for flower in self.flow_set:
            total_lifetime += flower.lifespan
        return total_lifetime / len(self.flow_set)

    def sort_by_old(self):
        self.flow_set.sort(key=lambda x: x.old)

    def sort_by_color(self):
        self.flow_set.sort(key=lambda x: x.color, reverse=True)

    def sort_by_price(self):
        self.flow_set.sort(key=lambda x: x.price)

    def find_more_or_equal_avg(self, lifetime):
        result = []
        for flower in self.flow_set:
            if flower.lifespan >= lifetime:
                result.append(flower)
        return result


rose1 = Rose("red", 3, 60, 7)
rose2 = Rose("pink", 2, 50, 12)
chamomile1 = Chamomile("white", 4, 20, 8)
chamomile2 = Chamomile("yellow", 1, 15, 11)


bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(chamomile1)
bouquet.add_flower(chamomile2)
print("All price: ", bouquet.calc_price_all())
print("Total lifetime: ", bouquet.calc_average_lifetime())
print(', '.join(str(flower) for flower in bouquet.find_more_or_equal_avg(11)))
bouquet.sort_by_price()
print("Отсортированные по цене:")
for flower in bouquet.flow_set:
    print(flower)
