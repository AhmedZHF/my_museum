from django.forms import ModelForm
from .models import Museum,Comment


class RoomForm(ModelForm):
    class Meta:
        model= Museum
        fields= '__all__'


class MessageForm(ModelForm):
    class Meta:
        model= Comment
        fields= 'body','rate','image'




