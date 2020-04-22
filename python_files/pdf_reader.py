import PyPDF2
import  os
from KMP import *


def get_text_from_pdf(file_name):
    pdfFileObj = open(file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    whole_pdf_text = ""
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        whole_pdf_text = whole_pdf_text + pageObj.extractText();
    pdfFileObj.close()
    return whole_pdf_text;



def convert_file_to_list(file_name):
    file=open(file_name,'r')
    list=[]
    for each_line in file:
        list.append(each_line[0:len(each_line)-1]) #so that new line is not entered
    return list


def file_rename(folder_path):
    fileNames=os.listdir(folder_path)
    for filename in fileNames:
        current_file_name=folder_path+'\\'+filename
        file_name_to_be_renamed='';
        for i in range(0,len(filename)):
            if filename[i]>='0' and filename[i]<='9':
                file_name_to_be_renamed=file_name_to_be_renamed+filename[i]
            else:
                break
        file_name_to_be_renamed=folder_path+file_name_to_be_renamed+'.pdf';
        os.rename(current_file_name,file_name_to_be_renamed)
    return





def find_data_by_country_name(country_name,whole_pdf_text):
    lenght_of_the_pdf = len(whole_pdf_text)
    expected_data_type_founded=0;
    current_posiotion=0;
    while expected_data_type_founded==0 and current_posiotion<lenght_of_the_pdf:
        location_of_the_country_name=KMPSearch(country_name, whole_pdf_text[current_posiotion:lenght_of_the_pdf])
        current_posiotion=location_of_the_country_name+current_posiotion;
        data=[];

        if current_posiotion>lenght_of_the_pdf:
            print("DATA NOT FOUND FOR "+ country_name);
        else:
            for data_type in range(0,2):
                current_string='';
                while current_posiotion < lenght_of_the_pdf and whole_pdf_text[current_posiotion]!='\n'and whole_pdf_text[current_posiotion]!=' 'and whole_pdf_text[current_posiotion]!='\t':
                    current_string=current_string+whole_pdf_text[current_posiotion]
                    current_posiotion=current_posiotion+1
                while current_posiotion < lenght_of_the_pdf and (whole_pdf_text[current_posiotion]=='\n'or whole_pdf_text[current_posiotion]==' 'or whole_pdf_text[current_posiotion]=='\t'):
                    current_posiotion=current_posiotion+1;
                data.append(current_string)
        if len(data)==0:
            data = [country_name, '0']
        if data[1].isnumeric(): #checking type of data given because country name can come other places without data
            expected_data_type_founded=1



    return  data











