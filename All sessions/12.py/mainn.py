from foodorder import get_menu, place_order

menu = get_menu()
print("Menu:", menu)

place_order(menu[0])