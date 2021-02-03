# We import path from django to power our urlpattern below
from django.urls import path
# We import views, using .views tell django to look within the current directory for a views.py file
from .views import homePageView

# If a user requests the homepage represented by the empty string "", django should use the view called homePageView
urlpatterns = [
    path("", homePageView, name="home")
]