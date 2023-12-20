from django.urls import path


from .views import create_term, TermList, TermDetail

urlpatterns = [
    path('create_term', create_term, name='create_term'),
    path('term/', TermList.as_view(), name='term_list'),
    path('term/<int:pk>/', TermDetail.as_view(), name='term_detail'),
]
