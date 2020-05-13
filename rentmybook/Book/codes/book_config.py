from Book.models import BOOK
import traceback

class book_configuration:

    
    def __init__(self):
        pass
    def add_book(self,book_name,book_image,author,publisher,owner_user_id,
                current_user_id,date_of_rent,rental_due,submission_date,fine_per_day,deposit_by_renter):

        try:
            new_book = BOOK(
                #id = id,
                book_name = book_name,
                book_image = book_image,
                author = author,
                publisher = publisher,
                owner_user_id = owner_user_id,
                current_user_id = current_user_id,
                date_of_rent = date_of_rent,
                rental_due = rental_due,
                submission_date = submission_date,
                fine_per_day = fine_per_day,
                deposit_by_renter = deposit_by_renter)

            new_book.save()
            return True
        except Exception as ex:
            print(ex)
            traceback.print_exc()
        return False

    def get_book_by_book_id(self,id):
        all_entries = []
        try:
            all_entries = BOOK.objects.get(id=id)        
        except Exception as ex:
            print(ex)
            traceback.print_exc()
        if  all_entries is not None:
            qs_json = serializers.serialize('json', all_entries)
 

    def edit_book_photo(self,id, image_list):
        pass
          
    def delete_book(self, ids: list):
        pass

    def check_book_status(self,id,current_user,date_of_rent,rental_due,submission_date):
        pass

    def  rent_book(self,id,user_id,date_of_rent,date_of_submission,rental_due,deposit_by_renter):
        pass
    
    def get_book_by_name(self,id):
        pass

    def get_book_by_author(self,id):
        pass

    #def generate_return_obj(self,):



        
            
