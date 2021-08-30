from django.shortcuts import render
import logging
logger = logging.getLogger('main')
# Create your views here.
def home(request) :
    """
    메인화면 출력
    """
    logger.info('INFO 레벨로 출력')
    return render(request, 'main/faust/home.html')

def faust1(request) :
    """
    faust1 화면 출력
    """
    return render(request, 'main/faust/faust1.html')

def faust2(request) :
    """
    faust2 화면 출력
    """
    return render(request, 'main/faust/faust2.html')

def faust3(request) :
    """
    faust3 화면 출력
    """
    return render(request, 'main/faust/faust3.html')

def faust4(request) :
    """
    faust4 화면 출력
    """
    return render(request, 'main/faust/faust4.html')

def faust5(request) :
    """
    faust5 화면 출력
    """
    return render(request, 'main/faust/faust5.html')

def faust6(request) :
    """
    faust6 화면 출력
    """
    return render(request, 'main/faust/faust6.html')


def faust7(request) :
    """
    faust7 화면 출력
    """
    return render(request, 'main/faust/faust7.html')

def faust8(request) :
    """
    faust8 화면 출력
    """
    return render(request, 'main/faust/faust8.html')

def faust9(request) :
    """
    faust9 화면 출력
    Red Wine
    """
    return render(request, 'main/faust/faust9.html')



def collage(request):
    return render(request, 'main/collage/collage.html')

def collage1(request):
    return render(request, 'main/collage/collage1.html')

def collage2(request):
    return render(request, 'main/collage/collage2.html')

def collage3(request):
    return render(request, 'main/collage/collage3.html')

def collage4(request):
    return render(request, 'main/collage/collage4.html')

def collage5(request):
    return render(request, 'main/collage/collage5.html')

def collage6(request):
    return render(request, 'main/collage/collage6.html')

def collage7(request):
    return render(request, 'main/collage/collage7.html')

def collage8(request):
    return render(request, 'main/collage/collage8.html')

def collage9(request):
    return render(request, 'main/collage/collage9.html')

def collage10(request):
    return render(request, 'main/collage/collage10.html')

def collage11(request):
    return render(request, 'main/collage/collage11.html')

def collage12(request):
    return render(request, 'main/collage/collage12.html')

def painting(request):
    return render(request, 'main/painting/painting.html')

def painting1(request):
    return render(request, 'main/painting/painting1.html')

def painting2(request):
    return render(request, 'main/painting/painting2.html')

def painting3(request):
    return render(request, 'main/painting/painting3.html')

def painting4(request):
    return render(request, 'main/painting/painting4.html')

def painting5(request):
    return render(request, 'main/painting/painting5.html')

def painting6(request):
    return render(request, 'main/painting/painting6.html')

def painting7(request):
    return render(request, 'main/painting/painting7.html')

def painting8(request):
    return render(request, 'main/painting/painting8.html')

def painting9(request):
    return render(request, 'main/painting/painting9.html')

def painting10(request):
    return render(request, 'main/painting/painting10.html')

def pastel(request):
    return render(request, 'main/pastel/pastel.html')

def pastel1(request):
    return render(request, 'main/pastel/pastel1.html')

def digital(request):
    return render(request, 'main/digital/digital.html')

def digital1(request):
    return render(request, 'main/digital/digital1.html')

def artist_note(request):
    return render(request, 'main/artist_note.html')

def about(request):
    return render(request, 'main/about.html')