from django.urls import path
from myapp.views import *


urlpatterns=[
    path('',index,name="index"),
    path('payment',payment,name="payment"),
    path('mail',mail_send,name="mail"),
    path('htmlmail',mail_html,name='htmlmail'),
    path("attach",mail_attach,name="attach"),
    
]