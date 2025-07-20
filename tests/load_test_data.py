from typing import Iterable
from meal_plan.utils import connect

from meal_plan.create_db import create_tables


def _to_insert_sql(table: str, columns: Iterable[str]) -> str:
    formatted_columns =  [f":{key}" for key in columns]
    return f"INSERT INTO {table} VALUES({', '.join(formatted_columns)})"


TABLE_CONTENTS = {
    "recipes": [
        {"id": 1, "name": "Spaghetti with Meat Sauce", "description": "A very simple Spaghetti Recipe."},
        {"id": 2, "name": "Beef Stew", "description": None},
    ],
    "ingredients": [
        {"id": 1, "name": "Pasta Sauce", "description": "Any pre-packaged pasta sauce."},
        {"id": 2, "name": "Spaghetti Noodles", "description": None},
        {"id": 3, "name": "Yellow Onion", "description": None},
        {"id": 4, "name": "Red Onion", "description": None},
        {"id": 5, "name": "Garlic", "description": None},
        {"id": 6, "name": "Olive Oil", "description": None},
        {"id": 7, "name": "Salt", "description": None},
        {"id": 8, "name": "Pepper", "description": None},
        {"id": 9, "name": "Parmesan Cheese", "description": None},
        {"id": 10, "name": "Basil", "description": None},
        {"id": 11, "name": "Oregano", "description": None},
        {"id": 12, "name": "Red Pepper Flakes", "description": None},
        {"id": 13, "name": "Ground Beef", "description": None},
        {"id": 14, "name": "Spicy Italian Sausage", "description": None},
        {"id": 15, "name": "Portabello Mushrooms", "description": None},
        {"id": 16, "name": "Carrots", "description": None},
        {"id": 17, "name": "Celery", "description": None},
        {"id": 18, "name": "Beef Broth", "description": None},
        {"id": 19, "name": "Red Wine", "description": None},
        {"id": 20, "name": "Bay Leaves", "description": None},
        {"id": 21, "name": "Stew Meat", "description": None},
    ],
    "units": [
        {"id": 1, "name": "box", "plural": "boxes"},
        {"id": 2, "name": "jar", "plural": "jars"},
        {"id": 3, "name": "clove", "plural": "cloves"},
        {"id": 4, "name": "to taste", "plural": "to taste"},
        {"id": 5, "name": "pinch", "plural": "pinch"},
        {"id": 6, "name": "leaf", "plural": "leaves"},
        {"id": 7, "name": "pound", "plural": "pounds"},
        {"id": 8, "name": "lb", "plural": "lbs"},
        {"id": 9, "name": "cup", "plural": "cups"},
        {"id": 10, "name": "whole", "plural": "whole"},
        {"id": 11, "name": "glug", "plural": "glugs"},
    ],
    "recipe_ingredients": [
        {"recipe_id": 1, "ingredient_id": 1, "unit_id": 2, "quantity": 2}, 
        {"recipe_id": 1, "ingredient_id": 2, "unit_id": 1, "quantity": 2,}, 
        {"recipe_id": 1, "ingredient_id": 3, "unit_id": 10, "quantity": 1}, 
        {"recipe_id": 1, "ingredient_id": 6, "unit_id": 11, "quantity": 2}, 
        {"recipe_id": 1, "ingredient_id": 9, "unit_id": 4, "quantity": 1}, 
        {"recipe_id": 1, "ingredient_id": 12, "unit_id": 4, "quantity": 1}, 
        {"recipe_id": 1, "ingredient_id": 13, "unit_id": 7, "quantity": 1}, 
        {"recipe_id": 1, "ingredient_id": 14, "unit_id": 7, "quantity": 1}, 
        {"recipe_id": 2, "ingredient_id": 3, "unit_id": 9, "quantity": 1},
        {"recipe_id": 2, "ingredient_id": 16, "unit_id": 9, "quantity": 0.5 },
        {"recipe_id": 2, "ingredient_id": 17, "unit_id": 9, "quantity": 0.5},
        {"recipe_id": 2, "ingredient_id": 18, "unit_id": 9, "quantity": 2},
        {"recipe_id": 2, "ingredient_id": 19, "unit_id": 9, "quantity": 0.33},
        {"recipe_id": 2, "ingredient_id": 20, "unit_id": 6, "quantity": 2},
        {"recipe_id": 2, "ingredient_id": 21, "unit_id": 7,"quantity": 2},
        {"recipe_id": 2, "ingredient_id": 6, "unit_id": 11, "quantity": 1},
    ],
    "recipe_instructions": [
        {"recipe_id": 1, "step": 1, "instruction": "Set water to boil in a large pot for the noodles."},
        {"recipe_id": 1, "step": 2, "instruction": "Dice onions and garlic. Remove sausage casings."},
        {"recipe_id": 1, "step": 3, "instruction": "Mix together ground meat and sausage, then brown in a large skillet. Season with salt and pepper to taste. Set aside."},
        {"recipe_id": 1, "step": 4, "instruction": "Reusing some of the oil from the meat, add olive oil to skillet and sautee onion and garlic. Season with salt to taste."},
        {"recipe_id": 1, "step": 5, "instruction": "Return the browned meat to the pan, then add sauce, bay leaves, and red pepper flakes. Cook until flavors come together, about 30 minutes."},
    ],
}


def load_tables(conn, table_contents):
    cursor = conn.cursor()
    for table, rows in table_contents.items(): 
        cursor.executemany(_to_insert_sql(table, rows[0].keys()), rows)
        conn.commit()


def main(db: str):
    conn = connect(db)
    create_tables(db)
    load_tables(conn, TABLE_CONTENTS)


if __name__ == "__main__":
    main('test.db')

