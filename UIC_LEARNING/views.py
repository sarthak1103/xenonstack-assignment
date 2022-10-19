from django.shortcuts import render
from E_LEARNING_PORTAL.urls import *
from django.http import JsonResponse
from UIC_LEARNING.models import enrolledstudents as enform


# Create your views here.
def About(request):
    return render(request, 'about.html')
def Efront(request):
    return render(request, 'Efront.html')
def htmlCourse(request):
    return render(request, 'htmlCourse.html')
def enrollForm(request):
    return render(request, 'enrollForm.html')
def enrollFormAPI(request):
    print(request.POST)
    fname=request.POST.get('fname')
    cno=request.POST.get('cno')
    course=request.POST.get('course')
    email=request.POST.get('email')
    pwd=request.POST.get('pwd')
    enform.objects.create(name=fname, contact_number=cno,course=course ,email=email ,password=pwd)

    return JsonResponse({"meta": {"status": 200}})
def pythonCourse(request):
    return render(request, 'pythonCourse.html')
def javaCourse(request):
    return render(request, 'javaCourse.html')
def LoginForm(request):
    return render(request, 'LoginForm.html')


def LoginFormAPI(request):
    print(request.POST)
    email=request.POST.get('email')
    pwd=request.POST.get('pwd')
    if enform.objects.filter(email__iexact=email).exists():
        password_query=enform.objects.filter(email__iexact=email).values('password')[0]['password']
        if password_query==pwd:
           course = enform.objects.filter(email__iexact=email).values('course')[0]['course']
           print("COURSE ",course)
           if course=="3MonthPlanH":
               return JsonResponse({"meta": {"status": "htmlVideo"}})
           if course=="6MonthPlanP":
               return JsonResponse({"meta": {"status": "javaVideo"}})
           if course=="9MonthPlanJ":
               return JsonResponse({"meta":{"status": "pythonVideo"}})
               

        else:
            return JsonResponse({"meta": {"status": 500}})
    else:
        return JsonResponse({"meta": {"status": 500}})



    return render(request, 'LoginForm.html')
def htmlVideo(request):
    return render(request, 'htmlVideo.html')
def pythonVideo(request):
    return render(request, 'pythonVideo.html')
def javaVideo(request):
    return render(request, 'javaVideo.html')

