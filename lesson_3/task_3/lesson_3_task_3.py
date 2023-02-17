from address import Mailing, Address

fromAddress = Address('123233', 'Челябинск', 'ул. Ленина', '23', '12')
toAddress = Address('029342', 'Санкт-Петербург', 'ул. 1905 года', '9', '98')
shipping = Mailing(fromAddress, toAddress, 1420, '029383238')

print('Отправление ' + shipping.track + ' из ' + shipping.fromPointA.city + ', ' + shipping.fromPointA.street + ', ' + shipping.fromPointA.building + '-' + shipping.fromPointA.appartment + ' в ' + shipping.toPointB.city + ', ' + shipping.toPointB.street + ', ' + shipping.toPointB.building + '-' + shipping.toPointB.appartment + '. Стоимость ' + str(shipping.cost) + ' рублей.')