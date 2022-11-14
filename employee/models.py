from django.db import models
import datetime
# Create your models here.
class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        today = datetime.date.today()
        age = today - self.birth_date
        return f'{age.year}'

class Employee(AbstractPerson):
    position = models.CharField(max_length=30)
    salary = models.IntegerField()
    work_experience = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.position

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        print(f'employee : {self.name} - {self.position} - {self.salary} - {self.work_experience} saved')

    class Meta:
        db_table = 'employee'

class Passport(models.Model):
    inn = models.IntegerField()
    id_card = models.IntegerField()
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee.name}'

    def get_gender(self):
        if list(self.inn[0]) == 1:
            return 'Female'
        else:
            return 'Male'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        print(f'Passport : {self.employee.name} - {self.inn}  - {self.id_card} saved')

    class Meta:
        db_table = 'passport'

class WorkProject(models.Model):
    project_name = models.CharField(max_length=30)
    employee = models.ManyToManyField(Employee, through="Membership")

    def __str__(self):
        return self.project_name

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        print(f'Project : {self.project_name} - {self.employee.name} saved')

    class Meta:
        db_table = 'work_project'

class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.project.name} - {self.employee.name}'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        print(f'{self.employee.name} {self.project.name} saved')

    class Meta:
        db_table = 'membership'

class Client(AbstractPerson):
    address = models.CharField(max_length=30)
    phone_number = models.IntegerField()

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        print(f'client :{self.name} - {self.address} - {self.phone_number} saved')

class VipClient(Client):
    vip_satus_start = models.BooleanField(default=False)
    donation_amaount = models.IntegerField()

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        print(f'Vip client : {self.vip_satus_start} - {self.donation_amaount} saved')


