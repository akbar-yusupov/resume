from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "portfolio/", views.PortfolioListView.as_view(), name="portfolio-list"
    ),
    path(
        "portfolio/<str:slug>",
        views.PortfolioDetailView.as_view(),
        name="portfolio-detail",
    ),
    path("contact/", views.ContactFormView.as_view(), name="contact"),
]
