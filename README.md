# Watcher of Friends Online

Скрипт отображает список друзей ВКонтакте, которые подключены к сети в данный момент.

# Предварительные настройки

- Создать конфигурационный файл приложения `.env`:
```
cp .env.example .env
```
- Создать [приложение](https://vk.com/editapp?act=create) ВКонтакте. (тип приложения - **standalone**)
- Из настроек приложения ВК скопировать **ID приложения** и добавить в `.env`:
```
APP_ID=123456
```
- Установить и запустить [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) для Python
- Установить дополнительные пакеты:
```
pip install -r requirements.txt
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора **Python** версии **3.5**.

**Запуск на Linux**

```bash
$ python vk_friends_online # или python3, в зависимости от настроек системы

# скрипт запросит логин/пароль VK для авторизации
Enter your VK login:
Enter your VK password:

# при успешном выполнении отобразит список друзей, которые находятся в сети
Users online:
Иван Иванов
Петр Петров
Андрей Андреев

# если введены неправиные логин/пароль/app_id выведет сообщение об ошибке
Failed to connect to VK. Make sure you have entered the correct login/password.
```

Запуск на **Windows** происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
