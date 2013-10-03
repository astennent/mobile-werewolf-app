from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #for POST requests from mobile devices that couldn't have gotten a csrf token.
from django.contrib.auth.models import User
from models import *

import json
import base64
from django.contrib.auth import authenticate, login

@csrf_exempt # allows POST requests without a csrf token
def ping(request):
    if not validate_mobile(request):
        return respond('Error: Invalid Login Credentials')
    return respond("success")


# Called whenever a mobile request is sent which requires authentication
def validate_mobile(request):
  try:
      username, password = base64.b64decode(request.POST['HTTP_AUTHORIZATION']).split(":")
  except:
      return None
  return authenticate(username=username, password=password)


# Helper method for returning json responses
def respond(response_data):
    if isinstance(response_data, str):
        data = {"message":response_data}
    else:
        data = response_data
    json_dump = json.dumps(data)
    return HttpResponse(json_dump, content_type="application/json")


@csrf_exempt
def create_account(request):
    username, password = base64.b64decode(request.POST['HTTP_AUTHORIZATION']).split(":")
    if len(User.objects.filter(username=username)) > 0:
        return respond("Username already taken")
    new_user = User.objects.create_user(username, '', password)
    new_account = Account(user=new_user)
    new_account.save()
    return respond("success")


@csrf_exempt
def delete_account(request):
    user = validate_mobile(request)
    if user == None:
        return respond("Error: Invalid Login Credentials")
    user.delete()
    return respond("success")

@csrf_exempt
def create_game(request):
    user = validate_mobile(request)
    if user == None:
        return respond("Error: Invalid Login Credentials")
    
