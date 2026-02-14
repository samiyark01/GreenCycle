from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PickupRequestForm  
from .models import PickupRequest,UserProfile
@login_required
def create_pickup_request(request):
    if request.method == 'POST':
        form = PickupRequestForm(request.POST)
        if form.is_valid():
            pickup = form.save(commit = False)
            pickup.user = request.user 
            pickup.save()
            return redirect('dashboard')
    else:
        form = PickupRequestForm()
    return render(request,'create_pickup.html',{'form':form})
@login_required
def dashboard(request):
    pickups = PickupRequest.objects.filter(user=request.user).order_by('-request_at')
    profile,created = UserProfile.objects.get_or_create(user=request.user)
    return render(request,'dashboard.html',{'pickups':pickups,'profile':profile})
