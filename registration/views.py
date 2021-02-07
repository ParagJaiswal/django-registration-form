from django.shortcuts import render

def index(request):
	if request.method=='POST':
	   if request.POST.get('fsubmit'):
	   		n = request.POST['name']
	   		gen = request.POST['r1']
	   		add = request.POST['address']
	   		st = request.POST['state']
	   		ci = request.POST['city']
	   		em = request.POST['email']
	   		num = request.POST['number']
	   		return render(request,'registration/form.html',{"name":n,"gender":gen,"address":add,"state":st,"city":ci,"email":em,"number":num})
	   else:
	   		return render(request,'registration/form.html')
	return render(request,'registration/form.html')
