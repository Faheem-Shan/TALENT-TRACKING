import datetime

import math
import random

from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.


from myapp.models import *
# from myapp.sampleee import pdf_reader
from myapp.sampleee import pdf_reader


def login(request):
    return render(request,'login.html')




def login_post(request, ob1=None):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    lobj = login_table.objects.filter(username=username, password=password)
    if lobj.exists():
        lobj = lobj[0]
        request.session['lid'] = lobj.id
        request.session['lin'] = 1
        request.session['log'] = 'lo'
        if lobj.type == 'admin':

            return HttpResponse("<script>alert('LOGINED');window.location='/admin_home'</script>")
        elif lobj.type == 'company':




            obx=company_table.objects.filter(LOGIN=lobj.id)

            if len(obx)>0:

                request.session['lid'] = lobj.id

                return HttpResponse("<script>alert('LOGINED');window.location='/company_home'</script>")
            else:
                return HttpResponse("<script>alert('User not Found');window.location='/'</script>")


        elif lobj.type == 'user':
            request.session['lid'] = lobj.id

            return HttpResponse("<script>alert('LOGINED');window.location='/userhome'</script>")
        else:
            return HttpResponse("<script>alert('User not Found');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('User not Found');window.location='/'</script>")

def logout(request):
    request.session['lin'] = 0
    return render(request, "login.html")
    # try:
    #     user=login_table.objects.get(username=username,password=password)
    #     if user.type=='admin':
    #         ob1=auth.authenticate(username='admin',password='admin')
    #     if ob1 is not None:
    #         auth.login(request,ob1)
    #
    #         return HttpResponse('''<script>alert("admin logined in successfully");window.location='/admin_home'</script>''')
    #     elif user.type == 'company':
    #         ob1 = auth.authenticate(username='admin', password='admin')
    #         if ob1 is not None:
    #             auth.login(request, ob1)
    #
    #         request.session['lid']=user.id
    #
    #         ob=company_table.objects.filter(LOGIN=user.id)
    #
    #         if len(ob)>0:
    #             return HttpResponse(
    #                 '''<script>alert("Company logined in successfully");window.location='/company_home'</script>''')
    #         else:
    #             return HttpResponse(
    #                 '''<script>alert("Invalid logined");window.location='/'</script>''')
    #
    #     elif user.type == 'user':
    #         ob1 = auth.authenticate(username='admin', password='admin')
    #         if ob1 is not None:
    #             auth.login(request, ob1)
    #
    #         request.session['lid']=user.id
    #
    #         ob=candidate_table.objects.filter(LOGIN=user.id)
    #
    #         if len(ob)>0:
    #             return HttpResponse(
    #                 '''<script>alert("Company logined in successfully");window.location='/userhome'</script>''')
    #         else:
    #             return HttpResponse(
    #                 '''<script>alert("Invalid logined");window.location='/'</script>''')
    #
    #
    #     else:
    #         return HttpResponse('''<script>alert("invalid username and password");window.location='/'</script>''')
    # except:
    #     return HttpResponse('''<script>alert("invalid");window.location='/'</script>''')
def admin_home(request):
    return render(request,'ADMIN/adminmainindex.html')


def admin_add_course(request):
    return render(request,'ADMIN/add course.html')

def admin_add_course_post(request):
    course_name=request.POST["textfield"]
    course_details=request.POST["textfield2"]

    obb=course_table()
    obb.course=course_name
    obb.course_details=course_details
    obb.save()
    return HttpResponse('''<script>alert("added");window.location='/admin_view_course'</script>''')


def admin_add_materials(request):
    ob=course_table.objects.all()
    return render(request,'ADMIN/add materilas.html',{"course":ob})

def admin_add_materials_post(request):
    material_name=request.POST["textfield"]
    COURSE=request.POST["select"]
    details=request.POST["textfield3"]
    file=request.FILES["file"]

    fs=FileSystemStorage()
    fsave=fs.save(file.name,file)


    obb=materials_table()
    obb.name=material_name
    obb.COURSE_id=COURSE
    obb.details=details
    obb.file=fsave
    obb.save()
    return HttpResponse('''<script>alert("added");window.location='/admin_view_materials'</script>''')





def company_registration_post(request):
    company_name=request.POST["textfield"]
    place=request.POST["textfield2"]
    pin=request.POST["textfield3"]
    post=request.POST["textfield4"]
    phone=request.POST["textfield5"]
    E_mail=request.POST["textfield6"]
    Website=request.POST["textfield7"]
    Username=request.POST["textfield8"]
    Password=request.POST["textfield9"]

    ob = login_table()
    ob.username = Username
    ob.password = Password
    ob.type = "pending"
    ob.save()

    obb=company_table()
    obb.LOGIN=ob
    obb.name=company_name
    obb.place=place
    obb.post=post
    obb.phone=phone
    obb.email=E_mail
    obb.pin=pin
    obb.website=Website
    obb.Username=Username
    obb.Password=Password
    obb.save()
    return HttpResponse('''<script>alert("added");window.location='/'</script>''')

#
# def admin_home(request):
#     return render(request,'ADMIN/admin home.html')

def admin_company_verify(request):
    ob=company_table.objects.all()
    return render(request,'ADMIN/company verify.html',{"data":ob})



def admin_edit_course(request,id):
    request.session["crid"]=id
    ob=course_table.objects.get(id=id)
    return render(request,'ADMIN/Edit course.html',{"data":ob})

def edit_course_post(request):
    Course_name = request.POST["textfield"]
    Course_details = request.POST["textfield2"]

    obb = course_table.objects.get(id=request.session['crid'])
    obb.course=Course_name
    obb.course_details=Course_details
    obb.save()
    return HttpResponse('''<script>alert("updated");window.location='/admin_view_course'</script>''')


def admin_edit_materials(request,id):
    request.session["crid"] = id
    ob = course_table.objects.all()
    obb=materials_table.objects.get(id=request.session["crid"])
    return render(request,'ADMIN/edit materials.html',{"data":ob,'val':obb})

def edit_materials_post(request):
    try:
        material_name = request.POST["textfield"]
        COURSE = request.POST["select"]
        details = request.POST["textfield3"]
        file = request.FILES["file2"]
        fs = FileSystemStorage()
        fsave = fs.save(file.name, file)
        obb = materials_table.objects.get(id=request.session["crid"])
        obb.name = material_name
        obb.COURSE_id = COURSE
        obb.details = details
        obb.file = fsave
        obb.save()
        return HttpResponse('''<script>alert("updated");window.location='/admin_view_materials'</script>''')
    except Exception as e:
        print("----------------",e)
        material_name = request.POST["textfield"]
        COURSE = request.POST["select"]
        details = request.POST["textfield3"]
        obb = materials_table.objects.get(id=request.session["crid"])
        obb.name = material_name
        obb.COURSE_id = COURSE
        obb.details = details
        obb.save()
        return HttpResponse('''<script>alert("updated");window.location='/admin_view_materials'</script>''')

def delete_materilas(request,id):
    request.session['cid']=id
    ob=materials_table.objects.get(id=request.session['cid'])
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/admin_view_materials'</script>''')



def admin_view_course(request):
    ob=course_table.objects.all()
    return render(request,'ADMIN/view course.html',{"val":ob})


def admin_search_course(request):
    course=request.POST['textfield']
    ob=course_table.objects.filter(course__istartswith=course)
    return render(request,'ADMIN/view course.html',{"val":ob,'course':course})

def admin_search_company_verify(request):
    name=request.POST['textfield']
    ob=company_table.objects.filter(name__istartswith=name)
    return render(request,'ADMIN/company verify.html',{"data":ob,'name':name})









def admin_view_feedback(request):
    ob=feedback_table.objects.all()
    return render(request,'ADMIN/view feedback.html',{"val":ob})

def admin_view_feedback_search(request):
    date1=request.POST["d1"]
    date2=request.POST["d2"]


    ob=feedback_table.objects.filter(date__range=(date1,date2))
    return render(request,'ADMIN/view feedback.html',{"val":ob})

def admin_view_materials(request):
    ob=materials_table.objects.all()
    obb=course_table.objects.all()
    return render(request,'ADMIN/view materials.html',{'val':ob,'data':obb})



def admin_search_materials(request):
    COURSE=request.POST['select']
    ob=materials_table.objects.filter(COURSE=COURSE)
    obb = course_table.objects.all()
    return render(request,'ADMIN/view materials.html',{'val':ob,'data':obb})








def admin_view_result(request):

    tes=test_table.objects.all()
    data=[]
    for i in tes:
        can=candidate_table.objects.all()
        quest=questions_table.objects.filter(TEST=i.id)
        for j in can:
            ob_incorre=result_table.objects.filter(CANDIDATE=j.id,QUESTIONS__TEST=i.id,result="Incorrect")
            ob_corre=result_table.objects.filter(CANDIDATE=j.id,QUESTIONS__TEST=i.id,result="Correct")
            r={"sname":j.name,"test":i.test_name,"correct":str(len(ob_corre)),"incorrect":str(len(ob_incorre)),"total":str(len(quest))}
            data.append(r)

    return render(request,'ADMIN/view result.html',{"val":data})
def company_ragistration(request):
    return render(request,'companyregistration.html')


def delete_course(request,id):
    request.session['cid']=id
    ob=course_table.objects.get(id=request.session['cid'])
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/admin_view_course'</script>''')

def acceptcompany(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='company'
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location='/admin_company_verify'</script>''')
def rejectedcompany(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='Rejected'
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location='/admin_company_verify'</script>''')


#------------------company

def company_home(request):
    return render(request,'COMPANY/index.html')

def change_password(request):
    return render(request, 'COMPANY/change password.html')

def change_password_post(request):
    Current_password = request.POST["textfield"]
    New_password = request.POST["textfield2"]
    Confirm_password = request.POST["textfield3"]
    obb = login_table.objects.get(id=request.session['lid'])
    if obb.password == Current_password:
        if New_password == Confirm_password:
            obb.password=New_password
            obb.save()
            return HttpResponse('''<script>alert("Changed Successfully");window.location='/company_home'</script>''')
        else:
            return HttpResponse('''<script>alert("New password does not match");window.location='/company_home'</script>''')
    else:
        return HttpResponse('''<script>alert("Current password is invalid ");window.location='/company_home'</script>''')

def view_profile(request):
    ob = company_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request, 'COMPANY/view profile.html', {"val": ob})

def edit_profile(request):
    ob=company_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'COMPANY/edit profile.html',{'val':ob})

def edit_profile_post(request):
    name = request.POST["textfield"]
    place = request.POST["textfield2"]
    pin = request.POST["textfield3"]
    post = request.POST["textfield4"]
    phone = request.POST["textfield5"]
    email = request.POST["textfield6"]
    website = request.POST["textfield7"]
    obb = company_table.objects.get(LOGIN__id=request.session['lid'])
    obb.name = name
    obb.place = place
    obb.phone = phone
    obb.email = email
    obb.post = post
    obb.pin = pin
    obb.website = website
    obb.save()
    return HttpResponse('''<script>alert("updated");window.location='/view_profile'</script>''')


# def view_vacancy(request):
#     ob =company_table.objects.get(LOGIN__id=request.session['lid'])
#     return render(request, 'COMPANY/view_vacancy.html',{"val": ob})

def view_vacancy(request):
    ob=vacancy_table.objects.filter(COMPANY__LOGIN_id=request.session['lid'])
    return render(request, 'COMPANY/view vacancy.html',{'val':ob})

def view_applications(request,id):
    request.session['vid']=id
    ob=job_request_table.objects.filter(VACANCY=id)
    return render(request, 'COMPANY/viewApplications.html',{'val':ob})




import re
WORD = re.compile(r'\w+')
from collections import Counter
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
def view_shortlist_applications(request):

    ob=job_request_table.objects.filter(VACANCY=request.session['vid'])

    for i in ob:
        resumdata=resume_table.objects.get(CANDIDATE=i.CANDIDATE.id)
        text = pdf_reader(r"E:\Project\MAIN PROJECT\TALENT_TRACKING\jobseeker\media\/"+str(resumdata.resume))

        # print("trx----",text)
        vec1 = text_to_vector(text)
        vec2 = text_to_vector(i.VACANCY.vacancy+" "+i.VACANCY.details)

        print("=================================")
        print(vec1)
        print("+++++++++++++++++++++++++++")
        print(vec2)
        print("+++++++++++++++++++++++++++")

        sim = get_cosine(vec1, vec2)



        print("Similiaruty=====",sim)

        if sim>0.1:
            obx=job_request_table.objects.get(id=i.id)
            obx.status="shortlisted"
            obx.save()
        else:
            obx = job_request_table.objects.get(id=i.id)
            obx.status = "rejected"
            obx.save()




    return view_applications(request,request.session['vid'])

def interviecall(request,reqid):
    request.session["reqid"]=reqid

    obx=job_request_table.objects.get(id=reqid)

    tes = test_table.objects.filter(VACANCY=obx.VACANCY.id)
    data = []
    for i in tes:
        quest = questions_table.objects.filter(TEST=i.id)

        ob_incorre = result_table.objects.filter(CANDIDATE=obx.CANDIDATE.id, QUESTIONS__TEST=i.id, result="Incorrect")
        ob_corre = result_table.objects.filter(CANDIDATE=obx.CANDIDATE.id, QUESTIONS__TEST=i.id, result="Correct")
        r = {"test": i.test_name, "correct": str(len(ob_corre)), "incorrect": str(len(ob_incorre)),
             "total": str(len(quest))}
        data.append(r)

    return render(request,'COMPANY/interviewcall.html',{"data":data})

def interviewCallpost(request):
    date=request.POST["date"]
    time=request.POST["time"]

    ob=interviewcall_table()
    ob.JOB_REQ_id_id=request.session["reqid"]
    ob.date=date
    ob.time=time
    ob.updated_date=datetime.datetime.now().date()
    ob.status="pending"
    ob.save()

    obx = job_request_table.objects.get(id=request.session["reqid"])
    obx.status = "Direct Interview Call"
    obx.save()


    # return view_applications(request,request.session['vid'])
    return HttpResponse("<script>alert('alloacted...');window.location='/view_applications/"+str(request.session['vid'])+"'</script>")


def company_add_vacancy(request):
    return render(request,'COMPANY/add vacancy.html')

def company_add_vacancy_post(request):
    Vacancy=request.POST["textfield"]
    No_of_vacancies=request.POST["textfield3"]
    Details=request.POST["textfield4"]

    obb=vacancy_table()
    obb.COMPANY=company_table.objects.get(LOGIN_id=request.session['lid'])
    obb.vacancy = Vacancy
    from datetime import datetime
    obb.date = datetime.now()
    obb.no_of_vacancy = No_of_vacancies
    obb.details = Details
    obb.save()
    return HttpResponse('''<script>alert("added");window.location='/view_vacancy';</script>''')


def company_edit_vacancy(request,id):
    request.session['vid']=id
    ob=vacancy_table.objects.get(id=request.session['vid'])
    return render(request,'COMPANY/edit vacancy.html',{'val':ob})

def edit_vacancy_post(request):
    vacancy = request.POST["textfield1"]
    no_of_vacancy = request.POST["textfield3"]
    details = request.POST["textfield4"]

    obb = vacancy_table.objects.get(id=request.session['vid'])
    obb.COMPANY = company_table.objects.get(LOGIN_id=request.session['lid'])
    obb.vacancy = vacancy
    obb.no_of_vacancy = no_of_vacancy
    from datetime import datetime
    obb.date = datetime.now()
    obb.details = details
    obb.save()
    return HttpResponse('''<script>alert("updated");window.location='/view_vacancy'</script>''')

def delete_vacancy(request,id):
    request.session['cid']=id
    ob=vacancy_table.objects.get(id=request.session['cid'])
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/view_vacancy'</script>''')

def view_test(request):
    ob = test_table.objects.filter(VACANCY__COMPANY__LOGIN__id=request.session['lid'])
    return render(request, 'COMPANY/view test.html', {"val": ob})

def add_test(request):
    ob=vacancy_table.objects.filter(COMPANY__LOGIN_id=request.session['lid'])
    return render(request,'COMPANY/add test.html',{'val':ob})


def comapny_view_notification(request):
    return render(request,'COMPANY/company notification.html')




def send_notification(request):
    notification=request.POST["textfield"]
    obb=notification_table()
    obb.company=company_table.objects.get(LOGIN__id=request.session['lid'])
    obb.Date = datetime.datetime.today()
    obb.notification = notification
    obb.save()
    return HttpResponse('''<script>alert("added");window.location='/company_home';</script>''')





def add_test_post(request):
    Vacancy=request.POST["select"]
    Test=request.POST["textfield2"]
    Description=request.POST["textfield3"]

    obb=test_table()
    obb.VACANCY=vacancy_table.objects.get(id=Vacancy)
    obb.test_name = Test
    obb.description = Description
    obb.save()
    return HttpResponse('''<script>alert("added");window.location='/view_test';</script>''')


def edit_test(request,id):
    request.session['vid']=id
    obb = vacancy_table.objects.filter(COMPANY__LOGIN_id=request.session['lid'])
    ob=test_table.objects.get(id=request.session['vid'])
    return render(request,'COMPANY/edit test.html',{'val':ob,'data':obb})

def edit_test_post(request):
    VACANCY = request.POST["select"]
    test_name = request.POST["textfield2"]
    description = request.POST["textfield3"]

    obb=test_table.objects.get(id=request.session['vid'])
    obb.VACANCY=vacancy_table.objects.get(id=VACANCY)
    obb.test_name = test_name
    obb.description = description
    obb.save()
    return HttpResponse('''<script>alert("Updated");window.location='/view_test';</script>''')

def delete_test(request,id):
    request.session['cid']=id
    ob=test_table.objects.get(id=request.session['cid'])
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/view_test'</script>''')

def view_questions(request,testid):
    request.session["testid"]=testid
    ob=questions_table.objects.filter(TEST=testid)
    return render(request, 'COMPANY/view questions.html', {"val": ob})


def add_question(request):
    return render(request,'COMPANY/add question.html')

def add_question_post(request):
    Question=request.POST["textfield"]
    Option1=request.POST["textfield2"]
    Option2=request.POST["textfield3"]
    Option3=request.POST["textfield4"]
    Option4=request.POST["textfield5"]
    Answer=request.POST["textfield6"]

    obb=questions_table()
    obb.TEST_id=request.session["testid"]
    obb.questions=Question
    obb.option_1 = Option1
    obb.option_2 = Option2
    obb.option_3 = Option3
    obb.option_4 = Option4
    obb.answer = Answer
    obb.save()
    return view_questions(request,request.session["testid"])


def edit_question(request,id):
    request.session["qid"]=id
    ob=questions_table.objects.get(id=request.session["qid"])
    return render(request,'COMPANY/edit question.html',{'val':ob,})


def edit_question_post(request):
    Question = request.POST["textfield"]
    option1 = request.POST["textfield2"]
    option2 = request.POST["textfield3"]
    option3 = request.POST["textfield4"]
    option4 = request.POST["textfield5"]
    Answer = request.POST["textfield6"]

    obb=questions_table.objects.get(id=request.session['qid'])
    obb.questions = Question
    obb.option_1 = option1
    obb.option_2 = option2
    obb.option_3 = option3
    obb.option_4 = option4
    obb.answer = Answer
    obb.save()
    return view_questions(request, request.session["testid"])

def delete_questions(request,id):
    request.session['qid']=id
    ob=questions_table.objects.get(id= request.session['qid'])
    ob.delete()
    return view_questions(request, request.session["testid"])


def view_result(request):
    ob=result_table.objects.all()
    return render(request,'COMPANY/view result.html',{"val":ob})


def view_feedback(request):
    ob=feedback_table.objects.all()
    return render(request,'COMPANY/view feedback.html',{"val":ob})

def view_feedback_search(request):
    date1=request.POST["d1"]
    date2=request.POST["d2"]


    ob=feedback_table.objects.filter(date__range=(date1,date2))
    return render(request,'COMPANY/view feedback.html',{"val":ob})

def reply_complaint(request,id):
    request.session['cid']=id
    ob=complaint_table.objects.get(id=request.session['cid'])
    return render(request, 'COMPANY/reply complaint.html')

def replypost(request):
    reply=request.POST['textfield']

    ob = complaint_table.objects.get(id=request.session['cid'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>alert("reply send successfull");window.location='/view_complaint';</script>''')


def view_complaint(request):
    ob = complaint.objects.filter(COMPANY__LOGIN_id=request.session['lid'])
    return render(request, 'COMPANY/view complaint.html',{'val':ob})



def view_resume(request):
    ob = resume_table.objects.all()
    return render(request, 'COMPANY/view resume.html',{"val":ob})

def view_interviewcall(request):
    ob = interviewcall_table.objects.all()
    return render(request, 'COMPANY/interviewcall.html',{"val":ob})


# ---------------------------User------------------------------

def userhome(request):
    return render(request,'USER/user index.html')

def user_view_profile(request):
    res =candidate_table.objects.get(LOGIN = request.session['lid'])
    return  render(request,"USER/view profile.html",{'data':res})


def edit_profile_user(request):
    res =candidate_table.objects.get(LOGIN = request.session['lid'])
    return  render(request,"USER/edit profile.html",{'data':res})
def edit_profile_action(request):
    try:
        name = request.POST['name']
        place = request.POST['place']
        pin = request.POST['pin']
        post = request.POST['post']
        phone = request.POST['phone']
        image = request.FILES['image']
        d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        fs = FileSystemStorage()
        # fs.save(r"C:\Users\Lenovo\Desktop\jobseeker\static\photo\\" + d + '.jpg', image)
        path = fs.save(image.name,image)
        candidate_table.objects.filter(LOGIN = request.session['lid']).update(name = name,place = place,pin = pin,post = post,phone = phone,photo = path)
        return HttpResponse('''<script>alert("Details Updated");window.location='/user_view_profile';</script>''')

    except Exception as e:
        name = request.POST['name']
        place = request.POST['place']
        pin = request.POST['pin']
        post = request.POST['post']
        phone = request.POST['phone']
        candidate_table.objects.filter(LOGIN=request.session['lid']).update(name=name, place=place, pin=pin, post=post,
                                                                            phone=phone)
        return HttpResponse('''<script>alert("Details Updated");window.location='/user_view_profile';</script>''')


def user_registration(request):
    return render(request,'USER/user registration.html')

def registrationcode(request):
    name=request.POST['name']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    email=request.POST['email']
    phone=request.POST['phone']
    password=request.POST['password']
    cpass=request.POST['cpass']
    image=request.FILES['image']
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs = FileSystemStorage()
    # fs.save(r"C:\Users\Lenovo\Desktop\jobseeker\static\photo\\"+d+'.jpg',image)
    # path = "/static/photo/"+d+'.jpg'
    path = fs.save(image.name,image)
    data = login_table.objects.filter(username = email)

    # if data.exists():
    #     return HttpResponse('''<script>alert("Email Alrerady Exists");window.location='/user_registration';</script>''')
    # else:
    if password == cpass:
        lob1 = login_table()
        lob1.username = email
        lob1.password = password
        lob1.type = 'user'
        lob1.save()
        lob = candidate_table()
        lob.name = name
        lob.place = place
        lob.post = post
        lob.pin = pin
        lob.phone = phone
        lob.email = email
        lob.photo = path
        lob.LOGIN_id = lob1.id
        lob.save()
        return HttpResponse('''<script>alert("Registration Success");window.location='/';</script>''')
    else:
        return HttpResponse('''<script>alert("Password missmatch");window.location='/user_registration';</script>''')


def user_upload_resume(request):
    return render(request,'USER/upload resume.html')


def user_upload_resume_action(request):
    resume = request.FILES['resume']
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs = FileSystemStorage()
    # fs.save(r"C:\Users\Lenovo\Desktop\jobseeker\static\resume\\" + d + '.pdf', resume)
    path = fs.save(resume.name,resume)
    data = resume_table.objects.filter(CANDIDATE__LOGIN = request.session['lid'])
    if data.exists():
        return HttpResponse('''<script>alert("Resume Already added");window.location='/userhome';</script>''')
    else:
        obj = resume_table()
        obj.resume = path
        obj.CANDIDATE_id = candidate_table.objects.get(LOGIN=request.session['lid']).id
        obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
        obj.save()
        return HttpResponse('''<script>alert("Uploaded");window.location='/userhome';</script>''')


def user_view_resume(request):
    res = resume_table.objects.get(CANDIDATE__LOGIN = request.session['lid'])
    return render(request,'USER/view resume.html',{'data':res})

def user_edit_resume(request):
    resume = request.FILES['resume']
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs = FileSystemStorage()
    # fs.save(r"C:\Users\Lenovo\Desktop\jobseeker\static\resume\\" + d + '.pdf', resume)
    path = fs.save(resume.name,resume)

    resume_table.objects.filter(CANDIDATE__LOGIN=request.session['lid']).update(resume = path)
    return HttpResponse('''<script>alert("Uploaded");window.location='/userhome';</script>''')


def view_candidate_vacancy(request):
    ob=vacancy_table.objects.all()
    print(ob,"wwww")
    return render(request,'USER/view vacancy.html',{'data':ob})


def apply_for_vacancy(request,id):
    data = job_request_table.objects.filter(VACANCY = id,CANDIDATE__LOGIN =request.session['lid'] )
    if data.exists():
        return HttpResponse('''<script>alert("Application already Exists");window.location='/view_candidate_vacancy';</script>''')
    else:
        obj = job_request_table()
        obj.CANDIDATE_id = candidate_table.objects.get(LOGIN=request.session['lid']).id
        obj.VACANCY_id = id
        obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
        obj.status = 'pending'
        obj.save()
        return HttpResponse('''<script>alert("Application added");window.location='/view_candidate_vacancy';</script>''')

def user_view_application(request):
    ob = job_request_table.objects.filter(CANDIDATE__LOGIN = request.session['lid'])
    return render(request,'USER/view application.html',{'data':ob})


def user_view_test(request,id):
    ar = test_table.objects.filter(VACANCY_id=id)
    return render(request, 'USER/view test.html',{'data': ar})
def user_view_interview_call(request,id):


    ob=interviewcall_table.objects.get(JOB_REQ_id_id=id)

    return render(request,'USER/InterView_info.html',{"in_date":ob.date,"in_time":ob.time,"status":ob.status})





def sendfeedback(request,id):
    return render(request,'USER/send feedback.html',{'id':id})

def sendfeedback_action(request,id):
    comp = request.POST['feedback']
    rating = request.POST['rating']
    lob = feedback_table()
    lob.CANDIDATE_id = candidate_table.objects.get(LOGIN_id=request.session['lid']).id
    lob.COMPANY_id = id
    lob.feedback = comp
    lob.rating = rating
    lob.date = datetime.datetime.today().now()
    lob.save()
    return HttpResponse('''<script>alert("Feedback added");window.location='/user_view_application';</script>''')


#########################################exam part###################################################################



def view_candidate_question2(request,id):
    ob=questions_table.objects.filter(TEST_id=id)
    return render(request, 'USER/view test.html',{'data': ob})

def view_result_canditate(request):
    lid=request.POST['lid']
    ob=result_table.objects.filter(CANDIDATE__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'QUESTIONS':i.QUESTIONS.questions,'answer':i.answer,'result':i.result,'cid':i.id}
        mdata.append(data)
    print(mdata)
    return JsonResponse({"status":"ok","data":mdata})

def view_candidate_question(request):
    lid=request.POST['lid']
    ob=result_table.objects.filter(CANDIDATE__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'QUESTIONS':i.QUESTIONS.questions,'result':i.result,'cid':str(i.id)}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def view_request_status(request):
    print(request.POST,"+++++++++++++++===========================+++++++++++++++==")
    tid=request.POST['lid']
    ob=job_request_table.objects.filter(CANDIDATE__LOGIN_id=tid)
    mdata=[]
    for i in ob:
        data={'VACANCY':i.VACANCY.vacancy,'date':i.date,'status':i.status,'cid':str(i.id)}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})

def candidate_submit_answer(request):
    print(request.POST,"")
    lid=request.POST['lid']
    qid=request.POST['qid']
    answer=request.POST['answer']
    obq=questions_table.objects.get(id=qid)
    result=0
    if answer==obq.ipconfig:
        result=1
    ob=result_table()
    ob.CANDIDATE=candidate_table.objects.get(LOGIN__id=lid)
    ob.QUESTIONS=obq
    ob.answer=answer
    ob.result=result
    return JsonResponse({"task":"ok"})





def start_quiz(request, test_id):
    # Fetch all questions related to the test
    questions = questions_table.objects.filter(TEST=test_id)
    kk=candidate_table.objects.get(LOGIN__id=request.session['lid'])
    candidate_id=kk.id
    # Shuffle questions for randomness
    questions = random.sample(list(questions), len(questions))

    request.session["ttid"]=test_id

    return render(request, 'ADMIN/Attent text.html', {'questions': questions, 'candidate_id': candidate_id, 'test_id': test_id})


def submit_answers(request):

    print("submit answer------")

    print(request.method)
    print(request.POST)
    if request.method == "POST":
        candidate_id=request.session['lid']
        test_id=request.POST['test_id']
        # Collect answers and store results
        candidate = candidate_table.objects.get(LOGIN__id=request.session['lid'])
        # questions = questions_table.objects.filter(TEST=test_id)
        questions = questions_table.objects.filter(TEST=request.session["ttid"])

        print(questions,"=========questionspppp",request.session["ttid"])

        score = 0
        for q in questions:

            print(q,"questions--------------")
            user_answer = request.POST.get("question_"+str(q.id))  # Get answer from form

            print("=====")
            print(user_answer,"---",q.answer)

            # Compare the user's answer with the correct one
            if user_answer == q.answer:

                print(user_answer,"====",q.answer)

                score += 1
            print("score=", score)


            # Store the result
            result = result_table.objects.create(
                CANDIDATE=candidate,
                QUESTIONS=q,
                answer=user_answer,
                result="Correct" if user_answer == q.answer else "Incorrect"
            )

        return render(request, 'result_page.html', {'score': score, 'total_questions': len(questions)})

    return redirect('quiz_page')  # If not POST, redirect to quiz page
def user_view_notification(request):
    ob=notification_table.objects.all()
    return render(request,'USER/view notification.html',{"data":ob})