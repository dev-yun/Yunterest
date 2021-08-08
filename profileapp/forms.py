from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'messsage']
#   ModelForm을 통해 model의 내용을 form 형식으로 만듬
