from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def sign_out(request):
    """
    Sign out from the site.
    """
    logout(request)
    return HttpResponseRedirect('/sign_in/')
