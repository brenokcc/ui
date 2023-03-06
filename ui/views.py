from django.http import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect('/app/action/listar_componentes/')