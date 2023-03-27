from CompanyPage import Company
from EmployeePage import Employee

company = Company("https://x-clients-be.onrender.com")
employee = Employee("https://x-clients-be.onrender.com")

# список компаний/создание новой компании/новый список компаний/id новой компании/список сотрудников = 0
def test_get_list_employee():
    list_company = company.get_company_list()
    new_company = company.create_company("Hard", "Logo")
    new_list_company = company.get_company_list()
    id_company = new_company["id"]
    my_params = {
        "company" : id_company
    }
    lists_employee = employee.employee_list(my_params)
    
    assert len(new_list_company) - len(list_company) == 1
    assert new_company["id"] == id_company
    assert len(lists_employee) == 0  

# новый сотрудник
def test_create_news_employee():
    first_name = "Татьяна"
    last_name = "Мохначева"
    middle_name = "Вячеславовна"

    list_company = company.create_company("Hard", "Logo")
    id_company = list_company["id"]
    my_params = {
        "company": id_company
    }
    new_employee = employee.create_employee(id_company, first_name, last_name, middle_name)
    list_employee = employee.employee_list(my_params)
    assert len(new_employee) == 1
    assert list_employee[0]["firstName"] == first_name
    assert list_employee[0]["lastName"] == last_name
    assert list_employee[0]["middleName"] == middle_name

# id сотрудника
def test_get_employee_id():
    list_company = company.get_company_list()
    id_company = list_company[-1]["id"]
    my_params = {
        "company": id_company
    }
    lists_employee = employee.employee_list(my_params)
    first_employee = lists_employee[-1]["id"]
    _employee = employee.get_employee_id(first_employee)
    assert _employee["companyId"] == id_company
    assert len(_employee) == 11


def test_change_info_employee():
    first_name = "Татьяна"
    last_name = "Мохначева"
    middle_name = "Вячеславовна"
    new_info = {
        "lastName": "Немохначева",
        "email": "test@test.com",
        "isActive": True
    }

    list_company = company.create_company("Sber", "Tech")
    id_company = list_company["id"]
    new_employee = employee.create_employee(id_company, first_name, last_name, middle_name)

    id_employee = new_employee["id"]
    new_info_employee = employee.change_info_employee(id_employee, new_info)
    assert new_info_employee["email"] == new_info["email"]
    assert new_info_employee["id"] == id_employee