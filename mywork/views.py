from django.shortcuts import render
from .models import Contact


#  Create your views here.
def index(request):

   if request.method == 'POST':
      user_name = request.POST.get('user_name')
      email= request.POST.get('email')
      subject= request.POST.get('subject')
      message= request.POST.get('message')

      b=Contact( user_name=user_name,email=email, subject=subject, message=message)
      b.save()
      return render(request, 'mywork/index.html')

   else:
      return render(request, 'mywork/index.html')

    