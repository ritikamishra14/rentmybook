from django.conf.urls import url
from Book.codes import book_request

urlpatterns = [
    url(r'^addbook$', book_request.add_book, name="addbook"),
    url(r'^getbookbybookid$', book_request.get_book_by_book_id, name="getbookbybookid"),
    url(r'^getbookbyname$', book_request.get_book_by_name, name="getbookbyname"),
    url(r'^deletebook$', book_request.delete_book, name="deletebook"),
    url(r'^checkbookstatus$', book_request.check_book_status, name="checkbookstatus"),
    # url(r'^change/$', social_request.enable_user, name="enableuser"),
    # url(r'^disableuser/$', social_request.disable_user, name="disableuser"),
    url(r'^rentbook$', book_request.rent_book, name="rentbook"),
    url(r'^getbookbyauthor$', book_request.get_book_by_author, name="getbookbyauthor"),

]
