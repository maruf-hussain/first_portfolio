from django.shortcuts import render

# Home Page......................
def home(request):
    return render(request,'home.html')

#About Page.........................
def about(request):
    return render(request,'about.html')

#Projects Page........................
def projects(request):
    return render(request,'projects.html')

#Testimonial Page.....................
def testimonial(request):
    return render(request,'testimonial.html')

#Hire Page............................
def hire(request):
    return render(request,'hire.html')