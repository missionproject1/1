from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm, SignUpForm, RegisterForm, LoginForm, ArtistProfileForm
from .models import UserProfile, Artwork, ArtistProfile
from elasticsearch_dsl import Search

from django.contrib.auth.decorators import login_required

def artist_dashboard_development(request):
    # Replace 'is_artist' with your actual logic to identify artists
    if request.user.is_authenticated and request.user.profile.user_type == 'artist':
        return render(request, 'core/artist_dashboard.html')
    else:
        # Redirect or render a different page for non-artists
        return render(request, 'core/artist_dashboard.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        # Check the user's role from UserProfile
            if user.profile.profile_type == 'artist':  # Adjust this condition based on your UserProfile model
                return redirect('artist_dashboard')  # Replace 'artist_dashboard' with your named URL
            else:
                return redirect('frontpage') 
        else:
            messages.error(request, 'Invalid username or password')

    # If request.method != 'POST' or login failed, render the login form again
    # Replace 'your_login_template.html' with the path to your actual login template
    return render(request, 'core/login.html')

# @login_required
# @user_passes_test(lambda u: u.userprofile.user_type == 'artist')
def artist_dashboard(request):
    return render(request, 'core/artist_dashboard.html')

# @login_required
# def add_artwork(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             artwork = form.save(commit=False)
#             artwork.artist = request.user
#             artwork.save()
#             return redirect('artist_dashboard')
#     else:
#         form = RegisterForm()

#     return render(request, 'core/add_artwork.html', {'form': form})

from .forms import ArtworkForm

def add_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user.artistprofile  # Assuming the artist is associated with the currently logged-in user
            artwork.save()
            return redirect('artist_dashboard', pk=artwork.pk)  # Redirect to the artwork detail page or another appropriate page
    else:
        form = ArtworkForm()

    return render(request, 'core/add_artwork.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArtistProfileForm

#@login_required
def edit_profile(request):
    artist = request.user  # Assuming you have a one-to-one relationship between User and ArtistProfile
    user_profile = request.user 
    if request.method == 'POST':
        # form = ArtistProfileForm(request.POST, instance=artist)
        form = ArtistProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_dashboard')
    else:
        # form = ArtistProfileForm(instance=artist)
        form = ArtistProfileForm()

    return render(request, 'core/edit_profile.html', {'form': form})

def logout_view(request):
    request.session.clear()
    request.session['logout_flag'] = True
    return HttpResponseRedirect(reverse('frontpage'))

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sensitive_view(request):
    return render(request, 'core/sensitive_template.html')

def is_artist(user):
    return user.groups.filter(name='Artists').exists()

def has_upload_permission(user):
    return user.userprofile.can_upload

# @login_required
# @user_passes_test(is_artist)
# @user_passes_test(has_upload_permission)
def has_artist_and_upload_permission(request):
    return render(request, 'core/your_template.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserProfileForm, CustomUserCreationForm

from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


# def register_view(request):
#     if request.method == 'POST':
#         user_form = UserCreationForm(request.POST)
#         profile_form = UserProfileForm(request.POST)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()

#             # Log the user in after registration
#             login(request, user)

#             return redirect('frontpage')  # Redirect to the homepage or any other page

#     else:
#         user_form = UserCreationForm()
#         profile_form = UserProfileForm()

#     return render(request, 'core/register.html', {'user_form': user_form, 'profile_form': profile_form})

# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             # Accessing form.cleaned_data directly
#             email = form.cleaned_data['email']
#             user_type = request.POST.get('user_type', 'artist')

#             # No need to create a separate UserProfile instance
#             UserProfile.objects.create(user=user, email=email, user_type=user_type)

#             request.session['user_type'] = user_type
#             login(request, user)
#             return redirect('artist_dashboard')
#     else:
#         form = RegisterForm()

#     return render(request, 'core/register.html', {'form': form})

# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             # Create UserProfile instance after saving the user
#             UserProfile.objects.create(user=user, email=form.cleaned_data['email'], user_type=request.POST.get('user_type', 'member'))

#             # Optionally, log in the user
#             login(request, user)

#             return redirect('artist_dashboard')

#     else:
#         form = RegisterForm()

#     return render(request, 'core/register.html', {'form': form})

def search_view(request):
    query = request.GET.get('q', '')
    search = Search(index='yourmodel_index').query('multi_match', query=query, fields=['title', 'description'])
    results = search.execute()

    return render(request, 'search_results.html', {'results': results})

def frontpage(request):
    return render(request, 'core/frontpage.html')

def base(request):
    return render(request, 'base.html')

def artworks(request):
    return render(request, 'core/artworks.html')

def cart(request):
    return render(request, 'core/cart.html')

def auction(request):
    return render(request, 'core/auction.html')

def frontpage(request):
    return render(request, 'core/frontpage.html')

# Additional views can be added below
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the User object
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']  # Assign the email to the User object
            user.save()
            # Create a UserProfile object if it doesn't exist
            UserProfile.objects.get_or_create(user=user, defaults={
                'date_of_birth': form.cleaned_data.get('date_of_birth'),
                'profile_type': form.cleaned_data.get('profile_type'),
                # Don't assign email here since it's already in the User object
            })
            # Additional code to log the user in or redirect as needed
            return redirect('artist_dashboard')
    else:
        form = SignUpForm()

    return render(request, 'core/register.html', {'form': form})


