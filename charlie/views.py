from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignUpForm, SignUpInfoForm
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template

def sign_up(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)

		if form.is_valid:
			form.save(commit=True)

			# send emails
			email = form.cleaned_data["email"]
			message = "emails/welcome.html"
			email_content = get_template('emails/welcome.html').render()
			msg = EmailMessage("Welcome", email_content, "yongyu@keyinsite.com", [email])
			msg.content_subtype = "html"
			msg.send()
			return HttpResponseRedirect('sign-up')
		else:
			print form.errors
	else:
		form = SignUpForm()

	return render(request, 'charlie/landing.html', {'form':form})

def sign_up_info(request):
	if request.method == "POST":
		form = SignUpInfoForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/thank-you')
		else:
			print form.errors
	else:
		form = SignUpInfoForm()

	return render(request, 'charlie/signup_info.html', {'form':form})