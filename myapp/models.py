from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
class company_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    pin=models.BigIntegerField()
    post=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    website=models.CharField(max_length=100)
class candidate_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=150)
    post=models.CharField(max_length=150)
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=150)
    photo=models.FileField()
class feedback_table(models.Model):
    CANDIDATE=models.ForeignKey(candidate_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=300)
    COMPANY = models.ForeignKey(company_table,on_delete=models.CASCADE)
    rating=models.FloatField()
    date=models.DateField()
class course_table(models.Model):
    course=models.CharField(max_length=100)
    course_details=models.CharField(max_length=300)


class vacancy_table(models.Model):
    COMPANY=models.ForeignKey(company_table,on_delete=models.CASCADE)
    vacancy=models.CharField(max_length=150)
    date=models.DateField()
    no_of_vacancy=models.BigIntegerField()
    details=models.CharField(max_length=300)


class materials_table(models.Model):
    COURSE=models.ForeignKey(course_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    details=models.CharField(max_length=10000)
    file=models.FileField()

class resume_table(models.Model):
    CANDIDATE=models.ForeignKey(candidate_table,on_delete=models.CASCADE)
    resume=models.FileField()
    date=models.DateField()

class test_table(models.Model):
    VACANCY=models.ForeignKey(vacancy_table,on_delete=models.CASCADE)
    test_name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)

class questions_table(models.Model):
    TEST=models.ForeignKey(test_table,on_delete=models.CASCADE)
    questions=models.CharField(max_length=150)
    option_1=models.CharField(max_length=100)
    option_2=models.CharField(max_length=100)
    option_3=models.CharField(max_length=100)
    option_4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)


class result_table(models.Model):
    CANDIDATE=models.ForeignKey(candidate_table,on_delete=models.CASCADE)
    QUESTIONS=models.ForeignKey(questions_table,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    result=models.CharField(max_length=100)

class job_request_table(models.Model):
    VACANCY=models.ForeignKey(vacancy_table,on_delete=models.CASCADE)
    CANDIDATE=models.ForeignKey(candidate_table,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100,default="pending")


class interviewcall_table(models.Model):
    JOB_REQ_id=models.ForeignKey(job_request_table,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.CharField(max_length=100)
    updated_date=models.DateField()
    status=models.CharField(max_length=100)

class notification_table(models.Model):
    company=models.ForeignKey(company_table,on_delete=models.CASCADE)
    notification = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)

# ifconfig()
#     date=models.DateField()
#

class skills_table(models.Model):
    CANDIDATE=models.ForeignKey(candidate_table,on_delete=models.CASCADE)
    skills = models.CharField(max_length=100)
    details = models.CharField(max_length=10000)