from Book.codes.book_config import book_configuration
from django.core import serializers
from django.http import HttpResponse
from Book.models import BOOK
from django.http import JsonResponse
import json
import traceback
from django.views.decorators.csrf import csrf_exempt
book_instance = book_configuration()

@csrf_exempt
def add_book(request):

    payload = json.loads(request.body)
    print(payload)

    
    try:

        #id = str(payload['id'])
        book_name = str(payload['book_name'])
        book_image = str(payload['book_image'])
        author = str(payload['author'])
        publisher = str(payload['publisher'])
        owner_user_id = str(payload['owner_user_id'])
        current_user_id = str(payload['current_user_id'])
        date_of_rent = str(payload['date_of_rent'])
        rental_due = str(payload['rental_due'])
        submission_date = str(payload['submission_date'])
        fine_per_day = str(payload['fine_per_day'])
        deposit_by_renter = str(payload['deposit_by_renter'])
        

        if book_instance.add_book(book_name,book_image,author,publisher,owner_user_id,
                                 current_user_id, date_of_rent,
                                 rental_due,submission_date,fine_per_day,
                                 deposit_by_renter): 
            jsonresponse = JsonResponse({'msg':'SUCCESS'}, status= 200 , safe=False)
            return jsonresponse
    except Exception as _:
        traceback.print_exc()
     
    jsonresponse = JsonResponse({'msg':  'FAILURE'}, status= 500, safe=False) 
    return jsonresponse

@csrf_exempt
def get_book_by_book_id(request,qs_json):

      return HttpResponse(qs_json, content_type='application/json')
      


    
        
