from Book.codes.book_config import book_configuration
from django.http import JsonResponse
import json
import traceback
# from django.http import HttpResponse
# from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

book_instance = book_configuration()


def add_book(request):
    payload = json.loads(request.body)
    print(payload)

    try:
        id = str(payload["id"])
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

        if book_instance.add_book(id, book_name, book_image, author, publisher,
                                  owner_user_id, current_user_id,
                                  date_of_rent, rental_due, submission_date, fine_per_day,
                                  deposit_by_renter):
            jsonresponse = JsonResponse({'msg': 'SUCCESS'}, status=200, safe=False)
            return jsonresponse
    except Exception as _:

        traceback.print_exc()

    jsonresponse = JsonResponse({'msg': 'FAILURE'}, status=500, safe=False)
    return jsonresponse


@csrf_exempt
def get_book_by_book_id(request):
    payload = json.loads(request.body)
    response_message = {}
    json_res = []
    print(payload)

    try:
        id = str(payload['id'])
        print(id)
        response_message = book_instance.get_book_by_book_id(id)
        print(response_message)
    except Exception as _:
        response_message = None
        traceback.print_exc()

    jsonresponse = JsonResponse(response_message, status=200, safe=False)
    return jsonresponse


@csrf_exempt
def get_book_by_author(request):
    payload = json.loads(request.body)
    response_message = {}
    json_res = []
    print(payload)

    try:
        author = str(payload['author'])
        print(author)
        response_message = book_instance.get_book_by_author(author)
        print(response_message)
    except Exception as _:
        response_message = None
        traceback.print_exc()

    jsonresponse = JsonResponse(response_message, status=200, safe=False)
    return jsonresponse


@csrf_exempt
def get_book_by_name(request):
    payload = json.loads(request.body)
    response_message = {}
    json_res = []
    print(payload)

    try:
        book_name = str(payload['book_name'])
        print(book_name)
        response_message = book_instance.get_book_by_name(book_name)
        print(response_message)
    except Exception as _:
        response_message = None
        traceback.print_exc()

    jsonresponse = JsonResponse(response_message, status=200, safe=False)
    return jsonresponse


@csrf_exempt
def delete_book(request):
    payload = json.loads(request.body)

    try:
        id = str(payload['id'])
        response_message = book_instance.delete_book(id)
    except Exception as _:
        response_message = None
        traceback.print_exc()
    jsonresponse = JsonResponse(response_message, status=200, safe=False)
    return jsonresponse


@csrf_exempt
def rent_book(request):
    payload = json.loads(request.body)

    try:
        id = str(payload['id'])
        current_user_id = str(payload['current_user_id'])
        date_of_rent = str(payload['date_of_rent'])
        submission_date = str(payload['submission_date'])
        rental_due = str(payload['rental_due'])
        deposit_by_renter = str(payload['deposit_by_renter'])

        if book_instance.rent_book(id, current_user_id,
                                   date_of_rent, submission_date,
                                   rental_due, deposit_by_renter):
            jsonresponse = JsonResponse({'msg': 'SUCCESS'}, status=200, safe=False)
            return jsonresponse
    except Exception as _:
        traceback.print_exc()

    jsonresponse = JsonResponse({'msg': 'FAILURE'}, status=500, safe=False)
    return jsonresponse


@csrf_exempt
def check_book_status(request):
    payload = json.loads(request.body)

    try:
        id = str(payload['id'])
        print(id)
        response_message = book_instance.check_book_status(id)
        # print(response_message)
    except Exception as _:
        response_message = None
        traceback.print_exc()

    jsonresponse = JsonResponse(response_message, status=200, safe=False)
    return jsonresponse
