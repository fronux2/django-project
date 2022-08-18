import imp
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError
from datetime import datetime
from django.contrib.admin.widgets import AdminDateWidget

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tip_consulta", "mensaje", "avisos"]
        fields = '__all__'
class DateInput(forms.DateInput):
    input_type = 'date'

class ProductoForm(forms.ModelForm):
    fecha_fabricacion = forms.DateField(widget=DateInput)
    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=1)])
    precio = forms.IntegerField(min_value=1, max_value=1500000)
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe =  Producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombre
        
    class Meta:        
        model = Producto
        fields = '__all__'
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    pass
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]