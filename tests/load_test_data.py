import sqlite3

def _to_optional(val):
    return "NULL" if val is None else f"'{val}'"

CREATE_RECIPES_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS recipes(
        id INTEGER NOT NULL PRIMARY KEY, 
        name TEXT NOT NULL,
        description TEXT
    )
"""
CREATE_INGREDIENTS_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS ingredients( 
        id INTEGER NOT NULL PRIMARY KEY, 
        name TEXT NOT NULL,
        description TEXT
    )
"""
CREATE_RECIPE_INGREDIENTS_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS recipe_ingredients(
        recipe_id INTEGER NOT NULL,
        ingredient_id INTEGER NOT NULL,
        quantity NUMERIC,
        unit TEXT,
        PRIMARY KEY (recipe_id, ingredient_id),
        FOREIGN KEY (recipe_id) REFERENCES recipes (id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients (id)
    )
"""
CREATE_RECIPE_INSTRUCTIONS_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS recipe_instructions(
        recipe_id INTEGER NOT NULL,
        step INTEGER NOT NULL,
        instruction TEXT NOT NULL,
        PRIMARY KEY (recipe_id, step),
        FOREIGN KEY (recipe_id) REFERENCES recipes (id)
    )
"""

RECIPES = [
    {"name": "Spaghetti", "description": "A very simple Spaghetti Recipe."},
    {"name": "Beef Stew", "description": "A simple beef stew recipe."},
]
INGREDIENTS = [
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
]
RECIPE_INGREDIENTS = [
]
RECIPE_INSTRUCTIONs = [
]

def main(db: str):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    for sql in [
        CREATE_RECIPES_TABLE_SQL,
        CREATE_INGREDIENTS_TABLE_SQL,
        CREATE_RECIPE_INGREDIENTS_TABLE_SQL,
        CREATE_RECIPE_INSTRUCTIONS_TABLE_SQL
    ]:
        cur.execute(sql)
    for recipe in RECIPES:
        add_recipe_sql = f"""
            INSERT INTO recipes VALUES 
                ({_to_optional(recipe.get("id"))}, '{recipe['name']}', '{recipe['description']}')
        """
        cur.execute(add_recipe_sql)
    for ingredient in INGREDIENTS:
        add_ingredient_sql = f"""
            INSERT INTO ingredients VALUES 
                (
                    {_to_optional(ingredient.get("id"))}, 
                    '{ingredient['name']}', 
                    {_to_optional(ingredient.get('description'))}
                )
        """
        cur.execute(add_ingredient_sql)
        conn.commit()


if __name__ == "__main__":
    main('test.db')

