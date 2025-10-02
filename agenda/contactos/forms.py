from django import forms
from .models import Contacto

CODIGOS_TELEFONO = {
    'CL': '+569',
    'AR': '+549',
    'PE': '+519',
    'BR': '+559',
    'US': '+1',
    'MX': '+521',
    'CO': '+573',
    'ES': '+346',
}

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'pais', 'telefono', 'correo', 'direccion']
        error_messages = { #Con (error_messages) lo usamos para poder personalizar los mensajes de error que genera django automaticamente
            'correo': {
                'unique': "Este correo ya existe",
                'invalid': "Correo no es valido, debe contener un '@' y un '.' para que sea valido",
            }
        }
        widgets = {
            'pais': forms.Select(),
            'telefono': forms.TextInput(),
            
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono', '').replace(' ', '')
        pais = self.cleaned_data.get('pais', 'CL')
        # Solo dígitos y símbolo +
        if not telefono.startswith('+') or not telefono[1:].isdigit():
            raise forms.ValidationError('El teléfono debe comenzar con "+" y contener solo números.')
        # Validación según país
        codigo = CODIGOS_TELEFONO.get(pais)
        if codigo and not telefono.startswith(codigo):
            raise forms.ValidationError(f'El número para {self.fields["pais"].label} debe comenzar con {codigo}.')
        # Validar longitud mínima (ajusta si lo necesitas por país)
        if len(telefono) < len(codigo) + 7:
            raise forms.ValidationError('El número parece demasiado corto para el país seleccionado.')
        return telefono