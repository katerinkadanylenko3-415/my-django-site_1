# from . import views
# from django.urls import path
#
# urlpatterns = [
#     path('', views.index, name="home"),
#     # # path('datetime/', views.current_datetime, name="current_datetime"),
#     # path('datetime/', views.CurrentDataTime.as_view()),
#     # path('randomquote/', views.get, name="randomquote"),
# ]

from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.index, name="home"),
    path('news/', views.news, name="news"),
    path('management/', views.management, name="management"),
    path('facts/', views.facts, name="facts"),
    path('contacts/', views.contacts, name="contacts"),

    # History
    path('history/', views.history, name="history"),
    path('history/people/', views.history_people, name="history_people"),
    path('history/photos/', views.history_photos, name="history_photos"),
]

# def index(request):
#     context = {'title': "First data context in render",
#                'text': "add some text in P tes"}
#     return render(request, 'blog/index.html', context)