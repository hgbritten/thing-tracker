from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)

from .models import Thing

# Create your views here.
class ThingListView(ListView):
    model = Thing
    template_name = "things/thing_list.html"


class ThingDetailView(DetailView):
    model = Thing
    template_name = "things/thing_detail.html"


class ThingCreateView(CreateView):
    model = Thing
    template_name = "things/thing_create.html"
    fields = ["name", "reviewer", "rating"]


class ThingUpdateView(UpdateView):
    template_name = "things/thing_update.html"
    model = Thing
    fields = ["name", "reviewer", "rating"]


class ThingDeleteView(DeleteView):
    model = Thing
    template_name = "things/thing_delete.html"
    success_url = reverse_lazy("_list")
