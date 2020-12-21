import re
from collections import defaultdict
from typing import List, Set, Dict

LINE_RE = re.compile(r'(.*) \(contains (.*)\)')


def find_ingredients_without_allergens(lines: List[str]) -> List[str]:
    ingredients: Set = set()
    ingredient_counter: Dict[str,int] = defaultdict(int)
    allergen_to_ingredients: Dict[str, Set[str]] = {}
    for line in lines:
        m = LINE_RE.match(line)
        local_ingredients = set()
        for ingredient in m.group(1).split(" "):
            local_ingredients.add(ingredient)
            ingredient_counter[ingredient] += 1
            ingredients.add(ingredient)
        for allergen in m.group(2).split(", "):
            if allergen in allergen_to_ingredients:
                allergen_to_ingredients[allergen] = allergen_to_ingredients[allergen].intersection(local_ingredients)
            else:
                allergen_to_ingredients[allergen] = local_ingredients
    for allergen in allergen_to_ingredients.keys():
        for ingredient in allergen_to_ingredients[allergen]:
            if ingredient in ingredients:
                ingredients.remove(ingredient)
    ret = []
    for ingredient in ingredients:
        for _ in range(ingredient_counter[ingredient]):
            ret.append(ingredient)
    return ret


def reduced(ati: Dict[str, Set[str]]) -> bool:
    for i in ati.keys():
        if len(ati[i]) > 1:
            return False
    return True


def allergens_with_one_ingredient(ati: Dict[str, Set[str]]) -> List[str]:
    ret = []
    for i in ati.keys():
        if len(ati[i]) == 1:
            ret.append(i)
    return ret


def allergens_with_more_ingredients(ati: Dict[str, Set[str]]) -> List[str]:
    ret = []
    for i in ati.keys():
        if len(ati[i]) > 1:
            ret.append(i)
    return ret


def find_dangerous_ingredients(lines: List[str]) -> List[str]:
    ingredients: Set = set()
    ingredient_counter: Dict[str,int] = defaultdict(int)
    allergen_to_ingredients: Dict[str, Set[str]] = {}
    for line in lines:
        m = LINE_RE.match(line)
        local_ingredients = set()
        for ingredient in m.group(1).split(" "):
            local_ingredients.add(ingredient)
            ingredient_counter[ingredient] += 1
            ingredients.add(ingredient)
        for allergen in m.group(2).split(", "):
            if allergen in allergen_to_ingredients:
                allergen_to_ingredients[allergen] = allergen_to_ingredients[allergen].intersection(local_ingredients)
            else:
                allergen_to_ingredients[allergen] = local_ingredients

    while not reduced(allergen_to_ingredients):
        for allergen in allergens_with_one_ingredient(allergen_to_ingredients):
            ingredient = list(allergen_to_ingredients[allergen])[0]
            for remove_from in allergens_with_more_ingredients(allergen_to_ingredients):
                if ingredient in allergen_to_ingredients[remove_from]:
                    allergen_to_ingredients[remove_from].remove(ingredient)

    ret = []
    for allergen in sorted(allergen_to_ingredients.keys()):
        ret.append(list(allergen_to_ingredients[allergen])[0])
    return ret
