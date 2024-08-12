from django.db.models import Q
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from typography.models import Publication, PublicationComment, Feedback


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.filter(is_hidden=False)
        }
        return context


class HomeSearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        search_word = self.request.GET['query']
        context = {
            'publication_list': Publication.objects.filter(is_hidden=False).filter(
                Q(title__icontains=search_word) | Q(description__icontains=search_word)
            )
        }
        return context


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=publication_pk),
        }
        return context


class CreatePublicationCommentView(View):

    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)
        user_name = request.POST['name']
        text = request.POST['message']

        PublicationComment.objects.create(publication=publication, user_name=user_name, text=text)

        return redirect('publication-detail-url', pk=publication_pk)


class ContactView(TemplateView):
    template_name = 'contact.html'


class CreateFeedbackView(View):

    def post(self, request, *args, **kwargs):
        user_name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['message']

        Feedback.objects.create(user_name=user_name, email=email, subject=subject, text=text)

        return redirect('contact-url')
