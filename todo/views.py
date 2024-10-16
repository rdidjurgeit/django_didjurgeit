from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Task, PremiumMembership
from .forms import TaskForm, TaskFormPremium, UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})

# Other views
@method_decorator(login_required, name='dispatch')
class TaskList(generic.ListView):
    model = Task
    template_name = 'todo/task_list.html'  # Specify your template name if needed
    
    def get_queryset(self):
        # Show only the tasks created by the logged-in user by Date
        queryset = Task.objects.filter(user=self.request.user)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset.order_by('due_date')  
#Task Create Stage
    
@login_required
def task_create(request):
    Form = get_task_form_class(request.user)
    if request.method == 'POST':  # Check if the form has been submitted
        form = Form(request.POST)  # Bind the form to the submitted data
        if form.is_valid():  # Validate the form
            task = form.save(commit=False)  # Create a task object but don't save it yet
            task.user = request.user  # Assign the task to the logged-in user
            task.save()  # Now save the task
            messages.success(request, 'Task was successfully created!')  # Add success message
            return redirect('task-list')  # Redirect to the task list after saving
    else:
        form = Form()  # Create a new blank form for GET requests

    context = {
        "form": form,
    }
    return render(request, "todo/task_create.html", context)

#Task Edit

@login_required
def task_edit(request, pk):
    Form = get_task_form_class(request.user)
    task = get_object_or_404(Task, pk=pk)  # Get the task or return a 404 if not found
    if request.method == 'POST':
        form = Form(request.POST, instance=task)  # Bind the form to the existing task
        if form.is_valid():
            form.save()  # Save changes to the task
            messages.success(request, 'Task was successfully edit!')  # Add success message
            return redirect('task-list')  # Redirect to task list
    else:
        form = Form(instance=task)  # Populate the form with existing task data

    context = {
        'form': form,
    }
    return render(request, 'todo/task_edit.html', context)

#Task Delete

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()  # Delete the task
        messages.success(request, 'Task was successfully deleted!')  # Add success message
        return redirect('task-list')  # Redirect to task list
    
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

# Task Toggle Status

@login_required
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # Toggle between the statuses
    if task.status == 'not_started':
        task.status = 'in_progress'
    elif task.status == 'in_progress':
        task.status = 'completed'
    else:
        task.status = 'not_started'

    task.save()  # Save the new status
    return redirect('task-list')

def get_task_form_class(user):
    is_premium = user.membership and user.membership.is_active
    return TaskFormPremium if is_premium  else TaskForm

# Premium Membership View
@login_required
def premium_membership(request):
    membership = getattr(request.user, 'membership', None)  # Fetch the user's membership

    if request.method == 'POST':
        if 'activate' in request.POST:
            if not membership:
                membership = PremiumMembership.objects.create(user=request.user)  # Create a new membership
            membership.is_active = True  # Set the membership to active
            membership.save()
            return redirect('task-list')

        elif 'cancel' in request.POST:
            if membership:
                membership.is_active = False  # Set the membership to inactive
                membership.save()
            return redirect('premium-membership')

    return render(request, 'todo/membership.html', {'membership': membership})
