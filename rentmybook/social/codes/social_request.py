from social.codes.social_config import social_configuration
from django.http import JsonResponse
import json, traceback


social_instance = social_configuration()


def add_user(request):

    try:
        email_id = str(request.POST.get('email_id'))
        gender = str(request.POST.get('gender'))
        date_of_creation = str(request.POST.get('date_of_creation'))
        user_image = str(request.POST.get('user_image'))
        name = str(request.POST.get('name'))
        address1 = str(request.POST.get('address1'))
        address2 = str(request.POST.get('address2'))
        landmark = str(request.POST.get('landmark'))
        state = str(request.POST.get('state'))
        city = str(request.POST.get('city'))
        zip_code = str(request.POST.get('zip_code'))
        status = str(request.POST.get('status'))
        contact = str(request.POST.get('contact'))
        time_zone = str(request.POST.get('time_zone'))
        user_lat = str(request.POST.get('user_lat'))
        user_lng = str(request.POST.get('user_lng'))

        if social_instance.add_user(email_id, gender ,date_of_creation,
                                    user_image, name, address1, address2,
                                    landmark, state, city, zip_code, status,
                                    contact, time_zone, user_lat, user_lng):
            jsonresponse = JsonResponse({'msg':'SUCCESS'}, status= 200 , safe=False)
            return jsonresponse
    except Exception as _:

        traceback.print_exc()

    jsonresponse = JsonResponse({'msg':  'FAILURE'}, status= 500, safe=False)
    return jsonresponse