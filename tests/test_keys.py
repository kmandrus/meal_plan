from sqlite3 import connect, IntegrityError
from pathlib import Path

import pytest

from tests.load_test_data import load_tables
from meal_plan.create_db import create_tables


@pytest.fixture
def conn():
    """ 
    A connection to a empty sqlite database.

    Is deleted after each use of the fixture. Not thread safe.
    """
    # when I have wifi, look up how to create a temporary file with pytest
    db = "test.db"
    test_db_path = Path(db)
    test_db_path.unlink(missing_ok=True)
    conn = connect(db)
    create_tables(conn)
    conn.commit()
    yield conn
    conn.close()
    test_db_path.unlink()


def test_id_col_is_primary_key_for_recipes_table(conn):
    table_contents = {
        "recipes": [
            {"id": 1, "name": "Spaghetti", "description": None},
            {"id": 1, "name": "Duplicate Spaghetti", "description": None},
        ],
    }
    with pytest.raises(IntegrityError, match="UNIQUE constraint failed: recipes.id"):
        load_tables(conn, table_contents)


def test_id_col_is_primary_key_for_ingredients_table(conn):
    table_contents = {
        "ingredients": [
            {"id": 1, "name": "Sauce", "description": None},
            {"id": 1, "name": "Sauce with same id", "description": None},
        ]
    }
    with pytest.raises(IntegrityError, match="UNIQUE constraint failed: ingredients.id"):
        load_tables(conn, table_contents)


def test_recipe_id_and_ingredient_id_form_primary_key_in_ingredients_table():
    pass


def test_recipe_id_in_recipe_ingredients_table_is_foreign_key_from_recipes_table():
    pass


def test_ingredient_id_in_recipe_ingredients_table_is_foreign_key_from_ingredients_table():
    pass


def test_unit_id_in_recipe_ingredients_table_is_foreign_key_from_unit_table():
    pass


def test_recipe_id_and_step_form_primary_key_in_recipe_instructions_table():
    pass


def test_recipe_id_in_recipe_instructions_table_is_foreign_key_from_recipes_table():
    pass


def test_id_is_primary_key_in_units_table(conn):
    table_contents = {
        "units": [
            {"id": 1, "name": "cup", "plural": "cups"},
            {"id": 1, "name": "teaspoon", "plural": "teaspoons"},
        ],
    }
    with pytest.raises(IntegrityError, match="UNIQUE constraint failed: units.id"):
        load_tables(conn, table_contents)
