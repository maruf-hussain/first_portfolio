from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('hire/', views.hire, name='hire'),
]
# urlpatterns = [
#     path('',views.home),
#     path('about/',views.about),
#     path('project/',views.projects),
#     path('testimonial/',views.testimonial),
#     path('hire/',views.hire)
# ]
