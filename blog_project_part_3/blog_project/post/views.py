from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# Create your views here.

# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         add_post = forms.PostForms(request.POST)
#         if add_post.is_valid():
#             # add_post.cleaned_data['author'] = request.user
#             add_post.instance.author = request.user
#             add_post.save()
#             return redirect('homepage')
#     else:
#         add_post = forms.PostForms()
#     return render(request,'add_post.html',{'form' : add_post})

#class based add post
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForms
    template_name = 'add_post.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# @login_required
# def edit_post(request,id):
#     post = models.Post.objects.get(pk = id)
#     post_forms = forms.PostForms(instance=post)
#     if request.method == 'POST':
#         post_forms = forms.PostForms(request.POST,instance=post)
#         if post_forms.is_valid():
#             post_forms.instance.author = request.user
#             post_forms.save()
#             return redirect('homepage')
#     return render(request,'add_post.html',{'form' : post_forms})
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForms
    template_name = 'add_post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

# @login_required
# def delete_post(request,id):
#     post = models.Post.objects.get(pk = id)
#     post.delete()
#     return redirect('homepage')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

class PostDetailsView(DetailView):
    model = models.Post
    template_name = 'Post_details_view.html'
    pk_url_kwarg = 'id'
    def post(self,request,*args, **kwargs):
        commentForm = forms.commentForm(data=self.request.POST)
        post = self.get_object()
        if commentForm.is_valid():
            new_comment = commentForm.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object #post model er object ai kane store korlam
        # comments = models.Comment.objects.filter(post=post)
        comments = post.comments.all()
        commentForm = forms.commentForm()
        context['comments'] = comments
        context['commentForm'] = commentForm
        return context
    