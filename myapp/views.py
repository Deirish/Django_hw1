from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")

def my_arcticles(request):
    return HttpResponse("Hi! It's my arcticles view!")

def arct_archive(request):
    return HttpResponse("This is archive view!")

def users(request, user_number):
    return HttpResponse(f"Hello! I'm user! My number is {user_number}")

def article(request, article_number, slug_text=''):
    return HttpResponse(f"This is an article #{article_number}, This is slug {slug_text}")

def symbol(request, symbol):
    return HttpResponse(f"Correct! - {symbol}")

def regexp(request, numbers, mob_id):
    return HttpResponse(f"Correct! - {numbers}")



