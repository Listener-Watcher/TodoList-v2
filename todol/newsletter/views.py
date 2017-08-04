from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from django.core.mail import send_mail
from .models import SignUp
# Create your views here.
def home(request):
    title = "Login to use it!"
    if request.user.is_authenticated():
        title = "Welcome %s" %(request.user)
    if request.method == "POST":
        print request.POST
    form = SignUpForm(request.POST or None)

    context = {
    "template_title": title,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
            "title": "Thank you"
        }

    if request.user.is_authenticated() and request.user.is_staff:
        # print SignUp.objects.all()
        # count = 1
        # for instance in SignUp.objects.all():
        #     print count ,
        #     print instance
        #     count += 1
        queryset = SignUp.objects.all().order_by('-timestamp')
        # queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name_icontains="Justin")
        # queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name_iexact="Justin")
        # .filter().count()
        context = {
            "queryset": queryset,
        }

    return render(request, "home.html", context)

def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "forms.html", context)

def profile(request):
    if request.user.is_authenticated():
        title = "Welcome %s" %(request.user)
        context = {
            "title": title
        }
        return render(request, "profile.html", context)
    else:
        context = {}
        return render(request, "home.html", context)
