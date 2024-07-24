from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import adoption_application ,user_details
from django.contrib.auth import login,logout


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)     
            return'done_registration'
    else:
        form= UserCreationForm()
        return render(request,'user_app/user_register.html',{'form':form})






def user_login(request):
    return redirect(request,'user_app/user_login.html')


def dashboard(request):
    pass


def user_logout(request):
    pass











def adoption_application(request):
    if request.method == 'POST':
        form = application_form (request.POST, request.FILES)
        if form.is_valid():
            application_form = form.save(commit=False)
            application_form.username = request.username
            application_form.password = request.password
            application_form.save()
            print('message: submition successfull')
            return redirect('pet_app.views/pet_list')
    else:

        form = application_form()
        return render(request, 'adoption_application.html', {'form':form})
    
def application_edit(request,application_id):
    application = get_list_or_404(adoption_application, pk=application_id,username = request.username)
    if request.method == 'POST':
        form = application_form(request.POST, request.FILES, instance=adoption_application)##### GIVING INSTANCE HERE TO UNDERSTAND THAT WE ARE EDITING OUR LAST APPLICATION FORM
        if form.is_valid():
            application_form = form.save(commit=False)
            application_form.username = request.username # #to show that the same username editid the application
            application_form.save()
            return redirect('pet_app.views/pet_list')
    else:
        form = adoption_application(instance= adoption_application)
    return render(request, 'adoption_application.html', {'form':form})

   
def application_delete(request,application_id):
    application = get_list_or_404(adoption_application, pk=application_id,username = request.username)
    if request.method == 'POST':
        application.delete()
        return redirect('pet_app.views/pet_list')
    return render(request, 'application_delete.html', {'application':application})
