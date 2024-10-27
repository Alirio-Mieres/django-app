from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, CustomLoginView, edit_account_view, notes_view, save_note, delete_note, create_note

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('edit/', edit_account_view, name='edit_account'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('notes/', notes_view, name='notes'),
    path('notes/save/<int:note_id>/', save_note, name='save_note'),
    path('notes/delete/<int:note_id>/', delete_note, name='delete_note'),
    path('notes/new/', create_note, name='create_note'),
]
