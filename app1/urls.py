
from django.urls import path
from .views import student_list, student_detail,  LibraryRegisterListCreateView, LibraryRegisterRetrieveUpdateDestroyView

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    # path('library-register/', LibraryRegisterListCreateView.as_view(), name='library-register-list'),
    # path('library-register/<str:slno>/', LibraryRegisterRetrieveUpdateDestroyView.as_view(), name='library-register-detail'), 
    path(
        "library-register/",
        LibraryRegisterListCreateView.as_view(),
        name="library-register-list-create",
    ),
    path(
        "library-register/<str:slno>/",
        LibraryRegisterRetrieveUpdateDestroyView.as_view(),
        name="library-register-retrieve-update-destroy",
    ),
]