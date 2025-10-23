from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    #path("liste/",views.list_conferences,name="list_conferences"),
    path("liste/",ConferenceList.as_view(),name="list_conferences"),
    path("<int:pk>/",Conferencedetail.as_view(),name="conferencedetail"),
    path("from/",ConferenceCreate.as_view(),name="add_conference"),
]