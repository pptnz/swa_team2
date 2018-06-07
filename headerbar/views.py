from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def sign_out(request):
    """
    Sign out from the site.
    """
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "로그아웃되었습니다.")
    return HttpResponseRedirect('/sign_in/')
