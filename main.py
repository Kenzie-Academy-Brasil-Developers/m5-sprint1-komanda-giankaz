from utils import adding_item_to_menu as write_json, menu_reading as read_json
from management import total_calculator as calculate_tab
import ujson as json

with open('menu.json', 'r') as test:
    data = json.load(test)
    print(data)

if __name__ == "__main__":
    print('Reading: ')
    print(read_json())
    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    print('Writing: ')
    print(write_json(new_item))

    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]

    table_2 = [
        {"id": 10, "amount": 3},
        {"id": 20, "amount": 2},
        {"id": 21, "amount": 5},
        ]
    print('Total Bill 1:')
    print(calculate_tab(table_1))
    print('Total Bill 2:')
    print(calculate_tab(table_2))