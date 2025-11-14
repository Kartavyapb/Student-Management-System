from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.core.validators import RegexValidator

class Student(models.Model):

    Gender_Choices = [
        ('','--Select Gender--'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]

    bldg_choices = [
        ('', '--Select Blood Group--'),
        ('A+','A+')   ,  ('A-','A-'),
        ('B+','B+')   ,  ('B-','B-'),
        ('AB+','AB+') ,  ('AB-','AB-'),
        ('O+','O+')   ,  ('O-','O-'),
    ]

    category_choices = [
        ('', '--Select Category--'),
        ('SC','SC'),
        ('ST','ST'),
        ('NT','NT'),
        ('OBC','OBC'),
        ('General','General'),
    ]
    
    
    Name        = models.CharField(max_length=80)
    Gender      = models.CharField(max_length=10, choices=Gender_Choices,default='', verbose_name="Gender", null=True, blank=True)
    DOB         = models.DateField(verbose_name = 'Date of Birth', null = True, blank=True)
    Age         = models.IntegerField(null=True, blank=True)
    Blood_Group = models.CharField(max_length=5, choices=bldg_choices, default='' ,verbose_name="Blood Group", null=True, blank=True)
    Nationality = models.CharField(max_length=20, default='Indian')
    Category    = models.CharField(max_length=10, choices=category_choices, default='' , verbose_name="Category")
    Religion    = models.CharField(max_length=20)
    Photo       = models.ImageField(upload_to='profile_images', null=True, blank=True)

#----------------------------------------------------------------------

    Phone_Number = PhoneNumberField(region='IN')
    Email        = models.EmailField()
    Address      = models.TextField()

#----------------------------------------------------------------------

    Father_Name          = models.CharField(max_length=80)
    Father_Occupation    = models.CharField()
    Mother_Name          = models.CharField(max_length=80)
    Mother_Occupation    = models.CharField()
    Parents_Address      = models.TextField()

#----------------------------------------------------------------------

    student_id     = models.CharField(max_length=10, unique=True, editable=False)
    Roll_Number    = models.IntegerField(null=True, blank=True)
    Marks          = models.FloatField(null=True, blank=True)
    
#----------------------------------------------------------------------

    Department         = models.CharField(max_length=20)
    Assigned_Teacher   = models.CharField(max_length=50)

#----------------------------------------------------------------------

    Total_Fees      = models.IntegerField(null=True, blank=True)
    Paid_Fees       = models.IntegerField(null=True, blank=True)
    Due_Fees        = models.IntegerField(null=True, blank=True)
    


    def save(self, *args, **kwargs):
        if not self.student_id:
            last_student = Student.objects.order_by('-id').first()
            if last_student and last_student.student_id:
                last_id = int(last_student.student_id[3:])
                new_id = f'STU{last_id + 1:04d}'
            else:
                new_id = 'STU0001'
            self.student_id = new_id

        if self.DOB:
            today = date.today()
            self.Age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))

        if self.Total_Fees is not None and self.Paid_Fees is not None:
            self.Due_Fees = self.Total_Fees - self.Paid_Fees
        
        print(f"Calculating Due_Fees : {self.Total_Fees} - {self.Paid_Fees}")

        super(Student, self).save(*args, **kwargs)



    def __str__(self):
        return self.name