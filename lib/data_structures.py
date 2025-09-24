spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass

def get_spiciest_foods(spicy_foods):
    pass

def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass

def get_names(foods):
    return [food["name"] for food in foods]

def get_spiciest_foods(foods):
    return [food for food in foods if food["heat_level"] > 5]

def print_spicy_foods(foods):
    for food in foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}")

def get_spicy_food_by_cuisine(foods, cuisine):
    for food in foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(foods):
    for food in get_spiciest_foods(foods):
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}")

def get_average_heat_level(foods):
    return sum(f["heat_level"] for f in foods) // len(foods)

def create_spicy_food(foods, new_food):
    foods.append(new_food)
    return foods
