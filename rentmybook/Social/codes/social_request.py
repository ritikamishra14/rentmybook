from Social.codes.social_config import social_configuration
from django.http import JsonResponse
import json, traceback


social_instance = social_configuration()


def adduser(request):
    try:
        email_id = str(request.POST.get("email_id"))
	    gender = str(request.POST.get("email_id"))
	    date_of_creation = str(request.POST.get("email_id"))
	    user_image = str(request.POST.get("email_id"))
	    name = str(request.POST.get("email_id"))
	    address1 = str(request.POST.get("email_id"))
	    address2 = str(request.POST.get("email_id"))
	    landmark = str(request.POST.get("email_id"))
	    state = str(request.POST.get("email_id"))
	    city = str(request.POST.get("email_id"))
	    zip_code = str(request.POST.get("email_id"))
	    status = str(request.POST.get("email_id"))
	    contact = str(request.POST.get("email_id"))
	    time_zone = str(request.POST.get("email_id"))
	    user_lat = str(request.POST.get("email_id"))
	    user_lng = str(request.POST.get("email_id"))

	    if social_instance.add_user(self,email_id, gender ,date_of_creation,
	    						 user_image, name, address1, address2, 
	    						 landmark, state, city, zip_code, status, 
                    			 contact, time_zone, user_lat, user_lng):
	    	jsonresponse = JsonResponse({"msg":  "SUCCESS"}, status=200, safe=False)
	    	return jsonresponse
    except Exception as e:
        traceback.print_exc()
     
    jsonresponse = JsonResponse({"msg":  "FAILURE"}, status=500, safe=False)
    return jsonresponse
    
