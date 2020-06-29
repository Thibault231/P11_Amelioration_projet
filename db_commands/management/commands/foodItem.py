# coding: utf-8
"""Create class FoodItem for init_db command.
"""


class FoodItemOFF():
    """
    Class 'food_item.FoodItem'
    Attributs:
    id (int), name(str), cat(str), cat_id(int), market(str),
    descriptions(str), nutriscore(str), url_id(int)
    All attributs are default str('none')
    Example:
    food_item = Food()
    """
    def __init__(self):
        self.name = str()
        self.brand = str()
        self.category = list()
        self.store = str()
        self.description = str()
        self.allergens = str()
        self.nutriscore = str()
        self.url_id = str()
        self.picture = str()
