from django.conf.urls import url
from social.codes import social_request




urlpatterns = [
    url(r'^adduser$',social_request.add_user, name="adduser"),
    url(r'^completeuser/$', social_request.complete_user, name="completeuser"),
    # url(r'^updateprofilephoto/$', social_request.update_profile_photo, name="updateprofilephoto"),
    url(r'^deleteuser/$', social_request.delete_user, name="deleteuser"),
    url(r'^enableuser/$', social_request.enable_user, name="enableuser"),
    url(r'^disableuser/$', social_request.disable_user, name="disableuser"),
    url(r'^getuserbyemailid/$', social_request.get_user_by_email_id, name="getuserbyemailid"),
    url(r'^getuserbyuserid/$', social_request.get_user_by_user_id, name="getuserbyuserid"),

]
