import json
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import Museum, Topic, Comment
from .forms import RoomForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
rooms = []



def loginPage(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    ch1='0'
    AV1=0
    ch2='0'
    AV2=0
    ch3='0'
    AV3=0
    ch4='0'
    AV4=0
    ch5='0'
    AV5=0
    ch6='0'
    AV6=0
    ch7='0'
    AV7=0
    ch8='0'
    AV8=0
    ch9='0'
    AV9=0
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Museum.objects.filter(
        Q(name__icontains=q) | Q(location__icontains=q))
    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = Comment.objects.filter(
        Q(room__topic__name__icontains=q))[0:3]
    
    ch1,AV1,message_count1=bardo1(request)
    ch2,AV2,message_count2=eljam1(request)
    ch3,AV3,message_count3=carthage1(request)
    ch4,AV4,message_count4=paleo1(request)
    ch5,AV5,message_count5=city1(request)
    ch6,AV6,message_count6=postal1(request)
    ch7,AV7,message_count7=douz1(request)
    ch9,AV9,message_count9=atp1(request)
    my_dict = {'AV5': AV5, 'AV6': AV6, 'AV6': AV6,'AV6': AV7, 'AV8': AV8,'AV1': AV1, 'AV2': AV2, 'AV3': AV3, 'AV4': AV4, 'AV9': AV9}
    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:6]}
    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count, 'room_messages': room_messages,'ch1':ch1,'ch2':ch2,'ch3':ch3,'ch4':ch4,'AV1':AV1,'message_count1':message_count1,
               'AV2':AV2,'message_count2':message_count2,'AV3':AV3,'message_count3':message_count3,'AV4':AV4,'message_count4':message_count4,
               'D':sorted_dict,'AV5':AV5,'message_count5':message_count5,'AV6':AV6,
               'message_count6':message_count6,'AV7':AV7,'message_count7':message_count7,'AV8':AV8,
               'AV9':AV9,'message_count9':message_count9}
    
    
    return render(request, 'base/home.html', context)


def list(request):
    ch1='0'
    AV1=0
    ch2='0'
    AV2=0
    ch3='0'
    AV3=0
    ch4='0'
    AV4=0
    ch5='0'
    AV5=0
    ch6='0'
    AV6=0
    ch7='0'
    AV7=0
    ch8='0'
    AV8=0
    ch9='0'
    AV9=0
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Museum.objects.filter(
        Q(name__icontains=q) | Q(location__icontains=q))
    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = Comment.objects.filter(
        Q(room__topic__name__icontains=q))[0:3]
    
    ch1,AV1,message_count1=bardo1(request)
    ch2,AV2,message_count2=eljam1(request)
    ch3,AV3,message_count3=carthage1(request)
    ch4,AV4,message_count4=paleo1(request)
    ch5,AV5,message_count5=city1(request)
    ch6,AV6,message_count6=postal1(request)
    ch7,AV7,message_count7=douz1(request)
    ch9,AV9,message_count9=atp1(request)
    my_dict = {'AV5': AV5, 'AV6': AV6, 'AV6': AV6,'AV6': AV7, 'AV8': AV8,'AV1': AV1, 'AV2': AV2, 'AV3': AV3, 'AV4': AV4, 'AV9': AV9}
    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:6]}
    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count, 'room_messages': room_messages,'ch1':ch1,'ch2':ch2,'ch3':ch3,'ch4':ch4,'AV1':AV1,'message_count1':message_count1,
               'AV2':AV2,'message_count2':message_count2,'AV3':AV3,'message_count3':message_count3,'AV4':AV4,'message_count4':message_count4,
               'D':sorted_dict,'AV5':AV5,'message_count5':message_count5,'AV6':AV6,
               'message_count6':message_count6,'AV7':AV7,'message_count7':message_count7,'AV8':AV8,
               'AV9':AV9,'message_count9':message_count9}
    
    
    return render(request, 'base/list_museums.html', context)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def museums(request):
    return render(request, 'base/museums.html')


def bardo(request):
    room =Museum.objects.get(Q(name__icontains='bardo'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='bardo'))
    participants = room.participants.all()
        
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'message_count':message_count,'AV':AV,'ch':ch}

    return render(request, 'base/bardo1.html', context)

def eljam(request):
    
    room = Museum.objects.get(Q(name__icontains='jem'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='el jem'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV1=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    if message_count != 0:
        AV1+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch1="%.1f/5" % (AV1)
    

    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'AV1':AV1,'ch1':ch1}

    return render(request, 'base/eljam.html', context)

def carthage(request):
    
    room = Museum.objects.get(Q(name__icontains='carthage'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='carthage'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'AV':AV,'ch':ch}

    return render(request, 'base/carthage.html', context)

def paleo(request):
    
    room = Museum.objects.get(Q(name__icontains='Paleo-Christian Museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='Paleo-Christian Museum'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'AV':AV,'ch':ch}

    return render(request, 'base/paleo.html', context)
def gallela(request):
    
    room = Museum.objects.get(Q(name__icontains='guallela museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='guallela museum'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'AV':AV,'ch':ch}

    return render(request, 'base/gallela.html', context)

def atp(request):
    room = Museum.objects.get(Q(name__icontains='ATP Tunis (Dar Ben Abdallah)'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='ATP Tunis (Dar Ben Abdallah)'))
    participants = room.participants.all()
        
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message =Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'message_count':message_count,'AV':AV,'ch':ch}

    return render(request, 'base/atp.html', context)
def douz(request):
    room = Museum.objects.get(Q(name__icontains='Douz_museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='Douz_museum'))
    participants = room.participants.all()
        
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'message_count':message_count,'AV':AV,'ch':ch}

    return render(request, 'base/douz.html', context)
def city(request):
    
    room = Museum.objects.get(Q(name__icontains='City of Sciences'))
    room_messages =Comment.objects.filter(Q(room__name__icontains='City of Sciences'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'AV':AV,'ch':ch}

    return render(request, 'base/city.html', context)

def postal(request):
    
    room = Museum.objects.get(Q(name__icontains='Postal Museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='Postal Museum'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    
    context = {'room': room, 'room_messages': room_messages,
               'participants': participants,'AV':AV,'ch':ch}

    return render(request, 'base/postal.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    room = Museum.objects.get(id=1)
    context = {'room': room}
    return render(request, 'base/room.html', context)



def room_forum(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            image = Museum(image=request.FILES['image'])

            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    return render(request, 'base/room_forum.html', {'form': form})


def detail_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Museum.objects.get(id=pk)

    return render(request, "base/detail_view.html", context)


def update_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Museum, id=pk)

    # pass the object as instance in form
    form = RoomForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('index')            

    # add form dictionary to context
    context["form"] = form

    return render(request, "base/update_view.html", context)


def delete_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Museum, id=pk)

    if request.method == "POST":
        # delete object
        obj.delete()

        return redirect('index')

        # after deleting redirect to
        # home page

    return render(request, "base/delete_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Museum.objects.all()

    return render(request, "base/list_view.html", context)


def index(request):
    data = {
        "museums": Museum.objects.all()
    }
    return render(request, 'base/index.html', data)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Museum.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here !!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_forum.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):

    room = Museum.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here !!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='login')
def deleteMessage(request, pk):

    message = Comment.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here !!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': message})



def bardo1(request):
    room = Museum.objects.get(Q(name__icontains='bardo'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='bardo'))
    participants = room.participants.all()
        
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message =Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)

    return (ch,AV,message_count)


def eljam1(request):
    
    room = Museum.objects.get(Q(name__icontains='jem'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='el jem'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV1=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    if message_count != 0:
        AV1+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch1="%.1f/5" % (AV1)

    return (ch1,AV1,message_count)

def carthage1(request):
    
    room = Museum.objects.get(Q(name__icontains='carthage'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='carthage'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)

    return (ch,AV,message_count)

def paleo1(request):
    
    room = Museum.objects.get(Q(name__icontains='Paleo-Christian Museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='Paleo-Christian Museum'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    
    return(ch,AV,message_count)

def city1(request):
    
    room = Museum.objects.get(Q(name__icontains='City of Sciences'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='City of Sciences'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)

    return (ch,AV,message_count)


def postal1(request):
    
    room = Museum.objects.get(Q(name__icontains='Postal Museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='Postal Museum'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    
    return (ch,AV,message_count)

def douz1(request):
    room = Museum.objects.get(Q(name__icontains='Douz_museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='Douz_museum'))
    participants = room.participants.all()
        
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
    return (ch,AV,message_count)

def gallela1(request):
    
    room = Museum.objects.get(Q(name__icontains='guallela museum'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='guallela museum'))
    participants = room.participants.all()
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)
   

    return (ch,AV,message_count)

def atp1(request):
    room = Museum.objects.get(Q(name__icontains='ATP Tunis (Dar Ben Abdallah)'))
    room_messages = Comment.objects.filter(Q(room__name__icontains='ATP Tunis (Dar Ben Abdallah)'))
    participants = room.participants.all()
        
    a=0
    b=0
    c=0
    d=0
    e=0
    AV=0
    if request.method == 'POST':
        if request.POST.get("rating5"):
            r = "⭐ ⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating4"):
            r = "⭐ ⭐ ⭐ ⭐"
        elif request.POST.get("rating3"):
            r = "⭐ ⭐ ⭐"
        elif request.POST.get("rating2"):
            r = "⭐ ⭐"  
        elif request.POST.get("rating1"):
            r = "⭐"
        else:
            r = ""
        message = Comment.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            rate=r,
            image=request.POST.get('avatar')
        )
        room.participants.add(request.user)

    message_count = room_messages.count()
 
    for message in room_messages:
        if message.rate==" ⭐ ⭐ ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐ ⭐ ⭐" :
            a+=1
        elif message.rate==" ⭐ ⭐ ⭐ ⭐"or message.rate=="⭐ ⭐ ⭐ ⭐" :
            b+=1
        elif message.rate==" ⭐ ⭐ ⭐" or message.rate=="⭐ ⭐ ⭐" :
            c+=1
        elif message.rate==" ⭐ ⭐" or message.rate=="⭐ ⭐" :
            d+=1
        elif message.rate==" ⭐" or message.rate=="⭐" :
            e+=1
        else:
            a=a
            b=b
            c=c
            d=d
            e=e
  
    if message_count != 0:
        AV+=(5*a+4*b+3*c+2*d+1*e)/message_count
    ch="%.1f/5" % (AV)


    return (ch,AV,message_count)