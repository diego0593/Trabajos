from django.urls import path
from Facebook.views import FacebookList, FacebookDetalle,FacebookCliks,FacebookViewable,FacebookList_clicks,FacebookList_viewable
from Facebook import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('FB/publicidad/', FacebookList.as_view(),name='Lista_Publicidad' ),
    path('FB/publicidad/<int:pk>', FacebookDetalle.as_view(),name='Detalle_publicidad' ),
    path('FB/Clicks/', FacebookCliks.as_view(),name='Lista_Clicks' ),
    path('FB/Viewability/', FacebookViewable.as_view(),name='Lista_Visibilidad' ),
    path('FB/publicidad/<int:pk>/Clicks/', FacebookList_clicks.as_view(),name='list_Clicks_anuncio' ),
    path('FB/publicidad/<int:pk>/Viewability/', FacebookList_viewable.as_view(),name='list_visible_anuncio' ),
    path('FB/lista_publicidad/', views.list_facebook ,name='list' ),
]
