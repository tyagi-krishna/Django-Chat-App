from django.shortcuts import render, redirect
from chat.models import Room, Message, Users
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def signup(request):
    if request.method == 'POST':
        user = Users()
        user.firstname = request.POST['first_name']
        user.lastname = request.POST['last_name']
        companyname = request.POST['company_name']
        user.companyname = companyname
        user.password = request.POST['password']
        user.description = request.POST['description']
        user.email = request.POST['email']
        user.addressline1 = request.POST['addressline1']
        user.city = request.POST['city']
        user.state = request.POST['state']
        user.country = request.POST['country']
        user.save()
        room = request.POST['company_name']
        if Room.objects.filter(name=companyname).exists():
            return redirect('/'+room+'/?username='+companyname)
        else:
            new_room = Room.objects.create(name=companyname)
            new_room.save()
            return redirect('/'+room+'/?username='+companyname)
    
    else:
        return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        companyname = request.POST.get("company_name")
        password = request.POST.get("password")
        room = request.POST['company_name']
        try:
            users = Users.objects.get(companyname=room)
            user_password = users.password
            if user_password == password:
                return redirect('/'+room+'/?username='+companyname)
            else:
                return render(request, 'wrong_password.html')
            
        except:
            return render(request, 'create_account.html')
    
    else:
        return render(request, 'login.html')