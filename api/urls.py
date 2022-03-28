from django.urls import path
from api.views import AuthorList
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


app_name="api"

urlpatterns=[
    path('api/', AuthorList.as_view()),
    path('api/<int:id>/',AuthorList.as_view()),
]