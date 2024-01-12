''' This code is defining the URL patterns for a Django web application. Each `path` function call
    specifies a URL pattern and associates it with a corresponding view function.
 '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_account', views.check_account, name='check_account'),
    path('create_account', views.create_account, name='create_account'),
    path('file_upload_and_save_asset', views.file_upload_and_save_asset, name='file_upload_and_save_asset'),
    path('set_asset_index', views.set_asset_index, name='set_asset_index'),
    path('get_all_requests', views.get_all_requests, name='get_all_requests'),
    path('get_all_assets', views.get_all_assets, name='get_all_assets'),
    path('set_asset_final_status', views.set_asset_final_status, name='set_asset_final_status'),
    path('create_trainee_request', views.create_trainee_request, name='create_trainee_request'),
    path('get_assets_trainee', views.get_assets_trainee, name='get_assets_trainee'),
]