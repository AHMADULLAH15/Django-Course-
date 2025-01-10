from django.shortcuts import render
from first_app.forms import StudentForms
# Create your views here.
def home(request):
    # student = StudentForms()
    if request.method == 'POST':
        student = StudentForms(request.POST)
        if student.is_valid():
            # student.save(commit=False)
            student.save()
            print(student.cleaned_data)
            # return HttpResponse("Data saved")
    else:
        student = StudentForms()
    return render(request, 'home.html',{'student':student})