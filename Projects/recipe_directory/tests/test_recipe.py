from lib.recipe import *

def test_construct_of_recipe():
    recipe = Recipe(1, 'Curry Chicken', 30, 4)
    assert recipe.id == 1
    assert recipe.recipe_name == 'Curry Chicken'
    assert recipe.average_cooking_time == 30
    assert recipe.rating == 4

def test_recipe_eqaual_to_each_other():
    recipe1 = Recipe(1, 'Curry Chicken', 30, 4)
    recipe2 = Recipe(1, 'Curry Chicken', 30, 4)
    assert recipe1 == recipe2

def test_recipe_format():
    recipe = Recipe(1, 'Curry Chicken', 30, 4)
    assert str(recipe) == "Recipe(1, Curry Chicken, 30, 4)"