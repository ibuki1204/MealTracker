from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal
from .forms import MealForm
from django.db.models import Q  # ← 検索用

def index(request):
    query = request.GET.get('q', '')  # URLパラメータ 'q' を取得
    if query:
        meals = Meal.objects.filter(name__icontains=query)  # 部分一致検索
    else:
        meals = Meal.objects.all()
    
    params = {
        'title': 'Meal Tracker',
        'message': 'Welcome to the Meal Tracker!',
        'meals': meals,
        'query': query,
    }
    return render(request, 'main/index.html', params)


def create(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MealForm()
    return render(request, 'main/create.html', {'form': form})

def update(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MealForm(instance=meal)
    return render(request, 'main/update.html', {'form': form, 'meal': meal})

def delete(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('index')
    return render(request, 'main/delete.html', {'meal': meal})



