from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import elections.views

from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls), #주소, 실행할 내용
    path('', elections.views.index, name="index"),
    path('areas/<str:area>/', elections.views.areas),
    path('polls/<int:poll_id>/', elections.views.polls),
    path('areas/<str:area>/results', elections.views.results),
]