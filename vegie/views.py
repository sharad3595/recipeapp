from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def recipes(request):
    if request.method == 'POST':
        form_data = request.POST
        # print(form_data)
        
        # print(recipe_image)
        recipe_name = form_data.get('recipe_name')
        recipe_desc = form_data.get('description')
        recipe_image = request.FILES['recipe_image']

        Vegie.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_desc,
            recipe_image = recipe_image,
            )    
        return redirect("/recipe/")
    queryset = Vegie.objects.all()
    context = {'recipes':queryset}
    return render(request,'vegie/recipes.html',context)

def recipe_delete(request,id):
    recipe = Vegie.objects.get(pk=id)
    recipe.delete()
    messages.success(request,'Recipe deleted successfully!!')
    return redirect('/recipe')

def recipe_edit(request,pk):
    queryset = Vegie.objects.get(pk=pk)
   

    if request.method == "POST":
        form_data = request.POST
        
        recipe_name = form_data.get('recipe_name')
        recipe_desc = form_data.get('description')
        recipe_image = request.FILES['recipe_image']

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_desc
        
        if recipe_image:
            queryset.recipe_image = recipe_image
        else:
            queryset.recipe_image = ""
        
        queryset.save()
        return redirect('/recipe')
    
    context = {'recipe':queryset}
    return render(request,'vegie/update_recipe.html',context)