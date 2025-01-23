from django.shortcuts import render,get_object_or_404
from . import models
from django.views.generic import DetailView
from . import forms
from django.shortcuts import redirect
from brand.models import Brand

# Create your views here.
# def home(request,brand_slug = None):
#     carData = models.Car.objects.all()
#     if brand_slug:
#         # carData = carData.filter(brand__slug = brand_slug)
#         # brand = Brand.objects.get(slug = brand_slug)
#         brand = Brand.objects.get(slug=brand_slug)
#         car = car.objects.filter(brand=brand)
#     branda = models.Brand.objects.all()
#     return render(request, 'home.html',{'data': carData,'brand' : branda})
def home(request, brand_slug=None):
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        carData = models.Car.objects.filter(brand=brand)
    else:
        carData = models.Car.objects.all()

    branda = Brand.objects.all()
    return render(request, 'home.html', {'data': carData, 'brand': branda})



class DetailsView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'viewDetails.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=request.POST)
        car = self.get_object()  
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return redirect('viewDetails', id=car.id)  
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object  
        context['comments'] = car.comments.all()
        context['commentForm'] = forms.CommentForm()  
        return context
