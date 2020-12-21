from pytest import fixture

from core.allergens import find_ingredients_without_allergens, find_dangerous_ingredients


@fixture
def ingredient_list():
    a = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split("\n")
    yield a


def test_part_one(ingredient_list):
    assert len(find_ingredients_without_allergens(ingredient_list)) == 5


def test_part_two(ingredient_list):
    todo = find_dangerous_ingredients(ingredient_list)
    assert ','.join(todo) == "mxmxvkd,sqjhc,fvjkl"
