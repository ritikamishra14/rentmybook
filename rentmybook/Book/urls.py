from django.conf.urls import url
from Book.codes import book_request

urlpatterns = [
    url(r'^addbook$',book_request.add_book, name="addbook"),
    url(r'^getbookbybookid/$', book_request.get_book_by_book_id, name="getbookbybookid"),
    # url(r'^updateprofilephoto/$', social_request.update_profile_photo, name="updateprofilephoto"),
    # url(r'^deleteuser/$', social_request.delete_user, name="deleteuser"),
    # url(r'^adduser/$', social_request.add_user, name="adduser"),
    # url(r'^enableuser/$', social_request.enable_user, name="enableuser"),
    # url(r'^disableuser/$', social_request.disable_user, name="disableuser"),
    # url(r'^getuserbyemailid/$', social_request.get_user_by_emai_id, name="getuserbyemailid"),
    # url(r'^getuserbyuserid/$', social_request.get_user_by_user_id, name="getuserbyuserid"),

]
