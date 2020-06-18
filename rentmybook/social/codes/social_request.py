from social.codes.social_config import social_configuration
from django.http import JsonResponse
# from django.http import HttpResponse
# from django.core import serializers
import json
import traceback
from django.views.decorators.csrf import csrf_exempt

social_instance = social_configuration()


@csrf_exempt
def add_user(request):
    payload = json.loads(request.body)
    print(payload)

    try:
        id = str(payload['id'])
        email_id = str(payload['email_id'])
        gender = str(payload['gender'])
        date_of_creation = str(payload['date_of_creation'])
        user_image = str(payload['user_image'])
        name = str(payload['name'])
        address1 = str(payload['address1'])
        address2 = str(payload['address2'])
        landmark = str(payload['landmark'])
        state = str(payload['state'])
        city = str(payload['city'])
        zip_code = str(payload['zip_code'])
        status = str(payload['status'])
        contact = str(payload['contact'])
        time_zone = str(payload['timezone'])
        user_lat = str(payload['user_lat'])
        user_lng = str(payload['user_lng'])

        if social_instance.add_user(id, email_id, gender, date_of_creation,
                                    user_image, name, address1, address2,
                                    landmark, state, city, zip_code, status,
                                    contact, time_zone, user_lat, user_lng):
            jsonresponse = JsonResponse({'msg': 'SUCCESS'}, status=200, safe=False)
            return jsonresponse
    except Exception as _:
        traceback.print_exc()

    jsonresponse = JsonResponse({'msg': 'FAILURE'}, status=500, safe=False)
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
        response_message = social_instance.get_user_by_email_id(email_id)
        print(response_message)
    except Exception as _:
        response_message = None
        traceback.print_exc()

    jsonresponse = JsonResponse(response_message, status=200, safe=False)
    return jsonresponse
