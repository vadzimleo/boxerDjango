from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def about(request):
    if request.method == "POST":
        
        name = request.POST['name']
        phone_number = request.POST['phone-number'] 
        email = request.POST['email'] 
        message = request.POST['message'] 
        send_mail(
            name,
            message,
            email,
            ['vadzimleo@gmail.com', 'S_vdm@mail.ru']
           
            
        )
        return render(request, 'about.html', {
        'name' : name,
        'phone_number' : phone_number,
        'email': email,
        'message': message
        })
    else:
        return render(request, 'about.html', {})
    
def classes(request):
    return render(request, 'class.html', {})

def blog(request):
    return render(request, 'blog.html', {})


def appointment(request):
    if request.method == "POST":
        your_schedule = request.POST['your-schedule'] 
        your_date = request.POST['your-date']  
        name = request.POST['name']
        phone_number = request.POST['phone-number'] 
        email = request.POST['email'] 
        message = request.POST['message'] 
        appointment = "your schedule:" + your_schedule + "your date:" + your_date + "name:" + name + "phone number:" + phone_number + "email:" + email + "message:" + message 
        # send_mail(
        #     'appointment request',
        #     appointment, 
        #     email,
        #     ['vadzimleo@gmail.com', 'S_vdm@mail.ru']                 
        # )

        return render(request, 'appointment.html', {
            'your_schedule': your_schedule,
            'your_date': your_date,
            'name' : name,
        'phone_number' : phone_number,
        'email': email,
        'message': message
        
        })
    else:
        return render(request, 'home.html', {})
