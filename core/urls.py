from django.urls import path
from .views import home, NuevaCategoria, NuevoProducto, NuevoProducto2, Indice, inventario, Productos, NuevaEntrada, NuevaEntrada2
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
]

core_patterns = ([
    path('nuevacategoria', NuevaCategoria.as_view(), name = 'nuevacategoria'),
    path('nuevoproducto', NuevoProducto.as_view(), name = 'nuevoproducto'),
    path('nuevoproducto2', NuevoProducto2.as_view(), name = 'nuevoproducto2'),
    path('indice/<int:categoria>', Indice, name = 'indice'),
    path('productos/<int:categoria>', Productos, name = 'productos'),
    path('inventario/<int:categoria>', inventario, name = 'inventario'),
    path('nuevaentrada/<int:pk>', NuevaEntrada, name = 'nuevaentrada'),
    path('nuevaentrada2/<int:pk>', NuevaEntrada2, name = 'nuevaentrada2'),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT), 'core')