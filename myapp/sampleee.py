
import csv
import base64,random
import time,datetime
# from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
# from nltk.corpus import stopwords
#

import io,random



def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text

#
# res=pdf_reader(r"C:\Users\VICTUS\PycharmProjects\jobseeker\media\Suman Parveen.pdf")
#
# print(res)
# #
# # @app.route('/predict',methods=['post'])
# # def predict():
# #     print(request.form)
# #     print(request.files)
# #
# #
# #     gend = '1'
# #     age = '18'
# #
# #     q1 = request.form['q1']
# #     q2 = request.form['q2']
# #     q3 = request.form['q3']
# #     q4 = request.form['q4']
# #     q5 = request.form['q5']
# #     print(q5,"=======================")
# #     img = request.files['file']
# #     print(img.filename,"===")
# #     # img.save(r"C:\Users\TOSHIBA\Desktop\cvanalysis\\"+img.filename.split('/')[-1])
# #     img.save(r"D:\smart_resume_selector\src\static\upload\1.pdf")
# #
# #     save_image_path = r"D:\smart_resume_selector\src\static\upload\1.pdf"
# #     resume_data = ResumeParser(save_image_path).get_extracted_data()
# #     # print(resume_data)
# #
# #     ### Resume writing recommendation
# #     resume_text = pdf_reader(save_image_path)
# #     resume_score = 0
# #     print("RT \n", resume_text)
# #
# #     if 'Objective' or 'OBJECTIVE' in resume_text:
# #         resume_score = resume_score + 20
# #         a = '[+] Awesome! You have added Objective'
# #     else:
# #         a = '[-] According to our recommendation please add your career objective, it will give your career intension to the Recruiters.'
# #
# #     if 'Declaration' in resume_text or 'DECLARATION' in resume_text:
# #         resume_score = resume_score + 20
# #         b = '[+] Awesome! You have added Declaration✍'
# #     else:
# #         b = '[-] According to our recommendation please add Declaration✍. It will give the assurance that everything written on your resume is true and fully acknowledged by you'
# #
# #     if 'Hobbies' in resume_text or 'HOBBIES' in resume_text or 'Interests' in resume_text or 'INTERESTS' in resume_text:
# #         resume_score = resume_score + 20
# #         c = '[+] Awesome! You have added your Hobbies⚽'
# #     else:
# #         c = '[-] According to our recommendation please add Hobbies⚽. It will show your persnality to the Recruiters and give the assurance that you are fit for this role or not.'
# #
# #     if 'Achievements' in resume_text or 'ACHIEVEMENTS' in resume_text:
# #         resume_score = resume_score + 20
# #         d = '[+] Awesome! You have added your Achievements🏅'
# #     else:
# #         d = '[-] According to our recommendation please add Achievements🏅. It will show that you are capable for the required position.'
# #
# #     if 'Projects' in resume_text or 'PROJECTS' in resume_text:
# #         resume_score = resume_score + 20
# #         e = '[+] Awesome! You have added your Projects👨‍💻'
# #
# #     # if 'abc' in resume_text or 'ABC' in resume_text:
# #     #     resume_score = resume_score + 20
# #     #     e = '[+] Awesome! You have added your ABC👨‍💻'
# #
# #     else:
# #         e = '[-] According to our recommendation please add Projects👨‍💻. It will show that you have done work related the required position or not.'
# #
# #     f = '**Resume Score📝**"'
# #
# #     score = 0
# #     for percent_complete in range(resume_score):
# #         score += 1
# #         time.sleep(0.1)
# #
# #     g = 'Your Resume Writing Score:' + str(score)
# #     print(" Your Resume Writing Score: ", str(score))
# #     print(a,b,c,d,e)
# #     h = '** Note: This score is calculated based on the content that you have added in your Resume. **'
# #
# #     # print(predict1(['1', '18', '5', '5', '7', '6', '5']))
# #     # pred = predict1([gend, age, q1, q2, q3, q4, q5])
# #     # print(pred)
# #
# #     data=[]
# #     row = {"task":"success","a":a,"b":b,"c":c,"d":d,"e":e,"prd":pred,"sc":str(score)}
# #     data.append(row)
# #     r = json.dumps(row)
# #     print(r)
# #     return r
# #
# #
# # app.run(host='0.0.0.0',port=5000)
#
#
#
#
#
#
