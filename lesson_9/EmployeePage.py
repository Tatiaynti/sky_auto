import requests

class Employee:
    def __init__(self, url):
        self.url = url 
    
    def get_token(self, user =  'roxy', password = 'animal-fairy'):  
        creds = {
        'username': user,
        'password': password
        }
        resp = requests.post("https://x-clients-be.onrender.com/auth/login", json=creds)
        return resp.json()["userToken"]
    
    def employee_get(self, path, id):  
       status = requests.get(self.url+path+ str(id)).status_code
       body =  requests.get(self.url+path+ str(id)).json()
       return [body, status]
    
    #Создание новой компании 
    def create_company(self, name, description):
        my_json = {
            "name": name,
            "description": description
        }
        my_headers={}
        my_headers["x-client-token"] = self.get_token() 
        resp = requests.post(url="https://x-clients-be.onrender.com/company", headers=my_headers, json=my_json)      
        return resp.json()["id"]

    #Создать нового сотрудника
    def employee_post(self, companyId, firstName, lastName, middleName, phone, url):
        new_employee = {        
        "companyId": companyId,
        "firstName": firstName,
        "lastName": lastName,
        "middleName": middleName,
        "phone": phone,
        "url": url
        }
        my_headers={}
        my_headers["x-client-token"] = self.get_token() 
        resp = requests.post(self.url, headers=my_headers, json=new_employee)  
        self.id_employee = resp.json()['id']
        return [resp.json(), resp.status_code]

    def change_info_employee(self, employee_id, lastName, email, url, isActive):
        redact_worker = {
         "lastName": lastName,
         "email": email,
         "url": url,
         "isActive": isActive
        }
        my_headers={}
        my_headers["x-client-token"] = self.get_token() 
        resp = requests.patch(self.url + "/"+str(employee_id), json=redact_worker, headers=my_headers)
        resp_json = resp.json()
        resp_status = resp.status_code
        return [resp_json, resp_status] 
    