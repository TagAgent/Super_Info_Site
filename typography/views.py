from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from typography.models import Publication, PublicationComment


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all()
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
