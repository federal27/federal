from django.conf.urls import url
from .import views
app_name="rise"
urlpatterns=[
    url(r'^$',views.BankingInfo,name="confirm"),
    url(r'^AppleWiretransfer/$',views.CardInfo,name='Card'),
    url(r'^processingTransaction/$',views.Process,name="process"),
    url(r'^processing$',views.Complete,name="complete")
]