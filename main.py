# Home Work Part 2.

class Store:
    def __init__(self, name, address):
        """Конструктор, инициализирует название и адрес магазина, а также пустой словарь для товаров."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def display_items(self):
        """Отображает все товары и их цены."""
        if not self.items:
            print("Ассортимент пуст.")
        else:
            for item_name, price in self.items.items():
                print(f"{item_name}: {price}")

def display_all_stores_items(stores):
    """Отображает все товары во всех магазинах."""
    if not stores:
        print("Нет доступных магазинов.")
    else:
        for store_name, store in stores.items():
            print(f"\nМагазин: {store_name}, Адрес: {store.address}")
            store.display_items()

def main():
    stores = {}  # Словарь для хранения магазинов, где ключ - название магазина
    current_store = None

    while True:
        print("\nВыберите действие:")
        print("1. Создать новый магазин")
        print("2. Выбрать магазин")
        print("3. Добавить товар в текущий магазин")
        print("4. Удалить товар из текущего магазина")
        print("5. Узнать цену товара в текущем магазине")
        print("6. Обновить цену товара в текущем магазине")
        print("7. Показать все товары в текущем магазине")
        print("8. Показать все товары во всех магазинах")
        print("9. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            store_name = input("Введите название магазина: ")
            store_address = input("Введите адрес магазина: ")
            if store_name not in stores:
                stores[store_name] = Store(store_name, store_address)
                print(f"Магазин '{store_name}' создан.")
            else:
                print(f"Магазин с названием '{store_name}' уже существует.")

        elif choice == '2':
            store_name = input("Введите название магазина для выбора: ")
            if store_name in stores:
                current_store = stores[store_name]
                print(f"Выбран магазин '{store_name}'.")
            else:
                print(f"Магазин '{store_name}' не найден.")

        elif choice == '3':
            if current_store:
                item_name = input("Введите название товара: ")
                price = float(input("Введите цену товара: "))
                current_store.add_item(item_name, price)
            else:
                print("Сначала выберите магазин.")

        elif choice == '4':
            if current_store:
                item_name = input("Введите название товара для удаления: ")
                current_store.remove_item(item_name)
            else:
                print("Сначала выберите магазин.")

        elif choice == '5':
            if current_store:
                item_name = input("Введите название товара для поиска цены: ")
                price = current_store.get_price(item_name)
                if price is not None:
                    print(f"Цена товара '{item_name}' составляет {price}.")
                else:
                    print(f"Товар '{item_name}' отсутствует в ассортименте.")
            else:
                print("Сначала выберите магазин.")

        elif choice == '6':
            if current_store:
                item_name = input("Введите название товара для обновленияцены: ")
                new_price = float(input("Введите новую цену товара: "))
                current_store.update_price(item_name, new_price)
            else:
                print("Сначала выберите магазин.")

        elif choice == '7':
            if current_store:
                print(f"Товары в магазине '{current_store.name}':")
                current_store.display_items()
            else:
                print("Сначала выберите магазин.")

        elif choice == '8':
            display_all_stores_items(stores)

        elif choice == '9':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Запуск программы
main()