from django.urls import path
from . import views

urlpatterns = [
  path('', views.JournalListView.as_view(),
       name="journallist"),
  path('journalcreate', views.JournalCreateView.as_view(),
       name="createjournal"),
  path('journalupdate/<pk>', views.JournalUpdateView.as_view(),
       name="updatejournal"),
  path('journaldelete/<pk>', views.JournalDeleteView.as_view(),
       name="deletejournal"),
]
