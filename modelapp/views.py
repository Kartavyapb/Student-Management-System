from django.shortcuts import render, redirect
from modelapp.forms import AddStudentForm , AddContactForm , AddParentsForm , AddAcademicForm , AddCourseForm , AddFeesForm , UpdateStudentForm
from django.contrib.auth.forms import UserCreationForm
from modelapp.models import Student
from django.http import HttpResponse


#--------------------------------------------------------------------------------

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')

    return render(request, 'modelapp/register.html', {'form' : form})

#-------------------------------------------------------------------------------

def home(request):

    return render(request, 'modelapp/home.html')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def add_student_info(request):

    print(request.POST)         # o/p:- {'name': ['Kartavya Badge'], 'marks': ['99.99'], 'roll_num': ['101'], 'age': ['23'], 'dept': ['computer science']}

    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            request.session['student_id'] = student.id
            return redirect('/contact/')

    context = {
        'forms' : AddStudentForm()
    }

    return render(request, 'modelapp/add.html', context)

#------------------------------------------------------------------------------------

def add_contact_info(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = AddContactForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/parents/')
        
    context = {
        'forms' : AddContactForm(instance=student)
    }

    return render(request, 'modelapp/contact.html', context)


#-------------------------------------------------------------------------------------

def add_parents_info(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = AddParentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/academic/')
        
    context = {
        'forms' : AddParentsForm(instance=student)
    }

    return render(request, 'modelapp/parents.html', context)


#-------------------------------------------------------------------------------------

def add_acdemic_info(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = AddAcademicForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/course/')
        
    context = {
        'forms' : AddAcademicForm(instance=student)
    }

    return render(request, 'modelapp/academic.html', context)


#-------------------------------------------------------------------------------------

def add_course_info(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = AddCourseForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/fees/')
        
    context = {
        'forms' : AddCourseForm(instance=student)
    }
 
    return render(request, 'modelapp/course.html', context)


#-------------------------------------------------------------------------------------

def add_fees_info(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = AddFeesForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/list/')
        
    context = {
        'forms' : AddFeesForm(instance=student)
    }

    return render(request, 'modelapp/fees.html', context)


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


def student_list_view(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'name')
    
    students = Student.objects.all()

    if search_query:
        students =  students.filter(Name__icontains=search_query)
    
    if sort_by.lower() == 'name':
        students =  students.order_by('Name')
    elif sort_by == 'age':
        students =  students.order_by('Age')

    context = {
        'data' : students ,
        'search_query' : search_query ,
        'sort_by' : sort_by 
    }

    return render(request, 'modelapp/list.html',context)

#----------------------------------------------------------------------------------------

def student_detail_view(request,id):
    context = {
            'obj' : Student.objects.get(pk=id)
    }
    return render(request, 'modelapp/detail.html',context)

#--------------------------------------------------------------------------------------------

def student_delete_view(request,id):
    obj = Student.objects.get(pk = id)
    obj.delete()

    return redirect('/list/')

#-----------------------------------------------------------------------------------------------

def student_update_view(request, id):

    obj = Student.objects.get(pk = id)

    form = UpdateStudentForm(request.POST , request.FILES , instance = obj)

    if form.is_valid():
        form.save()
        return redirect(f'/detail/{obj.id}/')

    context = {
            'form' : UpdateStudentForm(instance = obj )
    }

    return render(request, 'modelapp/update.html', context)

#--------------------------------------------------------------------------------------------------