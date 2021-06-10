from .models import Member, search
from django.forms import ModelForm

class GaurdianForm(ModelForm):
    class Meta:
        model = search
        fields =['name','house','image','phone','lat','lng']
    
class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields =['name','house','image','phone','retaled_to']
    