import pytest
from EmployeePage import Employee
from EmployeeTable import EmployeeTable
from faker import Faker

driver = Employee('https://x-clients-be.onrender.com/employee')
db = EmployeeTable("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")
fake = Faker()                       

# Тест списков сотрудников
def test_positive_get_list_of_employees():
    request_text = "select * from employee e where \"companyId\" =:curent_id"
    path = '?company='
    name = fake.name()
    descr = fake.text(20)
    id = driver.create_company(name, descr)
    resp_api_json = driver.employee_get(path, id)[0]
    resp_status = driver.employee_get(path, id)[1]
    db_result = db.get_any_db_request(id, request_text)
    assert len(resp_api_json) == len(db_result)
    assert resp_status == 200

# Тест создания нового сотрудника
def test_valid_create_new_employee():
    company_id = driver.create_company(fake.name(), fake.text(20))
    request_text = "select first_name, last_name, middle_name, phone, avatar_url, \"isActive\", id from employee e where id = :curent_id "
    api_resp_first_name = fake.first_name()
    api_resp_last_name = fake.last_name()
    api_resp_middle_name = fake.first_name()
    api_resp_phone = fake.phone_number()
    api_resp_url = fake.url()
    api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
    api_resp_new_worker_id = api_resp_new_worker[0]['id']
    new_db_resp = db.get_any_db_request(api_resp_new_worker_id, request_text)
    
    assert api_resp_new_worker_id == new_db_resp[0]["id"]
    assert api_resp_first_name == new_db_resp[0]["first_name"] 
    assert api_resp_last_name == new_db_resp[0]["last_name"]
    assert api_resp_middle_name == new_db_resp[0]["middle_name"]
    assert api_resp_phone == new_db_resp[0]["phone"]
    assert api_resp_url == new_db_resp[0]["avatar_url"]
    assert api_resp_new_worker[1]== 201

#Невалидное создание
@pytest.mark.xfail()  
def test_invalid_create():
    company_id = driver.create_company(fake.name(), fake.text(20))
    first_name = fake.first_name()
    last_name = fake.last_name()
    middle_name = fake.first_name()
    phone = fake.phone_number()
    url = fake.url()
    godzilla = fake.text(10)
    date = fake.date_time()
    
    nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url, godzilla, date)
    assert nem_worker[1]== 201   

#Тест запроса нового сотрудника
def test_valid_check_emloyee():
    company_id = driver.create_company(fake.name(), fake.text(20))
    api_resp_first_name = fake.first_name()
    api_resp_last_name = fake.last_name()
    api_resp_middle_name = fake.first_name()
    api_resp_phone = fake.phone_number()
    api_resp_url = fake.url()
    api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
    curent_id =  api_resp_new_worker[0]['id']
    path = '/'
    request_text = "select * from employee e where id = :curent_id "
    resp_status = driver.employee_get(path, curent_id)[1]
    api_resp_id = driver.employee_get(path, curent_id)[0]["id"]
    api_resp_isActive = driver.employee_get(path, curent_id)[0]["isActive"]
    api_resp_first_name = driver.employee_get(path, curent_id)[0]["firstName"]
    api_resp_last_name = driver.employee_get(path, curent_id)[0]["lastName"]
    api_resp_middle_name = driver.employee_get(path, curent_id)[0]["middleName"]
    api_resp_phone = driver.employee_get(path, curent_id)[0]["phone"]
    api_resp_email = driver.employee_get(path, curent_id)[0]["email"]
    api_resp_url = driver.employee_get(path, curent_id)[0]["avatar_url"]
    api_resp_company_id = driver.employee_get(path, curent_id)[0]["companyId"]

    new_db_resp = db.get_any_db_request(curent_id, request_text)
    
    assert resp_status == 200
    assert api_resp_id == new_db_resp[0]["id"]
    assert api_resp_isActive == new_db_resp[0]["isActive"]
    assert api_resp_first_name == new_db_resp[0]["first_name"] 
    assert api_resp_last_name == new_db_resp[0]["last_name"]
    assert api_resp_middle_name == new_db_resp[0]["middle_name"]
    assert api_resp_phone == new_db_resp[0]["phone"]
    assert api_resp_email == new_db_resp[0]["email"]
    assert api_resp_url == new_db_resp[0]["avatar_url"]
    assert api_resp_company_id == new_db_resp[0]["companyId"]

#Тест с невалидным id
@pytest.mark.xfail() 
def test_invalid_id_check():
    path = '/'
    new_id = 897878
    resp_status = driver.employee_get(path, new_id)[1]
    assert resp_status == 200    

#Тест редактирования сотрудника
def test_valid_change_employee():
    company_id = driver.create_company(fake.name(), fake.text(20))
    api_resp_first_name = fake.first_name()
    api_resp_last_name = fake.last_name()
    api_resp_middle_name = fake.first_name()
    api_resp_phone = fake.phone_number()
    api_resp_url = fake.url()
    api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
    curent_id =  api_resp_new_worker[0]['id']

    lastName = fake.first_name()
    email= fake.email()
    url = fake.url()
    isActive = True
    request_text = "select * from employee e where id = :curent_id "
    resp = driver.change_info_employee(curent_id, lastName, email, url, isActive)
    api_resp_status = resp[1]
    api_resp_id = resp[0]["id"]
    api_resp_email = resp[0]["email"]
    api_resp_url = resp[0]["url"]
    api_resp_isActive = resp[0]["isActive"]

    db_resp = db.get_any_db_request(curent_id, request_text)
    assert api_resp_id == db_resp[0]["id"]
    assert api_resp_email == db_resp[0]["email"]
    assert api_resp_url == db_resp[0]["avatar_url"]
    assert api_resp_isActive == db_resp[0]["isActive"]
    assert api_resp_status == 200

#Тест с некорректным параметром
@pytest.mark.xfail() 
def test_invalid_change_employee():
    company_id = driver.create_company(fake.name(), fake.text(20))
    api_resp_first_name = fake.first_name()
    api_resp_last_name = fake.last_name()
    api_resp_middle_name = fake.first_name()
    api_resp_phone = fake.phone_number()
    api_resp_url = fake.url()
    api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
    new_id =  api_resp_new_worker[0]['id']
    
    lastName = fake.last_name()
    email= fake.email()
    url = fake.url()
    isActive = 'string'

    resp = driver.change_info_employee(new_id, lastName, email, url, isActive)
    resp_status = resp[1]
    resp_id = resp[0]["id"]
    resp_email = resp[0]["email"]
    resp_url = resp[0]["url"]
    resp_isActive = resp[0]["isActive"]

    assert resp_id == new_id
    assert resp_email == email
    assert resp_url == url
    assert resp_isActive == isActive
    assert resp_status == 200


#Тест на редактирование с некорректным id
@pytest.mark.xfail() 
def test_invalid_change_worker_note_3():
    lastName = fake.last_name()
    email= fake.email()
    url = fake.url()
    isActive = True
    
    new_id = 20002020202

    resp = driver.change_info_employee(new_id, lastName, email, url, isActive)
    resp_status = resp[1]
    assert resp_status == 200