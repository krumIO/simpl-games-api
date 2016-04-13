from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import RoundForm
from ..models import Round


class RoundCreateView(SuccessMessageMixin, CreateView):
    model = Round
    form_class = RoundForm
    template_name = 'simpl/rounds/round_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:round_detail', args=(self.object.pk,))


class RoundDeleteView(DeleteView):
    model = Round
    template_name = 'simpl/rounds/round_delete.html'
    context_object_name = 'round'
    success_message = 'Round was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:round_list')


class RoundDetailView(DetailView):
    model = Round
    template_name = 'simpl/rounds/round_detail.html'
    context_object_name = 'round'


class RoundListView(ListView):
    model = Round
    template_name = 'simpl/rounds/round_list.html'
    paginate_by = 20
    context_object_name = 'round_list'
    allow_empty = True


class RoundUpdateView(UpdateView):
    model = Round
    form_class = RoundForm
    template_name = 'simpl/rounds/round_update.html'
    context_object_name = 'round'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:round_detail', args=(self.object.pk,))
