# coding: utf-8
"""Create command init_db for local and
distant implementation of postgres DB
from datas extracted from Open Food Fact.
"""
import requests
from django.core.management.base import BaseCommand
from food_selector.config import CATEGORIES_LIST
from food_selector.models import Category, FoodItem
from .foodItem import FoodItemOFF


def api_extraction_by_category(category, super_cat_list):
    """
    Return a list of class food.Food objects implemented with cat_id and
    an API from OpenfoodFacts. Datas are taken from the page "categorie".
    Args:
    category: list (list of food categories)
    Return:
    food_list: list (list of "food.Food")
    Example:
        self._api_extraction(categorie, cat_id)
    """
    response = requests.get(
        ('https://fr.openfoodfacts.org/categorie/{}.json').
        format(category))
    file = response.json()
    food_list = []
    food_items_list = []
    for element in file['products']:
        if ('ingredients_text_fr' in element)\
                and len(element['ingredients_text_fr']) > 5:
            if element['product_name'].lower() not in food_items_list:
                if ('nutriscore_grade' in element) and (
                 'ingredients_text_debug' in element):
                    if ('stores' in element) and (
                     'image_front_url' in element):
                        if (element[
                         'ingredients_text_debug']) is not None:
                            food_item = FoodItemOFF()
                            food_items_list.append(
                             element['product_name'].lower())

                            food_item.url_id = (element['_id'])
                            food_item.brand = (element['brands']).lower()
                            food_item.name = (element['product_name']).lower()
                            food_item.nutriscore = (
                                element['nutriscore_grade'].upper())
                            food_item.description = (
                                element['ingredients_text_debug'])
                            food_item.allergens = (
                             element['allergens_from_ingredients'])
                            food_item.store = (element['stores']).lower()
                            food_item.picture = (element['image_front_url'])

                            food_item.category = [category]
                            for cat_item in super_cat_list:
                                if cat_item in element[
                                 'categories'].split(', '):
                                    food_item.category.append(cat_item)

                            food_list.append(food_item)
    return food_list


def food_item_creation(food_item):
    new_food_item = FoodItem.objects.create(
        name=food_item.name,
        brand=food_item.brand,
        description=food_item.description,
        allergens=food_item.allergens,
        nutriscore=food_item.nutriscore,
        store=food_item.store,
        picture=food_item.picture,
        url_OpenFF=food_item.url_id,
        )
    return new_food_item


def Db_update(
 sup_cat_list=CATEGORIES_LIST[0],
 cat_list=CATEGORIES_LIST[1]):
    for category in sup_cat_list:
        food_items_list = api_extraction_by_category(category, cat_list)
        print(
         'Food items for category ',
         category,
         ': load from OpenFoodFact.')
        print(len(food_items_list))

        for food_item in food_items_list:
            try:
                fooditem_to_update = FoodItem.objects.get(
                    name=food_item.name)
                fooditem_to_update.name = food_item.name
                fooditem_to_update.brand = food_item.brand
                fooditem_to_update.description = food_item.description
                fooditem_to_update.allergens = food_item.allergens
                fooditem_to_update.nutriscore = food_item.nutriscore
                fooditem_to_update.store = food_item.store
                fooditem_to_update.picture = food_item.picture
                fooditem_to_update.url_OpenFF = food_item.url_id
                print('    Food item', food_item.name, ' updated.')

            except Exception:
                new_food_item = food_item_creation(food_item)
                print('    Create new FI:', new_food_item.name, ' ,ok')
                for cat_to_link in food_item.category:
                    new_food_item.linked_cat.add(
                     Category.objects.get(name=cat_to_link))
                    print('   New FI Linked to categories: ok')

            print('Update done for category: ', category)
    print('UPDATE: done')


class Command(BaseCommand):

    def handle(self, *args, **options):
        Db_update()
