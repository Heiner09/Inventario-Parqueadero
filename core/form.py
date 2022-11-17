from django import forms
from .models import Vehiculos,Propietarios, Ticket, Modelo

class FormVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = '__all__'

    def __init__(self, *args, **kwards):
        super(FormVehiculo, self).__init__(*args, **kwards)
        self.fields['modelo'].queryset = Modelo.objects.none()
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'input-form-vehiculo'
            else:
                field.widget.attrs['class'] = 'input-form-vehiculo'


        if 'marca' in self.data:
            try:
                marca_id = int(self.data.get('marca'))
                self.fields['modelo'].queryset = Modelo.objects.filter(marca_id=marca_id).order_by('descripcion')
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['modelo'].queryset = self.instance.marca.modelo_set.order_by('descripcion')

class FormPropietarios(forms.ModelForm):
    class Meta:
        model = Propietarios
        fields = '__all__'

    def __init__(self, *args, **kwards):
        super(FormPropietarios, self).__init__(*args, **kwards)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'input-form-vehiculo'
            else:
                field.widget.attrs['class'] = 'input-form-vehiculo'

class FormTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields= '__all__'
        exclude=('estado','hora_entrada','hora_salida','valor')
