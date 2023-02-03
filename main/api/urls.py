
from django.urls import path
from api.views import  get_token_view , add , subtract , multiply , divide


app_name = 'api'
urlpatterns = [
    path('token/', get_token_view),
    path('add/' , add, name='add'),
    path('subtract/' , subtract),
    path('multiply/' , multiply),
    path('divide/' , divide),
]