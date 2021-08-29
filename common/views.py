from django.shortcuts import render

# Create your views here.

def page_not_found(request,exception) :
    """
    404 page not found
    """
    return render(request,'common/404.html',{})

def test(request) :

    return render(request,'common/test.html')