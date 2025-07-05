import sqlite3
import argparse

CREATE_RECIPES_TABLE_SQL = """
    CREATE TABLE recipes(
        id INTEGER NOT NULL PRIMARY KEY, 
        name TEXT NOT NULL,
        description TEXT
    )
"""
CREATE_INGREDIENTS_TABLE_SQL = """
    CREATE TABLE ingredients( 
        id INTEGER NOT NULL PRIMARY KEY, 
        name TEXT NOT NULL,
        description TEXT
    )
"""
CREATE_RECIPE_INGREDIENTS_TABLE_SQL = """
    CREATE TABLE recipe_ingredients(
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
    CREATE TABLE recipe_instructions(
        recipe_id INTEGER NOT NULL,
        step INTEGER NOT NULL,
        instruction TEXT NOT NULL,
        PRIMARY KEY (recipe_id, step),
        FOREIGN KEY (recipe_id) REFERENCES recipes (id)
    )
"""

def create_db(name: str):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    for sql in [
        CREATE_RECIPES_TABLE_SQL,
        CREATE_INGREDIENTS_TABLE_SQL,
        CREATE_RECIPE_INGREDIENTS_TABLE_SQL,
        CREATE_RECIPE_INSTRUCTIONS_TABLE_SQL
    ]:
        cur.execute(sql)
        conn.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="CreateEmptyDb",
        description="Create a SQLite database for meal planning."
    )
    parser.add_argument(
        "db_name",
        type=str,
        help="The name of the database to create."
    )
    args = parser.parse_args()
    create_db(args.db_name)

