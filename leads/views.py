from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead , Agent
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import LeadForm, LeadModelForm

class LandingPageView(TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, 'landing.html')

class LeadListView(ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "lead_list.html", context)

class LeadDetailView(DetailView):
    template_name = "lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'


def lead_detail(request ,pk): #pk
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "lead_detail.html", context)



def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "lead_update.html", context)

# def lead_update(request, pk):
#     lead = Lead.ogjects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name =form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name=first_name,
#             lead.last_name=last_name,
#             lead.age=age,
#             lead.save()
            
#             return redirect('/')
#     context = {
#         "lead": lead,
#         "form": form
#     }
    
#     return render(request, lead_update.html, context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/")

class LeadCreateView(CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm


    def get_success_url(self):
        return reverse('leads:lead_list')


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            # first_name =form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = form.cleaned_data['agent']
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent
            # )
            
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, "lead_create.html", context)
   