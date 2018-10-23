from django.shortcuts import render
from .models import Notice

def index(request):
    notice =Notice.objects.all()
    return render(request, 'app/index.html  ',{'list': notice})
def detail(request):
    item = Notice.objects.get(id=1)
    # item = notice.objects get(pk=1)
    return render(request, 'app/detail.html',{'item'})