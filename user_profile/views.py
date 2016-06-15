from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
# Create your views here.


def account_view(request):
    if request.user.is_authenticated():
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'account.html', {})
    else:
        return redirect( '/login')