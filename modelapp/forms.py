from django import forms

from django.forms import ModelForm

from modelapp.models import Student

class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['Name' , 'Gender' , 'DOB' , 'Age' ,'Blood_Group' , 'Nationality' , 'Category' , 'Religion' , 'Photo']                                                                                   # for all data use "__all__"

        widgets = {
            'DOB' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control bg-light',
                'placeholder': 'Auto-calculated'
            }),
        }

#------------------------------------------------------------------------------------------------

class AddContactForm(ModelForm):
    class Meta:
        model = Student
        fields = ['Phone_Number' , 'Email' , 'Address']

#------------------------------------------------------------------------------------------------

class AddParentsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['Father_Name' , 'Father_Occupation' , 'Mother_Name' , 'Mother_Occupation' , 'Parents_Address']

#------------------------------------------------------------------------------------------------

class AddAcademicForm(ModelForm):
    class Meta:
        model = Student
        fields = ['Roll_Number' , 'Marks']

#------------------------------------------------------------------------------------------------

class AddCourseForm(ModelForm):
    class Meta:
        model = Student
        fields = ['Department' , 'Assigned_Teacher']

#------------------------------------------------------------------------------------------------

class AddFeesForm(ModelForm):
    class Meta:
        model = Student
        fields = ['Total_Fees' , 'Paid_Fees' , 'Due_Fees']
        widgets = {
            'Due_Fees' : forms.NumberInput(attrs={'readonly': 'readonly',
                                            'class': 'form-control bg-light',
                                            'placeholder': 'Auto-calculated'}),
        }
    


class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
                    'Name' , 'Gender' , 'DOB' , 'Age' ,'Blood_Group' , 'Nationality' , 'Category' , 'Religion' , 'Photo',
                    'Phone_Number' , 'Email' , 'Address' ,
                    'Father_Name' , 'Father_Occupation' , 'Mother_Name' , 'Mother_Occupation' , 'Parents_Address' ,
                    'Roll_Number' , 'Marks' , 
                    'Department' , 'Assigned_Teacher' ,
                    'Total_Fees' , 'Paid_Fees' , 'Due_Fees'
                ]   

        widgets = {
            'DOB' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control bg-light',
                'placeholder': 'Auto-calculated'
            }),
            'Due_Fees' : forms.NumberInput(attrs={'readonly': 'readonly' , 
                                            'class': 'form-control bg-light',
                                            'placeholder': 'Auto-calculated'}),
        }

        