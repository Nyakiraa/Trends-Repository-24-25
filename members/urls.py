from django.urls import include, path
from django.conf import settings
from . import views
from members.views import GoogleLoginRedirectView
from django.views.generic.base import RedirectView


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('google-login/', RedirectView.as_view(url='/accounts/google/login/?process=login&prompt=select_account'), name='google_login'),
    path('myfirst/', views.myfirst_view, name='myfirst'),
    path('login/', views.login_view, name='login'),
    path('policy/', views.policy_view, name='policy'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('account/', views.account_view, name='account'),
    path('bank/', views.bank_view, name='bank'),
    path('ewallet/', views.ewallet_view, name='ewallet'),
    path('assessment/', views.assessment_view, name='assessment'),
    path('matriculation/', views.matriculation_view, name='matriculation'),
    path('payment/', views.payment_view, name='payment'),
    path('bank_payment/', views.bank_payment_view, name='bank_payment'),
    path('ewallet_payment/',views.ewallet_payment_view, name='ewallet_payment'),
    path('track_payment/', views.track_payment_view, name='track_payment'),
    path('report/',views.report_view, name='report'),
    path('about_us/',views.about_us_view, name='about_us'),
]
