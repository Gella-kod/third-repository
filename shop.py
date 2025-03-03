class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в каталог."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин '{self.name}'.")

    def remove_item(self, item_name):
        """Удаляет товар из каталога."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в магазине '{self.name}'.")

    def get_item_price(self, item_name):
        """Выводит цену товара по его названию."""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена в магазине '{self.name}'.")
        else:
            print(f"Товара'{item_name}' нет в магазине '{self.name}'.")

    def __str__(self):
        """Возвращает итоговое представление магазина."""
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

store1 = Store("Продукты у дяди Коли", "пл. Чкалова 8а")
store2 = Store("Булошная тетя Глаша", "пр. Мира, 25")
store3 = Store("Автоцентр Михалыч", "ул. Садовая, 5")

store1.add_item("хлеб", 40)
store1.add_item("газировка", 50)
store1.add_item("майонез", 120)

store2.add_item("эклеры", 25)
store2.add_item("синабоны", 99)
store2.add_item("ватрухи", 50)

store3.add_item("диски", 100500)
store3.add_item("покрышки", 9000)
store3.add_item("масло моторное", 2500)

print(store1)
print(store2)
print(store3)

store1.remove_item("майонез")
print(store1.get_item_price("хлеб"))
store1.update_item_price("газировка", 66)

print(store1)