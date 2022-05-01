from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Item

def home(request):
    return render(request, 'index.html')

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

@csrf_exempt  
def id_request(request, id):
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
        return get_id(id)
    elif method == 'PUT':
        return update_id(id, request)
    elif method == 'DELETE':
        return delete_id(id)

def get_id(id):
    """
    Method to retrieve single item by id 

    """
    try:
        item = Item.objects.get(id = id)
        repsonse = json.dumps([{'id' : item.id, 'name' : item.name}])
    except:
        repsonse = json.dumps([{'Error' : 'No item with that id.'}])
    return HttpResponse(repsonse, content_type='text/json')
            
def update_id(id, request):
    """
    Method to update single item by id 

    """
    try:
        payload = json.loads(request.body)
        name = payload['name']
        Item.objects.filter(id=id).update(name = name)
        response = json.dumps([{'id' : id, 'name' : name}])
    except:
        response = json.dumps([{'Error' : 'No item with that id.'}])
    return HttpResponse(response, content_type='text/json')

def delete_id(id):
    """
    Method to delete single item by id 

    """
    try:
        Item.objects.filter(id=id).delete()
        response = json.dumps([{'Success' : 'Deleted Item.'}])
    except:
        response = json.dumps([{'Error' : 'No item with that id.'}])
    return HttpResponse(response, content_type='text/json')

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