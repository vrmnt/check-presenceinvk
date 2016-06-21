# Парсинг статуса(Online, Offline, Deleted, Absence) юзера Вконтакте #

Используются python3.4, requests, BeautifulSoup4.
Оптимизированно под unix.

### Входные данные ###
На вход дается идентификатор пользователя в чистом виде без 'id' с начала и символов: '307993310', 307993310, '0124', 0124.
### Способы запуска ###
Вы можете передать сразу же параметр:
input[1]: python3 vk.py 307339910
А можете так:
input[1]: python3 vk.py
input[2]: 307339910
output[3]: "Your status."
### Результат ###
Выдается статус(Online, Offline, Deleted, Absence) юзера. Данные вывода имеют тип str.
Примеры данных вывода: 'Online', 'Был в сети 1 час назад', 'The user is absent', 'Account has been deleted or does not exist', 'Not enough permission to access', 'Invalid identifier'.
### Возможные, частые ошибки ###
* Пользователь может запретить просматривать свою страницу из всемирной веб-паутины(в таком случае будет выведен ответ: "Not enough permission to access.")
* При вводе идентификатора стандартного вида(id[any number]) 'id' не пишется. Правильное написание: 'any number'.