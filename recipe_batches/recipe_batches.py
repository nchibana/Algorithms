#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  if len(recipe.values()) > len(ingredients.values()):
    batches = 0
  else:
    product = [i // j for i, j in zip(ingredients.values(), recipe.values())]
    curr_index = 0
    min_index = curr_index
    for i in range(len(product)-1):
      if product[curr_index + 1] < product[min_index]:
        min_index = curr_index + 1
    batches = product[min_index]
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))