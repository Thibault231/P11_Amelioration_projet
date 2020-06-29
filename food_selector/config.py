# coding: utf-8
"""Define global variables
for food_selector APP program.
"""


CATEGORIES_LIST = [
    [
        'acras', 'endives-au-jambon', 'cassoulets',
        'pains-aux-raisins', 'brioches-tranchees',
        'croissants-fourres', 'yaourts-natures',
        'laits-concentres', 'milkfat', 'biscuits',
        'sauces-tomates-au-basilic', 'aiolis', 'guacamoles',
        'pizzas-au-chorizo', 'pizzas-chevre-lardons',
        'chocolats-noirs-sales', 'jus-d-orange'
        ],
    [
        'Plats préparés', 'Viennoiseries', 'Produits laitiers',
        'Sauces', 'Pizzas', 'Snacks sucrés'
        ]
    ]

TESTS = {
    "name1": "impossible",
    "name2": "hellfest",
    "RightStatus": 200,
    "UnfoundStatus": 404,
    "WrongStatus": 302,
    "UrlApp": "https://djangonutella.herokuapp.com/",
    "UrlResult": "https://djangonutella.herokuapp.com/food_selector/result/",
    "UrlHistory": "https://djangonutella.herokuapp.com/food_selector/history/",
    "UrlAccount": "https://djangonutella.herokuapp.com/accounts/myaccount/",
    "UrlCreation":
    "https://djangonutella.herokuapp.com/accounts/account_creation/",
    "UrlConnexion":
    "https://djangonutella.herokuapp.com/accounts/connexion/",
    "UrlItem": "https://djangonutella.herokuapp.com/food_selector/item/21/",
    "UrlSave": "https://djangonutella.herokuapp.com/food_selector/save/21/",
    "UrlDeconnexion":
    "https://djangonutella.herokuapp.com/accounts/deconnexion/"
}
