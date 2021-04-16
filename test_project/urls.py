from django.urls import path, reverse_lazy
from django.views.generic import DeleteView

from .views import get_form_data, load_data, edit_items, delete_item

app_name = 'test_project'
urlpatterns = [
    path('', get_form_data, name='get_form_data'),
    path('load/', load_data, name='load_data'),
    path('delete/<int:pk>', delete_item, name='delete_item'),
    path('edit/<int:pk>', edit_items, name='edit_items')
]
