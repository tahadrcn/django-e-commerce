
from django.urls import path
from . import views
from .views import ContactFormView

urlpatterns = [
    path("",views.homepage),
    path("homepage", views.homepage,name ="homepage"),
    path("kahveler",views.kahveler,name = "kahveler"),
    path("ekipmanlar",views.ekipmanlar,name ="ekipmanlar"),
    path("hikayemiz",views.hikayemiz,name ="hikayemiz"),
    path("toptankahve",views.toptankahve,name ="toptankahve"),
    path("blog",views.blog,name ="blog"),
    path("iletisim",ContactFormView.as_view(),name ="iletisim"),
    path("kahveler/<int:id>",views.product_details,name ="detay"),
]