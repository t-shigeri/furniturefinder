from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models import Q
from .models import RoomPhoto, Furniture
from .forms import FurnitureSearchForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from .models import Furniture
    
class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

@method_decorator(login_required, name='dispatch')
class GalleryView(ListView):
    template_name = 'gallery.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return RoomPhoto.objects.filter(user=self.request.user)

class ServicesView(TemplateView):
    template_name = 'services.html'

class ReferenceView(TemplateView):
    template_name = 'reference.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        
        subject = 'お問い合わせ: {}'.format(name)
        message = 'Name: {}\nEmail: {}\nMessage: {}'.format(name, email, message)
        from_email = 'fko2447037@stu.o-hara.ac.jp'
        to_list = ['fko2447037@stu.o-hara.ac.jp']

        email_message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
        email_message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました')
        return super().form_valid(form)

class SearchView(FormView):
    template_name = 'search.html'
    form_class = FurnitureSearchForm
    success_url = reverse_lazy('result')

    def form_valid(self, form):
        min_height = form.cleaned_data.get('min_height')
        max_height = form.cleaned_data.get('max_height')
        min_width = form.cleaned_data.get('min_width')
        max_width = form.cleaned_data.get('max_width')
        style = form.cleaned_data.get('style')

        query = Q()
        if min_height:
            query &= Q(height__gte=min_height)
        if max_height:
            query &= Q(height__lte=max_height)
        if min_width:
            query &= Q(width__gte=min_width)
        if max_width:
            query &= Q(width__lte=max_width)
        if style:
            query &= Q(style__icontains=style)

        results = Furniture.objects.filter(query)
        return self.render_to_response(self.get_context_data(form=form, results=results))

class ResultView(FormView):
    template_name = 'search_results.html'
    form_class = FurnitureSearchForm

    def form_valid(self, form):
        min_height = form.cleaned_data.get('min_height')
        max_height = form.cleaned_data.get('max_height')
        min_width = form.cleaned_data.get('min_width')
        max_width = form.cleaned_data.get('max_width')
        style = form.cleaned_data.get('style')

        query = Q()
        if min_height:
            query &= Q(height__gte=min_height)
        if max_height:
            query &= Q(height__lte=max_height)
        if min_width:
            query &= Q(width__gte=min_width)
        if max_width:
            query &= Q(width__lte=max_width)
        if style:
            query &= Q(style__icontains=style)

        results = Furniture.objects.filter(query)
        return self.render_to_response(self.get_context_data(form=form, results=results))

class SuccessView(TemplateView):
    template_name = 'success.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'アカウントが作成されました。ログインしてください。')
        return super().form_valid(form)
    


def furniture_detail(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    return render(request, 'furniture_detail.html', {'furniture': furniture})
