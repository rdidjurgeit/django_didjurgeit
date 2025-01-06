from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages

from .models import Task, PremiumMembership
from .forms import TaskForm, TaskFormPremium, UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class TaskList(generic.ListView):
    model = Task
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        # Show tasks only by the logged-in user
        queryset = Task.objects.filter(user=self.request.user)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset.order_by('due_date')


@login_required
def task_create(request):
    FormClass = get_task_form_class(request.user)
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task successfully created!')
            return redirect('task-list')
    else:
        form = FormClass()
    return render(request, 'todo/task_create.html', {"form": form})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        messages.error(request, "You cannot edit another user's task.")
        return redirect('task-list')

    FormClass = get_task_form_class(request.user)
    if request.method == 'POST':
        form = FormClass(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task successfully updated!')
            return redirect('task-list')
    else:
        form = FormClass(instance=task)
    return render(request, 'todo/task_edit.html', {'form': form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        messages.error(request, "You cannot delete another user's task.")
        return redirect('task-list')

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task was successfully deleted!')
        return redirect('task-list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})


@login_required
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        messages.error(request, "You cannot modify another user's task.")
        return redirect('task-list')

    if task.status == 'not_started':
        task.status = 'in_progress'
    elif task.status == 'in_progress':
        task.status = 'completed'
    else:
        task.status = 'not_started'
    task.save()
    return redirect('task-list')


def get_task_form_class(user):
    membership = getattr(user, 'membership', None)
    is_premium = membership and membership.is_active
    return TaskFormPremium if is_premium else TaskForm


@login_required
def premium_membership(request):
    membership = getattr(request.user, 'membership', None)
    if request.method == 'POST':
        if 'activate' in request.POST:
            if not membership:
                membership = PremiumMembership.objects.create(user=request.user)
            membership.is_active = True
            membership.save()
            return redirect('task-list')
        elif 'cancel' in request.POST:
            if membership:
                membership.is_active = False
                membership.save()
            return redirect('premium-membership')
    return render(request, 'todo/membership.html', {'membership': membership})
