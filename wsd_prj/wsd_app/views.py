from django.shortcuts import render

# Create your views here.
def main(requests):
    return render(requests, 'main.html')

def subscribe(request):
    return render(request, 'subscribe.html')

def subscribe2(request):
    return render(request, 'subscribe2.html')

def subscribe3(request):
    return render(request, 'subscribe3.html')

def subscribe4(request):
    return render(request, 'subscribe4.html')

def introduce(requests):
    return render(requests, 'introduce.html')

def QA(requests):
    return render(requests, 'QA.html')

def review(requests):
    return render(requests, 'review.html')

def product(requests):
    return render(requests, 'product.html')