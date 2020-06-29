# coding: utf-8
"""Run the views for save_favorite APP.
Views:
-save:@login_required
-history:@login_required
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db import transaction
from food_selector.models import FoodItem, Account

@login_required
def save(request, item_id):
    """Rule the saving of a substitute
    on an account.
    @login_required
    Arguments:
    -request {GET}
    Returns:
    -template -- save.html
    """
    food_item = get_object_or_404(FoodItem, id=item_id)
    account = Account.objects.get(user=request.user)
    old_history = account.history.all()
    if food_item not in old_history:
        account.history.add(food_item)
        message = "Le produit a bien été ajouté à vos favoris"
    else:
        message = "Le produit est déjà dans vos favoris"
    context = {
        'message': message
    }
    return render(request, 'save_favorite/save.html', context)

@login_required
def history(request):
    """Display the substitutes
    saved in an account.
    @login_required
    Arguments:
    -request {GET}
    Returns:
    -template -- history.html
    """
    account = Account.objects.get(user=request.user)
    substitute_list = account.history.all()

    context = {
        'substitute_list': substitute_list,
    }
    return render(request, 'save_favorite/history.html', context)
