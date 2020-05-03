from Book.codes.book_config import book_configuration
from django.http import JsonResponse
import json, traceback


book_instance = book_configuration()


def add_book(request):
    
    try:
        id = str(request.POST.get('id'))
        book_name = str(request.POST.get('book_name'))
        book_image= str(request.POST.get('book_image'))
        author = str(request.POST.get('author'))
        publisher = str(request.POST.get('publisher'))
        owner_user_id = str(request.POST.get('owner_user_id'))
        current_user_id = str(request.POST.get('current_user_id'))
        date_of_rent = str(request.POST.get('date_of_rent'))
        rental_due = str(request.POST.get('rental_due'))
        submission_date= str(request.POST.get('submission_date'))
        fine_per_day = str(request.POST.get('fine_per_day'))
        deposit_by_renter = str(request.POST.get('deposit_by_renter'))
        

        if book_instance.add_book(id,book_name,book_image,author,publisher,
                                 owner_user_id,current_user_id,
                                 date_of_rent,rental_due,submission_date,fine_per_day,
                                 deposit_by_renter ): 
                                 jsonresponse = JsonResponse({'msg':'SUCCESS'}, status= 200 , safe=False)
                                 return jsonresponse
    except Exception as _:
    
        traceback.print_exc()
     
    jsonresponse = JsonResponse({'msg':  'FAILURE'}, status= 500, safe=False)
    return jsonresponse