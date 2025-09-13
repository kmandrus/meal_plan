from sqlite3 import IntegrityError

import pytest

from tests.load_test_data import load_tables
from meal_plan.create_db import create_tables
from meal_plan.utils import connect


@pytest.fixture
def conn():
    """ 
    A connection to an empty, in-memory sqlite database.
    """
    db = ":memory:"
    conn = connect(db)
    create_tables(conn)
    conn.commit()
    yield conn
    conn.close()


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


def test_recipe_id_and_ingredient_id_form_primary_key_in_recipe_ingredients_table(conn):
    table_contents = {
        "recipes": [
            {"id": 1, "name": "Spaghetti", "description": None},
            {"id": 2, "name": "Carbonana", "description": None},
        ],
        "ingredients": [
            {"id": 1, "name": "sauce", "description": None},
            {"id": 2, "name": "pasta", "description": None},
            {"id": 3, "name": "onion", "description": None},
        ],
        "units": [
            {"id": 1, "name": "cup", "plural": "cups"},
        ],
        "recipe_ingredients": [
            {"recipe_id": 1, "ingredient_id": 1, "unit_id": 1, "quantity": 1}, 
            {"recipe_id": 1, "ingredient_id": 2, "unit_id": 1, "quantity": 1,}, 
            {"recipe_id": 2, "ingredient_id": 1, "unit_id": 1, "quantity": 1}, 
            {"recipe_id": 2, "ingredient_id": 2, "unit_id": 1, "quantity": 1}, 
        ],
    }
    load_tables(conn, table_contents)
    with pytest.raises(
        IntegrityError, 
        match="UNIQUE constraint failed: recipe_ingredients.recipe_id, recipe_ingredients.ingredient_id"
    ):
        conn.cursor().execute("INSERT INTO recipe_ingredients VALUES(1, 1, 1, 1)")


def test_recipe_id_in_recipe_ingredients_table_is_foreign_key_from_recipes_table(conn):
    table_contents = {
        "ingredients": [
            {"id": 1, "name": "sauce", "description": None},
        ],
        "units": [
            {"id": 1, "name": "cup", "plural": "cups"},
        ],
        "recipe_ingredients": [
            {"recipe_id": 1, "ingredient_id": 1, "unit_id": 1, "quantity": 1}, 
        ],
    }
    with pytest.raises(
        IntegrityError,
        match="FOREIGN KEY constraint failed",
    ):
        load_tables(conn, table_contents)


def test_ingredient_id_in_recipe_ingredients_table_is_foreign_key_from_ingredients_table(conn):
    table_contents = {
        "recipes": [
            {"id": 1, "name": "saucy chicken", "description": None}
        ],
        "units": [
            {"id": 1, "name": "cup", "plural": "cups"},
        ],
        "recipe_ingredients": [
            {"recipe_id": 1, "ingredient_id": 1, "unit_id": 1, "quantity": 1}, 
        ],
    }
    with pytest.raises(
        IntegrityError,
        match="FOREIGN KEY constraint failed",
    ):
        load_tables(conn, table_contents)


def test_unit_id_in_recipe_ingredients_table_is_foreign_key_from_units_table(conn):
    table_contents = {
        "recipes": [
            {"id": 1, "name": "saucy chicken", "description": None}
        ],
        "ingredients": [
            {"id": 1, "name": "sauce", "description": None},
        ],
        "recipe_ingredients": [
            {"recipe_id": 1, "ingredient_id": 1, "unit_id": 1, "quantity": 1}, 
        ],
    }
    with pytest.raises(
        IntegrityError,
        match="FOREIGN KEY constraint failed",
    ):
        load_tables(conn, table_contents)


def test_recipe_id_and_step_form_primary_key_in_recipe_instructions_table(conn):
    table_contents = {
        "recipes": [
            {"id": 1, "name": "saucy chicken", "description": None},
        ],
        "recipe_instructions": [
            {"recipe_id": 1, "step": 1, "instruction": "make the sauce"},
        ]
        
    }
    load_tables(conn, table_contents)
    with pytest.raises(IntegrityError, match="UNIQUE constraint failed: recipe_instructions.recipe_id, recipe_instructions.step"):
        conn.cursor().execute("INSERT INTO recipe_instructions VALUES(1, 1, 'chop chicken')")


def test_recipe_id_in_recipe_instructions_table_is_foreign_key_from_recipes_table(conn):
    table_contents = {
        "recipe_instructions": [
            {"recipe_id": 1, "step": 1, "instruction": "make the sauce"},
        ]
        
    }
    with pytest.raises(IntegrityError, match="FOREIGN KEY constraint failed"):
        load_tables(conn, table_contents)


def test_id_is_primary_key_in_units_table(conn):
    table_contents = {
        "units": [
            {"id": 1, "name": "cup", "plural": "cups"},
            {"id": 1, "name": "teaspoon", "plural": "teaspoons"},
        ],
    }
    with pytest.raises(IntegrityError, match="UNIQUE constraint failed: units.id"):
        load_tables(conn, table_contents)
