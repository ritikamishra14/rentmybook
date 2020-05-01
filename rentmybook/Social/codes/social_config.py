from Social.models import USER
import traceback


class social_configuration:

    def __init__(self):
        pass

    def add_user(self,email_id, gender ,date_of_creation, user_image, name, 
                    address1, address2, landmark, state, city, zip_code, 
                    status, contact, time_zone, user_lat, user_lng):
        try:
            new_user = USER(email_id=email_id,
                       gender=gender,
                       date_of_creation=date_of_creation,
                       user_image=user_image,
                       name=name,
                       address1=address1,
                       address2=address2,
                       landmark=landmark,
                       state=state,
                       city=city,
                       zip_code=zip_code,
                       status=status,
                       contact=contact,
                       time_zone=time_zone,
                       user_lat=user_lat,
                       user_lng=user_lng)
            new_user.save()
        except Exception as ex:
            print(ex)
            traceback.print_exc()


    def complete_user(self, gender, address, dob, city, postel_code, contact_no):
        pass

    def upadate_profile_photo(self, user_name, email_id, contact):
        pass

    def delete_user(self, ids: list):
        pass

    def enable_user(self, user_id):
        pass

    def disable_user(self, user_id):
        pass

    def get_user_by_emai_id(self, user_id):
        pass

    def get_user_by_user_id(self, user_id):
        pass

    # def generate_user_obj(self):

