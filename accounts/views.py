from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Note
from django.shortcuts import get_object_or_404


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

@login_required
def edit_account_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_account.html', {'form': form})


@login_required
def notes_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'accounts/notes.html', {'notes': notes})

@login_required
def save_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.content = request.POST['content']
        note.save()
    return redirect('notes')

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
    return redirect('notes')

@login_required
def create_note(request):
    if request.method == 'POST':
        Note.objects.create(user=request.user, content=request.POST.get('content', ''))
        return redirect('notes')
    return render(request, 'accounts/create_note.html')