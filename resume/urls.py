from django.urls import path
from .import views

urlpatterns = [
    path('health/',views.health,name='health'),
    path('candidates/',views.create_candidate,name='create_candidate'),
    path('candidates/list',views.list_candidate,name='list_candidates'),
    path('candidate/<str:candidate_id>',views.get_candidate,name='get_candidate'),
    path('candidate/delete/<str:candidate_id>',views.delete_candidate,name='delete_candidate'),

]
