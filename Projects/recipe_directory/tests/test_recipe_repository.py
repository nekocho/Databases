from lib.recipe import *
from lib.recipe_repository import *

def test_recipe_get_all(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)

    recipe = repository.all()

    assert recipe == [
        Recipe(1, 'Curry Chicken', 30, 4),
        Recipe(2, 'Tonkotsu Ramen', 15, 5),
        Recipe(3, 'Sushi', 20, 5),
        Recipe(4, 'Instant Noodles', 5, 2)
    ]

def test_recipe_find_recipe(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)

    recipe = repository.find(1)

    assert recipe == Recipe(1, 'Curry Chicken', 30, 4)