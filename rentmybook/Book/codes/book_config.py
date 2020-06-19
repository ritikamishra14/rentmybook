from Book.models import BOOK
from django.core.exceptions import ObjectDoesNotExist
import traceback


class book_configuration:

    def __init__(self):
        pass

    def add_book(self, id, book_name, book_image, author, publisher, owner_user_id,
                 current_user_id, date_of_rent, rental_due, submission_date, fine_per_day, deposit_by_renter):

        try:
            new_book = BOOK(
                book_name=book_name,
                book_image=book_image,
                author=author,
                publisher=publisher,
                owner_user_id=owner_user_id,
                current_user_id=current_user_id,
                date_of_rent=date_of_rent,
                rental_due=rental_due,
                submission_date=submission_date,
                fine_per_day=fine_per_day,
                deposit_by_renter=deposit_by_renter)

            new_book.save()
        except Exception as ex:
            print(ex)
            traceback.print_exc()
        return False

    def delete_book(self, id):
        try:
            BOOK.objects.filter(id=id).delete()
            return True
        except ObjectDoesNotExist:
            print("Entry or Blog doesnt exist")
        return False

    def check_book_status(self, id):
        try:
            book_exist = BOOK.objects.get(id=id)
            if book_exist.current_user_id == 'NULL':
                print("Not on rent")
            else:
                print("on rent")
        except ObjectDoesNotExist:
            print("Either The Entry or Blog Doesn't Exist")
        return False

    def rent_book(self, id, current_user_id, date_of_rent, submission_date, rental_due, deposit_by_renter):
        try:
            book_exist = BOOK.objects.get(id=id)
            book_exist.current_user_id=current_user_id
            book_exist.date_of_rent=date_of_rent
            book_exist.submission_date=submission_date
            book_exist.rental_due=rental_due
            book_exist.deposit_by_renter=deposit_by_renter
            book_exist.save()
            return True
        except ObjectDoesNotExist:
            book_exist=None
        return False

    def get_book_by_name(self, book_name):
        try:
            book_row = BOOK.objects.filter(book_name=book_name)
        except ObjectDoesNotExist:
            print("Either The Entry or Blog Doesn't Exist")
            book_row = None
        if book_row is not None:
            for book in book_row:
                book_ob = {}
                book_ob['id'] = book.id
                book_ob['book_name'] = book.book_name
                # book_obj['book_image'] = book.book_image
                book_ob['author'] = book.author
                book_ob['publisher'] = book.publisher
                book_ob['owner_user_id'] = book.owner_user_id
                book_ob['current_user_id'] = book.current_user_id
                book_ob['date_of_rent'] = book.date_of_rent
                book_ob['rental_due'] = book.rental_due
                book_ob['submission_date'] = book.submission_date
                book_ob['fine_per_day'] = book.fine_per_day
                book_ob['deposit_by_renter'] = book.deposit_by_renter
            return book_ob
        return None

    def get_book_by_author(self, author):
        try:
            book_row = BOOK.objects.filter(author=author)
        except ObjectDoesNotExist:
            print("Either The Entry or Blog Doesn't Exist")
            book_row = None
        if book_row is not None:
            for book in book_row:
                book_obb = {}
                book_obb['id'] = book.id
                book_obb['book_name'] = book.book_name
                # book_obb['book_image'] = book.book_image
                book_obb['author'] = book.author
                book_obb['publisher'] = book.publisher
                book_obb['owner_user_id'] = book.owner_user_id
                book_obb['current_user_id'] = book.current_user_id
                book_obb['date_of_rent'] = book.date_of_rent
                book_obb['rental_due'] = book.rental_due
                book_obb['submission_date'] = book.submission_date
                book_obb['fine_per_day'] = book.fine_per_day
                book_obb['deposit_by_renter'] = book.deposit_by_renter
            return book_obb
        return None

    def get_book_by_book_id(self, id):
        try:
            book = BOOK.objects.get(id=id)
        except ObjectDoesNotExist:
            print("Either The Entry or Blog Doesn't Exist")
            book = None
        if book is not None:
            # for book in book_row:
            book_obj = {}
            book_obj['id'] = book.id
            book_obj['book_name'] = book.book_name
            # book_obj['book_image'] = book.book_image
            book_obj['author'] = book.author
            book_obj['publisher'] = book.publisher
            book_obj['owner_user_id'] = book.owner_user_id
            book_obj['current_user_id'] = book.current_user_id
            book_obj['date_of_rent'] = book.date_of_rent
            book_obj['rental_due'] = book.rental_due
            book_obj['submission_date'] = book.submission_date
            book_obj['fine_per_day'] = book.fine_per_day
            book_obj['deposit_by_renter'] = book.deposit_by_renter
            return book_obj
        return None

        # except Exception as ex:
        #     print(ex)
        #     traceback.print_exc()
        # if  all_entries is not None:
        #     qs_json = serializers.serialize('json', all_entries)

    def edit_book_photo(self, id, image_list):
        pass

    # def generate_return_obj(self,):
