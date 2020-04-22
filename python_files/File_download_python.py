import wget
import datetime
import os

first_report_case_date = datetime.datetime(2020,1, 21);
folder_path='C:\\Users\\Asus\\Desktop\\COVID_19\\WHO_reports\\'
number_of_total_report=90;
start_case=1;
current_date=first_report_case_date+datetime.timedelta(days=start_case-1)
list=[]
file_not_downloaded=['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '74']
for x in file_not_downloaded:
    i=int(x);
    current_date=first_report_case_date+datetime.timedelta(days=i-1)
    combined_date=current_date.strftime('%Y')+current_date.strftime('%m')+current_date.strftime('%d')
    file_name=combined_date+'-sitrep-'+str(i)+'-ncov.pdf'
    url_link='https://www.who.int/docs/default-source/coronaviruse/situation-reports/'+file_name
    file_path=folder_path+file_name
    if os.path.isfile(file_path):
        os.remove(file_path)
    print('\n downloading case report number :'+ str(i)+'\n' + 'URL:'+url_link)
    try:
        wget.download(url_link,file_path)
    except:
        list.append(str(i))


print(list)

#https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200126-sitrep-6-2019--ncov.pdf
#https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200323-sitrep-63-covid-19.pdf?sfvrsn=b617302d_4