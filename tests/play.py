import sqlite3

"""
A script for playing with results in the repl.
"""

DISPLAY_RECIPE_INGREDIENTS_SQL = """
SELECT
    recipes.name AS recipe_name,
    ingredients.name AS ingredient_name,
    recipe_ingredients.quantity AS quantity,
    units.name AS unit_name
FROM recipe_ingredients
    JOIN recipes ON recipe_ingredients.recipe_id = recipes.id 
    JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.id
    JOIN units ON units.id = recipe_ingredients.unit_id
"""


TEST_SQL = """
SELECT
    *
FROM recipe_ingredients
    JOIN recipes ON recipe_ingredients.recipe_id = recipes.id 
"""


def get_cursor(db: str):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn.cursor()


def print_query(results):
    for row in results:
        print(dict(row))


cur = get_cursor('test.db')
res = cur.execute(DISPLAY_RECIPE_INGREDIENTS_SQL).fetchall() 
recipes = cur.execute("select * from recipes").fetchall()
ingredients = cur.execute("select * from ingredients").fetchall()
units = cur.execute("select * from units").fetchall()
recipe_ingredients = cur.execute("select * from recipe_ingredients").fetchall()
recipe_instructions = cur.execute("select * from recipe_instructions").fetchall()
