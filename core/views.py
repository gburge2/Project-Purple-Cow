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
    based off the request's method. POST request's
    must be an array of JSON objects or just a single
    JSON object. 
    
    Request Methods :
    POST - clears curent items and set new items. 
    GET -  retrieves current items. 
    DELETE - deletes all items.  
         
    """ 
    method = request.method
    if method == 'GET': 
        return get_items()
    elif method == 'POST':
        return set_items(request)
    elif method == 'DELETE':
        return delete_items()

@csrf_exempt  
def id_request(request, id):
    """
    Method to determine what method to execute
    based off the request's method. 
    
    Request Methods :
    PUT - updates name of item by id
    GET -  retrieves item by id 
    DELETE - deletes item by id  
         
    """ 
    method = request.method
    if method == 'GET': 
        return get_id(id)
    elif method == 'PUT':
        return update_name_by_id(id, request)
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
            
def update_name_by_id(id, request):
    """
    Method to update single item by id . The request must be 
    a single JSON object. 

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
        Item.objects.get(id = id).delete()
        response = json.dumps([{'Success' : 'Deleted Item with id '+str(id)}])
    except:
        response = json.dumps([{'Error' : 'No item with that id.'}])
    return HttpResponse(response, content_type='text/json')

def set_items(request):
    """
    Method to clear and set items. 

    """
    Item.objects.all().delete()   
    return add_items(request)   

def get_items():
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
    Method to add item(s). Request can either be a JSON object or an
    array of JSON objects. 

    """
    response_list = []
    payload = json.loads(request.body)
    if not isinstance(payload, list):
        name = payload['name']
        id = payload['id']
        item = Item(name=name , id=id)
        item.save()
        response_list.append({'id' : item.id, 'name' : name})  
        response = json.dumps(response_list)
    else:
        for load in payload:       
            try:
                name = load['name']
                id = load['id']
                item = Item(name=name , id=id)
                item.save()
                response_list.append({'id' : item.id, 'name' : item.name})
            except:
                response_list.append({'Error' : str(type(payload))})
        response = json.dumps(response_list)
    return HttpResponse(response, content_type='text/json')

 
def delete_items():
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