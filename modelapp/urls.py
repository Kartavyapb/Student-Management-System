from django.urls import path
from modelapp import views

urlpatterns = [
    path('home/', views.home),

    path('add/', views.add_student_info),
    path('contact/',views.add_contact_info),
    path('parents/',views.add_parents_info),
    path('academic/',views.add_acdemic_info),
    path('course/',views.add_course_info),
    path('fees/',views.add_fees_info),

    path('list/',views.student_list_view),
    path('detail/<int:id>/',views.student_detail_view),
    path('delete/<int:id>/',views.student_delete_view),
    path('update/<int:id>/',views.student_update_view),
    path('register/',views.register),
]
