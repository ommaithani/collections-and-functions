# Inside a package folder called 'foodorder', create two modules: menu.py (with a function get_menu() returning a list of food items) and order.py (with a function place_order(item) that prints 'Order placed for: item'). Use __init__.py to import both functions so they can be accessed directly from the package.<br><br><em><strong>Hint:</strong> Use 'from .menu import get_menu' and 'from .order import place_order' in __init__.py.</em>

from .menu import get_menu
from .order import place_order