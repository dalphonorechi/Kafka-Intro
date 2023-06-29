import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        valid_pizza_names = [
            'Margherita',
            'Marinara',
            'Diavola',
            'Mari & Monti',
            'Salami',
            'Peperoni'
        ]
        
        return valid_pizza_names[random.randint(0, len(valid_pizza_names)-1)]
    
    def pizza_toppings(self):
        available_pizza_toppings = [
            'tomato',
            'mozarella',
            'blue cheese',
            'green peppers',
            'ham',
            'olives',
            'garlic',
            'tuna',
            'onion',
            'banana'
        ]
        
        return available_pizza_toppings[random.randint(0, len(available_pizza_toppings)-1)]
        
    def pizza_shop(self):
        pizza_shops = [
            'Mario Pizza',
            'Luigis Pizza',
            'Circular Pi Pizzeria',
            'Mammamia Pizza',
        ]
        
        return pizza_shops[random.randint(0, len(pizza_shops)-1)]