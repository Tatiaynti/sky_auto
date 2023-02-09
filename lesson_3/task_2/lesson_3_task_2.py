from smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Samsung', 'Galaxy S', '+79132939293'))
catalog.append(Smartphone('Xiaomi', 'Mi 9', '+79138939294'))
catalog.append(Smartphone('Nokia', '3310', '+79154244293'))
catalog.append(Smartphone('Siemens', 'A50', '+79014535444'))
catalog.append(Smartphone('Oppo', 'A54', '+79253459293'))

for item in catalog:
    print(item.brand + ' - ' + item.model + '. ' + item.phone_number)