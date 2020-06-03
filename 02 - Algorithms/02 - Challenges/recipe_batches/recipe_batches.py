#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = float('inf')
  for key,value in recipe.items():
    if key not in ingredients:
      return 0
    if max_batches > ingredients[key] // value:
      max_batches = ingredients[key] // value

  return max_batches





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 200, 'butter': 99, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))