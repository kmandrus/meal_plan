# Meal-Planning Application

Stores recipes, generates meal plans, creates shopping lists, and displays cooking instructions.

## Database Schema

Primary Keys: `recipe_id`, `ingredient_id`
Fact Tables: `recipes`, `ingredients`
Dimension Tables: `recipe_instructions`, `recipe_ingredients`

Parenthetical items are potential, unimplemented, additions. 

### Tables
- recipes
    - id
    - name
    - description

- ingredients
    - id
    - name
    - description
    - (store_location)
    - (package_quantity)
    - (package_unit) 

- recipe_instructions
    - recipe_id
    - step
    - instruction

- recipe_ingredients
    - recipe_id
    - ingredient_id
    - quantity
    - unit

