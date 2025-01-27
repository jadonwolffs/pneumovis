"""
The file that processes user actions and page routes for most basic pages
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Count

from swabs.models import Swab
from .dash_apps import *
from .files import *
from .tasks import *

from datetime import datetime

def index(request):
    messages.warning(request,'Please be aware that this page takes a while to load properly')
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def dashboard(request):
    return redirect('dashboard')


def dep(request):
    messages.error(request, 'Not yet implemented')
    return redirect('index') 
    return redirect('about') 
    


def login(request):
    if request.method == 'POST':
        # login logic
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('index')


def ip(request):
    return render(request, 'pages/index-proto.html')


def browse(request):
    num_swabs = len(Swab.objects.all())
    num_participants = len(Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(dcount=Count('Particcipant_ID')))
    num_strains = len(Swab.objects.order_by('Serotype_autocolour').values('Serotype_autocolour').annotate(dcount=Count('Serotype_autocolour')))
    context={
    'num_swabs':num_swabs,
    'num_participants':num_participants,
    'num_strains':num_strains,
    }
    return render(request, 'pages/browse.html',context)


def upload(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.user.id
            uploaded_file = request.FILES['file_upload']

            fs = FileSystemStorage()
            # TODO rename using date convention
            filename = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_url = fs.url(filename)
            print("POST request comes to: ",request.POST)
            delimiter = request.POST['delimiter']
            try:
                header_value=request.POST['header']
                header = True
            except:
                header = False
            # Spawn Subprocess
            # Check if user has made request recently and if so block it for a couple minutes to allow processes to finish
            import threading
            upload_thread = threading.Thread(target=process_csv, args=(uploaded_file_url,header, delimiter), kwargs={})
            upload_thread.setDaemon(True)
            upload_thread.start()
            # p=subprocess.Popen(['/bin/cp',f , '/home/dutzy/Desktop'])
            
            # result = process_csv(uploaded_file_url,header, delimiter)
            # result = [pool.apply(process_csv, args=(uploaded_file_url,header,delimiter))]
            # results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
            # messages.info(request, 'Successfully made ' +
            #               str(result['s'])+' new entries and failed to make '+str(result['f'])+' entries')
            # context = {'uploaded_file_url': uploaded_file_url}
            return render(request, 'pages/upload.html')
        else:
            messages.error(request, 'You have to be logged in to add swabs')
        return redirect('upload')

    else:
        return render(request, 'pages/upload.html')


def contact(request):
    return render(request, 'pages/contact.html')
