from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blogcore.models import AdLucemUser



class AdLucemUserCreationForm(UserCreationForm):

    class Meta:
        model = AdLucemUser
        fields = ("email",)


class AdLucemUserChangeForm(UserChangeForm):

    class Meta:
        model = AdLucemUser
        fields = ("email",)
