"""
URL configuration for super_info_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from typography.views import (HomeView, HomeSearchView,
                              PublicationDetailView, CreatePublicationCommentView,
                              ContactView, CreateFeedbackView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-url'),
    path('home/search/', HomeSearchView.as_view(), name='home-search-url'),
    path('publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail-url'),
    path('publication-detail/<int:pk>/create-comment/', CreatePublicationCommentView.as_view()),
    path('contact/', ContactView.as_view(), name='contact-url'),
    path('contact/create-feedback/', CreateFeedbackView.as_view(), name='contact-create-feedback-url'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
