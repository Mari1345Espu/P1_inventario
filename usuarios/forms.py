from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Cliente, Repartidor, MiembroCuadrilla, Administrativo

from django import forms
from django.contrib.auth.models import User

class UsuariosForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User  # Asegúrate de que Usuario es un modelo que hereda de User o usa directamente User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Encripta la contraseña
        if commit:
            user.save()
        return user



class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'tipo_usuario', 'foto_perfil')

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'tipo_usuario', 'foto_perfil')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('direccion', 'ciudad', 'estado', 'codigo_postal')

class RepartidorForm(forms.ModelForm):
    class Meta:
        model = Repartidor
        fields = ('disponibilidad', 'bodega')

class MiembroCuadrillaForm(forms.ModelForm):
    class Meta:
        model = MiembroCuadrilla
        fields = ('cuadrilla', 'rol')

class AdministrativoForm(forms.ModelForm):
    class Meta:
        model = Administrativo
        fields = ('departamento',)
