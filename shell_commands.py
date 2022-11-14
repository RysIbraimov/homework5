from employee.models import *

#1 Создание 4-x Emloyee (с какими то данными, одним из них должны быть Вы. То есть ввести свои данные)

e1 = Employee.objects.create(name='Arsen',birth_date='1990-04-18',position='manager',salary=30000,work_experience='2012-01-22')
e2 = Employee.objects.create(name='Aidai',birth_date='1995-05-18',position='singer',salary=60000,work_experience='2019-01-22')
e3 = Employee.objects.create(name='Sultan',birth_date='1999-07-23',position='soldier',salary=40000,work_experience='2010-01-22')
e4 = Employee.objects.create(name='Yryskeldi',birth_date='1999-07-23',position='student',salary=0,work_experience='2022-08-22')

#2 Добавление им паспортных данных (себе можно вписать НЕ настоящие паспортные данные)
p1 = Passport.objects.create(inn=219900418205,id_card=4567890,employee=e1)
p2 = Passport.objects.create(inn=119900456205,id_card=2317890,employee=e2)
p3 = Passport.objects.create(inn=219912318205,id_card=4568760,employee=e3)
p4 = Passport.objects.create(inn=219900418205,id_card=4567890,employee=e4)

#Удаление последней записи паспортных данных, и сотрудника
# e4.delete()
# p4.delete()

#4 Создание WorkProject
work_p = WorkProject(id=1,project_name='Python')
work_p.save()
#Добавление в WorkProject всех созданных сотрудников одной датой.
work_p.employee.set([e1,e2,e3,e4],through_defaults={'date_joined':'2022-08-22'})

#Удаление одного из сотрудников
work_p.employee.remove(e1)
#Добавление нового сотрудника, которого еще не было
work_p.employee.create(name='Nurlan',birth_date='1990-04-18',position='manager',salary=30000,through_defaults={'date_joined':'2018-06-07'})

#Создание новых клиентов (3 чел)
c1 = Client.objects.create(name='Aisuluu',birth_date='1991-06-09',address='lala',phone_number=8000)
c2 = Client.objects.create(name='Aisuluu',birth_date='1991-06-09',address='blala',phone_number=10000)
c3 = Client.objects.create(name='Aisuluu',birth_date='1991-06-09',address='lala',phone_number=20000)

#Создание нового VIP клиента (1 чел)
vip_c = VipClient(name='Janyl',birth_date='1999-06-09',address='jjjj',phone_number=250000,vip_satus_start=True,donation_amaount=10000)
vip_c.save()
#Удаление одного из обычных клиентов
c3.delete()
#Вывести в окно терминала список всех Employee
print(Employee.objects.all())
#Вывести в окно терминала список всех Employee с паспортными данными
print(Passport.employee)
#Вывести в окно терминала все проекты
print(WorkProject.objects.all())
#Вывести всех Клиентов
print(Client.objects.all())
print(VipClient.objects.all())

