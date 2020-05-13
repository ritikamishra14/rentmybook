from social.codes.social_config import social_configuration
from django.http import JsonResponse
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
        gender = str(payload['gender'])
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

        if social_instance.add_user(email_id, gender ,
                                    user_image, name, address1, address2,
                                    landmark, state, city, zip_code, status,
                                    contact, time_zone, user_lat, user_lng):
            jsonresponse = JsonResponse({'msg':'SUCCESS'}, status= 200 , safe=False)
            return jsonresponse
    except Exception as _:
        traceback.print_exc()

    jsonresponse = JsonResponse({'msg':  'FAILURE'}, status= 500, safe=False)
    return jsonresponse

 def get_user_by_email_id(request)
    payload = json.loads(request.body)
    response_message = {}    
    print(payload)
    try:
        email_id=str(payload['email_id'])
        response_message =social_instance.get_user_by_email_id(email_id)
    except Exception as _:
        response_message = None
        traceback.print_exc()
    jsonresponse = JsonResponse(response_message, status= 500, safe=False)
    return jsonresponse

 