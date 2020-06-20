from social.codes.social_config import social_configuration
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import json
import traceback
from django.views.decorators.csrf import csrf_exempt
social_instance = social_configuration()

@csrf_exempt
def add_user(request):

    payload = json.loads(request.body)
    print(payload)

    try:
        email_id = str(payload['email_id'])
        name = str(payload['name'])
        address1 = str(payload['address1'])
        state = str(payload['state'])
        city = str(payload['city'])
        contact = str(payload['contact'])

        if social_instance.add_user(email_id, name, address1, state,
                                    city,contact):
            jsonresponse = JsonResponse({'msg':'SUCCESS'}, status= 200 , safe=False)
            return jsonresponse
    except Exception as _:
        traceback.print_exc()

    jsonresponse = JsonResponse({'msg':  'FAILURE'}, status= 500, safe=False)
    return jsonresponse


@csrf_exempt
def get_user_by_email_id(request):

    payload = json.loads(request.body)
    response_message = {}
    json_res = []
    print(payload)

    try:
        email_id = str(payload['email_id'])
        print(email_id)
        response_message =social_instance.get_user_by_email_id(email_id)
        print(response_message)
    except Exception as _:
        response_message = None
        traceback.print_exc()
    
    jsonresponse = JsonResponse(response_message, status= 200, safe=False)
    return jsonresponse

@csrf_exempt
def delete_user(request):

    payload = json.loads(request.body)

    try:
        email_id = str(payload['email_id'])
        response_message = social_instance.delete_user(email_id)
    except Exception as _:
        response_message = None
        traceback.print_exc()
    jsonresponse = JsonResponse(response_message, status= 200, safe=False)
    return jsonresponse

@csrf_exempt
def enable_user(request):
    payload = json.loads(request.body)

    try:
        email_id = str(payload['email_id'])
        response_message = social_instance.enable_user(email_id)
    except Exception as _:
        response_message = None
        traceback.print_exc()
    jsonresponse = JsonResponse(response_message, status= 200, safe=False)
    return jsonresponse

@csrf_exempt
def disable_user(request):
    payload = json.loads(request.body)

    try:
        email_id = str(payload['email_id'])
        response_message = social_instance.disable_user(email_id)
    except Exception as _:
        response_message = None
        traceback.print_exc()
    jsonresponse = JsonResponse(response_message, status= 200, safe=False)
    return jsonresponse

@csrf_exempt
def complete_user(request):
    payload = json.loads(request.body)

    try:
        email_id = str(payload['email_id'])
        gender = str(payload['gender'])
        user_image = str(payload['user_image'])
        address2 = str(payload['address2'])
        landmark = str(payload['landmark'])
        status = str(payload['status'])
        zip_code = str(payload['zip_code'])
        time_zone = str(payload['time_zone'])

        if social_instance.complete_user(email_id,gender, user_image,
                                         address2, landmark, status,
                                         zip_code, time_zone
                                         ):

            jsonresponse = JsonResponse({'msg': 'SUCCESS'}, status=200, safe=False)
        return jsonresponse

    except Exception as _:
        traceback.print_exc()

    jsonresponse = JsonResponse({'msg': 'FAILURE'}, status=500, safe=False)
    return jsonresponse

@csrf_exempt
def get_user_by_user_id(request):
    payload = json.loads(request.body)
    response_message = {}
    print(payload)

    try:
        id = str(payload['id'])
        response_message =social_instance.get_user_by_user_id(id)
        print(response_message)
    except Exception as _:
        response_message = None
        traceback.print_exc()

    jsonresponse = JsonResponse(response_message, status= 200, safe=False)
    return jsonresponse


