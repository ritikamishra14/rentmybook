from social.models import USER
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import traceback


class social_configuration:

    def _init_(self):
        pass

    def add_user(self, email_id, name, address1, state, city,
                 contact):
        try:
            new_user = USER(email_id=email_id,
                            name=name,
                            address1=address1,
                            state=state,
                            city=city,
                            contact=contact)
            new_user.save()
            return True
        except Exception as ex:
            print(ex)
            traceback.print_exc()
        return False

    def complete_user(self, email_id, gender, user_image, address2, landmark, status,zip_code, time_zone):
        try:
            user_exist = USER.objects.get(email_id=email_id)
            user_exist.gender=gender
            user_exist.user_image=user_image
            user_exist.address2=address2
            user_exist.landmark=landmark
            user_exist.status=status
            user_exist.zip_code=zip_code
            user_exist.time_zone=time_zone
            user_exist.save()
            return True

        except ObjectDoesNotExist:
            user_exist = None
        return False

    def update_profile_photo(self, user_name, email_id, contact):
        pass

    def delete_user(self, email_id):
        try:
            USER.objects.filter(email_id=email_id).delete()
            return True
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")
        return False

    def enable_user(self, email_id):
        try:
            user_row = USER.objects.get(email_id=email_id)
            user_row.status = 'ACTIVE'
            user_row.save()
            return True
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")
            user_row = None
        return False

    def disable_user(self, email_id):
        try:
            user_row = USER.objects.get(email_id=email_id)
            user_row.status = 'INACTIVE'
            user_row.save()
            return True
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")
            user_row = None
        return False

    def get_user_by_email_id(self, email_id):
        try:
            user_row = USER.objects.filter(email_id=email_id)
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")
            user_row = None
        if user_row is not None:
            for user in user_row:
                user_obj = {}
                user_obj['email_id'] = user.email_id
                user_obj['gender'] = user.gender
                user_obj['date_of_creation'] = user.date_of_creation
                #user_obj['user_image'] = user.user_image
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

    def get_user_by_user_id(self, id):
        try:
            user_row = USER.objects.filter(id=id)
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")
            user_row = None
        if user_row is not None:
            for user in user_row:
                user_obj = {}
                user_obj['email_id'] = user.email_id
                user_obj['gender'] = user.gender
                user_obj['date_of_creation'] = user.date_of_creation
                #user_obj['user_image'] = user.user_image
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

    # def generate_user_obj(self):
