from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/",views.login , name = 'login'),
    path("signup/", views.signup , name ='signup'),
    path("useracc", views.useracc, name='useracc'),
    path("events",views.event , name = 'events'),
    path('eventinfo/<int:event_ID>', views.eventinfo, name='eventinfo'),
    path("xyz",views.xyz , name = 'xyz'),
    path("organizer_actions",views.organizer_actions , name = 'organizer_actions'),
    path('add_event', views.add_event, name='add_event'),
    path('edit_event', views.edit_event, name='edit_event'),
    path('change_event/<int:event_ID>/', views.change_event, name='change_event'),
    path('userbookinfo',views.userbookeventinfo , name = 'userbookeventinfo'),
    path('add_to_cart/<int:event_ID>/', views.add_to_cart, name='add_to_cart'),
    path('payment', views.payment, name='payment'),
    path('admin_actions', views.admin_actions, name='admin_actions'),
    path('pending', views.pending, name='pending'),
    path('rejected', views.rejected, name='rejected'),
    path('eventaction/<int:event_ID>', views.eventaction, name='eventaction'),
     path('approve_event/<int:event_ID>', views.approve_event, name='approve_event'),
    path('reject_event/<int:event_ID>', views.reject_event, name='reject_event'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('logout/', views.logout, name='logout'),
    path('delete/<int:event_ID>/', views.delete, name='delete'),
    path('remove',views.remove, name='remove'),
    path('editacc',views.editacc, name = 'editacc'),
    path('edit',views.edit,name = 'edit'),
    path('delete_booking/<int:event_ID>/', views.delete_booking, name='delete_booking'),
    

 
]
