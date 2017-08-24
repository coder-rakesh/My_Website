from django.shortcuts import render
from .models import Solution
from .models import Tutorial
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def home_page(request):
    return render(request, 'website/home_page.html', {})

def solutions_page(request):
    solutions = Solution.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/solutions_page.html', {'solutions':solutions})

def tutorials_page(request):
    tutorials = Tutorial.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/tutorials_page.html', {'tutorials':tutorials})

def about_page(request):
    return render(request, 'website/about_page.html', {})

def solutions_detail(request, pk):
    solution = get_object_or_404(Solution, pk=pk)
    return render(request, 'website/solutions_detail.html', {'solution':solution})

def tutorials_detail(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'website/tutorials_detail.html', {'tutorial':tutorial})
    

