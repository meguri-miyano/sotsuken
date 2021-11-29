from django.shortcuts import render
from django.http import HttpResponse
from .import forms
from django.views.generic import TemplateView
from .models import Menudata

# Create your views here.
def top_index(request):
	  return render(request,'toppage.html')

def list_index(request):
    context ={
      'menu_list':Menudata.objects.all(),
    }
    return render(request,'list.html',context)


class FormView(TemplateView):

	def __init__(self):
		self.params = {"form":forms.RegisterForm(),}
	
	def get(self,request):
		return render(request,"register.html",context=self.params)

	def post(self,request):
		if request.method == "POST":
			self.params["form"] = forms.RegisterForm(request.POST)

			if self.params["form"].is_valid():
				self.params["form"].save(commit=True)
				self.params["Message"] = "メニューが登録されました。"

		return render(request,"register.html",context=self.params)
