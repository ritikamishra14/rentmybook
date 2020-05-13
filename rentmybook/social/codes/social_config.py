
from social.models import USER
import traceback


class social_configuration:

    def _init_(self):
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
            return True
        except Exception as ex:
            print(ex)
            traceback.print_exc()
        return False

    def complete_user(self, gender, address, dob, city, postel_code, contact_no):
        pass

    def update_profile_photo(self, user_name, email_id, contact):
        pass

    def delete_user(self, ids: list):
        pass

    def enable_user(self, user_id):
        pass

    def disable_user(self, user_id):
        pass

    def get_user_by_emai_id(self, user_id):
    	try:
    		user_row = USER.objects.get(id=user_id)
    	except:
    		user_row = None
    	if user_row is not None:
    		for user in user_row:
    			user_obj = {}
    			user_obj['email_id'] = user.email_id
    			user_obj['gender'] = user.gender
                user_obj['date_of_creation'] = user.date_of_creation
                user_obj['user_image'] = user.ser_image
                user_obj['name'] = user.name
                user_obj['address1'] = user.address1
                user_obj['address2'] = user.address2
                user_obj['landmark'] = user.landmark
                user_obj['state'] = user.state
                user_obj['city'] = user.city
                user_obj['zip_code'] = user.zip_code
                user_obj['status'] = user.status
                user_obj['contact'] = user.contact
                user_obj['time_zone'] = user.time_zone
                user_obj['user_lat'] = user.user_lat
                user_obj['user_lng'] = user.user_lng
            return user_obj
        return None

    def get_user_by_user_id(self, user_id):
        pass

    # def generate_user_obj(self):