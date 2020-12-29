def read_input(input_path="input.txt"):
    f = open(input_path)
    input_lines = f.read().split('\n')
    f.close()
    return input_lines


def find_allergen(ingredients_list):
    allergen_to_ingredient = {}
    ingredient_count = {}
    for ingredient_allergen in ingredients_list:
        ingredients, allergens = ingredient_allergen.rstrip(")").split(" (contains ")
        ingredients = ingredients.split()
        allergens = allergens.split(", ")
        update_ingredient_count(ingredient_count, ingredients)
        for allergen in allergens:
            if allergen in allergen_to_ingredient:
                allergen_to_ingredient[allergen] = [i for i in ingredients if i in allergen_to_ingredient[allergen]]
            else:
                allergen_to_ingredient[allergen] = [i for i in ingredients]
    dangerous_ingredients = set(
        [ingredient for ingredients in allergen_to_ingredient.values() for ingredient in ingredients])
    non_dangerous_ingredients = set(list(ingredient_count.keys())).difference(dangerous_ingredients)
    safe_ingredient_count = get_safe_ingredient_count(ingredient_count, non_dangerous_ingredients)
    return safe_ingredient_count, dangerous_ingredients


def get_safe_ingredient_count(ingredient_count, non_dangerous_ingredients):
    dangerous_ingredient_count = 0
    for ingredient in non_dangerous_ingredients:
        dangerous_ingredient_count = dangerous_ingredient_count + ingredient_count[ingredient]
    return dangerous_ingredient_count


def update_ingredient_count(ingredient_count, ingredients):
    for ingredient in ingredients:
        if ingredient in ingredient_count:
            ingredient_count[ingredient] = ingredient_count[ingredient] + 1
        else:
            ingredient_count[ingredient] = 1


if __name__ == '__main__':
    input_data = read_input("input.txt")
    count, dangerous = find_allergen(input_data)
    print(count)
    print(dangerous)
