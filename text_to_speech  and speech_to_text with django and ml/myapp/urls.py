
from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name="base"),
 
    path('text-to-speech/',views.index,name="text-to-speech"),
    path('text-to-speech/ss',views.some,name='some'),

    path('speech_to_text/',views.speech_to_text,name="speech_to_text"),
    path('record/',views.record,name='record')

]
