from django import forms
from core.models import Categoria, Producto, Movimiento
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NuevaCategoriaForm(forms.ModelForm):
    
    class Meta: 
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
            'nombre':''
        }

class CategoriaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Categoria):
        return Categoria.nombre

class NuevoProductoForm(forms.ModelForm):
    categoria =  CategoriaModelChoiceField(queryset = Categoria.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    unidadPaquete = forms.IntegerField(required = True, widget = forms.NumberInput(attrs={'class':'form-control'}), label="Unidades por paquete")
    
    class Meta: 
        model = Producto
        fields = ['nombre','categoria', 'unidadPaquete', 'paquetes']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'paquetes': forms.HiddenInput(),
            'empaquetado': forms.HiddenInput(),
        }
        labels = {
             'nombre':'Nombre', 'unidadPaquete':'Unidades por paquete', 'categoria':'Categoria'
        }
        
class NuevoProductoForm2(forms.ModelForm):
    categoria =  CategoriaModelChoiceField(queryset = Categoria.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    
    class Meta: 
        model = Producto
        fields = ['nombre','categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
             'nombre':'Nombre', 'categoria':'Categoria'
        }
        
        
class NuevaEntradaForm(forms.ModelForm):
    
    class Meta: 
        opciones = [(False, "Paquete"), (True, "Unidad")]
        model = Movimiento
        fields = ['medida','cantidad', 'producto']
        widgets = {
            'medida': forms.Select(choices = opciones, attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'0'}),
            'producto':forms.HiddenInput(),
        }
        labels = {
             'medida':'Seleccione la medida', 'cantidad':'Cantidad'
        }
        
class NuevaEntradaForm2(forms.ModelForm):
    
    class Meta: 
        model = Movimiento
        fields = ['cantidad', 'producto']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'0'}),
            'producto':forms.HiddenInput(),
        }
        labels = {
            'cantidad':'Cantidad'
        }