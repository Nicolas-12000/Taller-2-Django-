from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Solicitud
from .forms import SolicitudForm


class SolicitudListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/solicitud_list.html'
    context_object_name = 'solicitudes'
    paginate_by = 20


class SolicitudDetailView(DetailView):
    model = Solicitud
    template_name = 'solicitudes/solicitud_detail.html'
    context_object_name = 'solicitud'


class SolicitudUpdateView(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'solicitudes/solicitud_form.html'
    success_url = reverse_lazy('solicitudes:solicitud_list')


class SolicitudDeleteView(DeleteView):
    model = Solicitud
    template_name = 'solicitudes/solicitud_confirm_delete.html'
    success_url = reverse_lazy('solicitudes:solicitud_list')

class SolicitudCreateView(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'solicitudes/solicitud_form.html'
    success_url = reverse_lazy('solicitudes:confirmacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Formulario de Solicitud'
        context['descripcion'] = 'Complete el siguiente formulario para enviar su solicitud'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'Solicitud enviada exitosamente. Número de referencia: SOL-{self.object.id:06d}'
        )
        return response
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija los errores e el formulario.'
        )
        return super().form_invalid(form)

class SolicitudConfirmacionView(TemplateView):
    template_name = 'solicitudes/confirmacion.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Solicitud Enviada'
        context['mensaje'] = 'Su solicitud ha sido enviada exitosamente'
        return context