import datetime
import  os
from pdf_reader import  *



folder_path='C:\\Users\\Asus\\Desktop\\COVID_19\\WHO_reports\\'
file_rename(folder_path);

country_name=convert_file_to_list('C:\\Users\\Asus\\Desktop\\COVID_19\\python_files\\country_names.txt')
print(country_name)

first_report_case_date = datetime.datetime(2020,1, 21);

empty_list_to_store_country_data=[];
for counting in country_name:
    empty_list_to_store_country_data.append([])


datas_of_country=dict(zip(country_name,empty_list_to_store_country_data))


starting_case=4;
end_case=91;

for i in range(starting_case,end_case):
    current_date=first_report_case_date+datetime.timedelta(days=i-1)
    combined_date=current_date.strftime('%Y')+current_date.strftime('%m')+current_date.strftime('%d');
    current_file_name=folder_path+combined_date+'.pdf'
    print("Current working file : " +current_file_name)
    whole_pdf_text = get_text_from_pdf(current_file_name)
    for names in country_name:
        obtained_data_from_search=find_data_by_country_name(names, whole_pdf_text)
        datas_of_country[names].append(obtained_data_from_search[1])


data_file_address='C:\\Users\\Asus\\Desktop\\COVID_19\\data.csv'
if os.path.isfile(data_file_address):
    os.remove(data_file_address)

data_file=open(data_file_address,'a');
data_file.write('DAY_NO,')
for names in country_name:
    data_file.write(names+',')

data_file.write('\n')

for data_for_day in range(0,end_case-starting_case):
    data_file.write(str(data_for_day+1)+',')
    for names in country_name:
        data_file.write(datas_of_country[names][data_for_day]+',')
    data_file.write('\n')

data_file.close()







