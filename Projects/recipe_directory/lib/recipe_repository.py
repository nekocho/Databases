from lib.recipe import *

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM recipe")
        recipe = []
        for row in rows:
            item = Recipe(row['id'], row['recipe_name'], row['average_cooking_time'], row['rating'])
            recipe.append(item)
        return recipe

    def find(self, id):
        rows = self._connection.execute("SELECT * FROM recipe WHERE id = %s", [id])
        return Recipe(rows[0]['id'], rows[0]['recipe_name'], rows[0]['average_cooking_time'], rows[0]['rating'])