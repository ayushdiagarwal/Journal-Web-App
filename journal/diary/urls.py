from django.urls import path
from .views import index, EntryCreate, Profile, EntryUpdate, EntryDelete

app_name = 'diary'

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('create/', EntryCreate.as_view(), name="entry-create"),
    path('entry/<int:pk>/update', EntryUpdate.as_view(), name="entry-update"),
    path('entry/<int:pk>/delete', EntryDelete.as_view(), name="entry-delete"),
    path('profile/', Profile, name='profile')
]
