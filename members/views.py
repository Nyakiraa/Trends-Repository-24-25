from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.views import View
from django.views.decorators.http import require_http_methods
from .models import Member


def about_us_view(request):
    team_members = Member.objects.all()[:4]  # Get first 4 team members
    context={"team_members": team_members}
    return render(request, 'about_us.html',context)

@require_http_methods(["GET"])
def google_login(request):
    """
    Direct redirect to Google OAuth without intermediate page
    """
    # Construct the redirect URL to Google's OAuth
    redirect_uri = request.build_absolute_uri(reverse('google_callback'))
    
    # Google OAuth endpoint
    auth_url = f"https://accounts.google.com/o/oauth2/auth?client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={redirect_uri}&response_type=code&scope=email%20profile&prompt=select_account"
    
    return redirect(auth_url)

def google_callback(request):
    """
    Handle the callback from Google OAuth
    """
    # Process the OAuth callback and authenticate the user
    # This is a simplified version - you'll need to implement the full OAuth flow
    code = request.GET.get('code')
    
    if not code:
        # Handle error case
        return redirect('login')
    
    # Exchange code for token and authenticate user
    # ...
    
    # After successful authentication, redirect to dashboard or home
    return redirect('policy')

class GoogleLoginRedirectView(View):
    def get(self, request):
        # Redirect to the Google OAuth provider login URL
        return redirect(reverse('google_login'))

def myfirst_view(request):
    return render(request, 'myfirst.html')

def login_view(request):
    return render(request, 'login.html')

def policy_view(request):
    return render(request, 'policy.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def account_view(request):
    return render(request, 'account.html')

def bank_view(request):
    return render(request, 'bank.html')

def ewallet_view(request):
    return render(request, 'ewallet.html')

def assessment_view(request):
    return render(request, 'assessment.html')

def matriculation_view(request):
    return render(request, 'matriculation.html')

def payment_view(request):
    return render(request, 'payment.html')

def bank_payment_view(request):
    return render(request, 'bank_payment.html')

def ewallet_payment_view(request):
    return render(request, 'ewallet_payment.html')

def track_payment_view(request):
    return render(request, 'track_payment.html')

def report_view(request):
    return render(request, 'report.html')




