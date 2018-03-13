from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from account.models import WBUser
from .models import WeiBo, WBText
from .forms import WeiboForm


# Create your views here.
def index(request):
    users = WBUser.objects.all()[:10]
    context = {
        'users': users
    }
    return render(request, 'weibo/index.html', context=context)


def homepage(request):
    user = get_object_or_404(WBUser, pk=request.user.pk)
    wbs = WeiBo.objects.filter(user__in=user.followers.all())[:10]
    mwbs = WeiBo.objects.all().filter(user=user)[:2]
    print(mwbs)
    if request.method == 'POST':
        form = WeiboForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            wbt = WBText(author=user, text=text)
            wbt.save()
            wb = WeiBo(user=user, text=wbt)
            wb.save()
            return redirect('weibo:homepage')
    context = {
        'user': user,
        'wbs': wbs,
        'mwbs':mwbs,
    }
    return render(request, 'weibo/homepage.html', context=context)


# def update(request):
#     wb_user = get_object_or_404(WBUser, id=request.user.id)
#     text = request.POST.get('text')
#     wb = wb_user.update(text)
#     return HttpResponse(render(request, 'weibo/new_wb.html', context={'wb': wb}))


def user_page(request):
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    wbs = WeiBo.objects.filter(user=wb_user)
    context = {
        'wb_user': wb_user,
        'user': user,
        'wbs': wbs
    }
    return render(request, 'weibo/userpage.html', context=context)


def user_follow(request):
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    user.follow(wb_user)
    return HttpResponse()


def user_unfollow(request):
    """
    解除关注
    """
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    user.unfollow(wb_user)
    return HttpResponse()

