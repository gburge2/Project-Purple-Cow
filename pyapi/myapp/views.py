from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Item

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def items_request(request):
    """
    Method to determine what method to execute
    based off the request's method. 
    
    Request Methods :
    POST - clears curent items and set new items. 
    GET -  retrieves current items. 
    DELETE - deletes all items.  
         
    """ 
    method = request.method
    if method == 'GET': 
        return get_items(request)
    elif method == 'POST':
        return set_items(request)
    elif method == 'DELETE':
        return delete_items(request)

def set_items(request):
    """
    Method to clear and set items. 

    """
    Item.objects.all().delete()   
    return add_items(request)   

def get_items(request):
    """
    Method to get items. 

    """
    response_list = []
    try:
        for item in Item.objects.all():
            response_list.append({'id' : item.id, 'name' : item.name})
    except:
        response_list.append({'Error'})
    response = json.dumps(response_list)
    return HttpResponse(response, content_type='text/json')


def add_items(request):   
    """
    Method to add items. 

    """
    response_list = []
    payload = json.loads(request.body)
    for load in payload:
        name = load['name']
        item = Item(name=name)
        try:
            item.save()
            response_list.append({'id' : item.id, 'name' : item.name})
        except:
            response_list.append({'Failure' : name})
    response = json.dumps(response_list)
    return HttpResponse(response, content_type='text/json')

 
def delete_items(request):
    """
    Method to delete items. 

    """
    response_list = []
    try:
        Item.objects.all().delete()   
        response_list.append({ 'Success' : 'Deleted All Items'})
    except:
        response_list.append({ 'Failure' : 'Could not delete.'})
    response = json.dumps(response_list)
    return HttpResponse(response, content_type='text/json')