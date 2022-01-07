from django.shortcuts import render
from django.http import HttpResponse
from kinotake.models import Vote

def index(request):
    return render(request, 'kinotake/index.html')

def vote(request):
    if request.method == 'POST':
        if request.POST.get('item') == 'kinoko':
            vote = Vote(target=Vote.KINOKO, comment=request.POST['message'])
            vote.save()
        if request.POST.get('item') == 'takenoko':
            vote = Vote(target=Vote.TAKENOKO, comment=request.POST['message'])
            vote.save()

    kinoko_cnt = Vote.objects.filter(target=Vote.KINOKO).count()
    takenoko_cnt = Vote.objects.filter(target=Vote.TAKENOKO).count()
    results = Vote.objects.order_by('-at')

    context = {
        'kinoko_cnt': kinoko_cnt,
        'takenoko_cnt': takenoko_cnt,
        'results': results,
    }
    return render(request, 'kinotake/vote.html', context)
