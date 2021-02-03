"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
# Import include so we can include our pages app
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This works by when a user visits the homepage, they will first be routed to the 'pages' app, and then to the homePageView view set in the pages/urls.py file
    # Think of this url as the gateway to the various url patterns in each distinct app.
    path("", include("pages.urls")),
]
