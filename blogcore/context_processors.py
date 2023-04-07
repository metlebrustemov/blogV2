from blogcore.models import Setting


def settings(request):
    return {'setting': Setting.objects.last()}