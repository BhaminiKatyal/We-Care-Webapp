from django.shortcuts import render, redirect
from .models import Questions
from .models import Responses, Prescription
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login/')

def movies(request):
    return render(request, 'file.html')

def quiz(request):
    quesList = Questions.objects.all()
    if (request.method=="POST"):
        q1 = int(request.POST.get('q1', 0))
        q2 = int(request.POST.get('q2', 0))
        q3 = int(request.POST.get('q3', 0))
        q4 = int(request.POST.get('q4', 0))
        q5 = int(request.POST.get('q5', 0))
        total_score = q1 + q2+ q3+q4+q5
        response = Responses(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
        response.save()
        if (total_score<12):
            showMessage = '''Based on your responses, it appears that you are currently at a low risk. That's great news! Remember, these results are not a diagnosis. To support your mental well-being, consider exploring our services. Engage in calming yoga sessions to promote relaxation.
             Discover uplifting and inspiring movies for a positive break, Connect with our chatbot for a friendly conversation or additional support.
'''
            messages.info(request, showMessage)
            return render(request, 'index.html')
        elif (total_score<18):
            showMessage = '''Your quiz results indicate a moderate level of concern, and it's perfectly okay to acknowledge life's challenges. To feel better you can listen to calming music or do yoga from the website
'''
            messages.info(request, showMessage)
            return render(request, 'index.html')
        else:
            showMessage = ''' Your responses indicate an elevated level of concern but you're not alone. It takes courage to recognize the need for support, and we're here to accompany you on this journey towards well-being. Reach out for support and book a call with a doctor through our website. '''
            messages.info(request, showMessage)
            return render(request, 'index.html')
    
    return render(request, 'quiz.html', {'questions': quesList})

def music(request):
    return render(request, 'music2.html')

def yoga(request):
    return render(request, 'yoga.html')

def doctors(request):
    return render(request, 'doctor.html')

def medicines(request):
    if (request.method=="POST"):
        address = request.POST.get('file')
        pres = request.POST.get('file')
        prescription = Prescription(address=address, file=pres)
        
        if not pres:
            messages.warning(request,"Please upload doctor's prescription")
        else:
            prescription.save()
            messages.success(request,"We will be validating the prescription and delivering the medicines soon")

    return render(request, 'medicines.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})

    return render(request, 'register.html')

def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'index.html', {'name': request.user.first_name})
    return render(request, 'login.html')
    
@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

def logout_view(request):
    logout(request)
    return redirect("/login")

