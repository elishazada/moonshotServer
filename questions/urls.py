from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^$', views.question_list),
]