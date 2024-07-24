from django.shortcuts import render,redirect
from .models import pet_details
from .forms import pet_forms
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def pet_list(request):
     pet_detail = pet_details.objects.all()
     page = request.GET.get('page',1)
     paginator = Paginator(pet_detail, 1)
     try:
         pet_detail = paginator.page(page)

     except PageNotAnInteger:
         pet_detail = paginator.page(1)

     except EmptyPage:
         pet_detail = paginator.page(paginator.num_pages)

     context= {'pet_detail': pet_detail}
     return render(request, 'pet_list.html',context )
    
    

def pet_avilability_create(request):
    if request.method == 'POST':
        form = pet_forms (request.POST, request.FILES)
        if form.is_valid():
            pet_forms = form.save(commit=False)
            pet_forms.username = request.username
            pet_forms.save()
            return redirect('pet_app.views/pet_list')
    else:

        form = pet_forms()
        return render(request, 'pet_avilability_create.html', {'form':form})
    
def pet_list_edit(request,pet_list_id):
    pet_list = get_list_or_404(pet_avilability_create, pk=pet_list_id,username = request.username)
    if request.method == 'POST':
        form = pet_form(request.POST, request.FILES, instance=pet_avilability_create)# GIVING INSTANCE HERE TO UNDERSTAND THAT WE ARE EDITING OUR LAST pet_list FORM
        if form.is_valid():
            pet_form = form.save(commit=False)
            pet_form.username = request.username # to show that the same username editid the pet_list
            pet_form.save()
            return redirect('pet_app.views/pet_list')
    else:
        form = pet_avilability_create(instance= pet_avilability_create)
    return render(request, 'pet_avilability_create.html', {'form':form})

   
def pet_list_delete(request,pet_list_id):
    pet_list = get_list_or_404(pet_avilability_create, pk=pet_list_id,username = request.username)
    if request.method == 'POST':
        pet_list.delete()
        return redirect('pet_app.views/pet_list')
    return render(request, 'pet_list_delete.html', {'pet_list':pet_list})
