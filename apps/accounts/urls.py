from django.urls import path
from .views import RegisterView, UpdatePasswordView, HomeUserView


app_name = 'users'


urlpatterns = [
    path('', HomeUserView.as_view(), name='user_home'),
    #path('perfil/update-user/', UpdateUserView.as_view(), name='update_user'),
    path('alterar-senha/', UpdatePasswordView.as_view(), name='update_password'),
    path('registro/', RegisterView.as_view(), name='register'),

]