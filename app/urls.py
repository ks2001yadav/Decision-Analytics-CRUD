from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswwordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.home ,name = "home"),
    path('listmeet/',views.listmeet,name='list'),
    path('addmeet/',views.AddMeetingView.as_view(),name='addmeeting'),
    path('update/<int:id>/', views.update,name='update'),
    path('listmeet/edit/<int:id>/', views.edit,name='edit'),
    path('listmeet/delete/<int:id>/', views.delete,name='delete'),
    # path('login/',views.login,name="login"),
    # path('otp/',views.otp,name="otp"),
    path('mobile/',views.mobile,name="mobile"),
    path('register/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswwordResetForm),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]