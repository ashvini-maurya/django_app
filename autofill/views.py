from django.shortcuts import render
from django.http import HttpResponse

from autofill.forms import UserForm

def index(request):
  context_dict = {'boldmessage': "I am bold font from the context"}
  return render(request, 'autofill/index.html', context_dict)

  # return HttpResponse("Hello World")



def add_address(request):
  if request.method == 'POST':
    form = UserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print form.errors
  else:
    form = UserForm()
  
  return render(request, 'autofill/add_address.html', {'form': form})

  