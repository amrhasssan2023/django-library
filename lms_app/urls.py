from django.urls import path, include
from . import views
from . import api
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('books',api.viesets)
router.register('cat',api.viewsets_cat)




urlpatterns = [
    path('',views.index, name='index'),

    path('api-auth', include('rest_framework.urls')),

    path('books/',views.books, name='books'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),

    #___________________________________________________
    path('model_no_rest', api.model_no_rest),
    path('rest', api.FBV_list),
    path('rest/<int:id>', api.FBV_id),\
    path('rest_CBV/', api.CBV_list.as_view()),
    path('rest_CBV/<int:id>', api.CBV_id.as_view()),
    
    path('rest_mixins_list/', api.mixins_list.as_view()),
    path('rest_mixins_list/<int:id>', api.mixins_id.as_view()),


    
    path('rest_generic_list/', api.generic_list.as_view()),
    path('rest/generic_id/<int:id>', api.generic_id.as_view()),

    path('rest/viewsets', include(router.urls)),

    path('api-authtoken', obtain_auth_token)
]