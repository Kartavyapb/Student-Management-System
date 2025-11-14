from django.contrib import admin

from modelapp.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
                        'Name',  'student_id', 'Gender', 'DOB', 'Age', 'Blood_Group', 'Nationality' , 'Category' , 'Religion',
                        'Phone_Number', 'Email', 'Address',
                        'Father_Name', 'Father_Occupation', 'Mother_Name', 'Mother_Occupation', 'Parents_Address',
                        'Marks', 'Roll_Number', 
                        'Department', 'Assigned_Teacher',
                        'Total_Fees', 'Paid_Fees', 'Due_Fees'
                    )
    
    readonly_fields = ('student_id','Marks', 'Blood_Group', 'Nationality', 'Category', 'Religion', 'Father_Name', 'Mother_Name', 'Total_Fees')
    
    search_fields = ('Name', 'student_id', 'Gender', 'Blood_Group' , 'Department')

    def save_model(self, request, obj, form, change):
        obj.save()

        