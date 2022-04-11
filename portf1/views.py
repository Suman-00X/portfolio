from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def skills(request):
    return render(request, 'skills.html')

def resume(request):
    return render(request, 'resume.html')

def work(request):
    return render(request, 'work.html')

def education(request):
    return render(request, 'education.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'name': form.cleaned_data['name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "index.html", {'form':form})