# testParleto
Test Tast from www.parleto.io

Процессор / память - VIA Eden Processor 1000MHz (32бит) / 0,5 Гб DDR2

Версия AlpineLinux / Версия ядра Linux - 3.21.3 / 6.12.13-0-lts

Сервер имеет локальный адрес - 192.168.8.193/24

Работаем от root

Для коммитов в постоянную память используем команду - lbu commit


### 1. Впишем новые репозитории для обновления пакетов
```
vi /etc/apk/repositories
	I
	http://dl-cdn.alpinelinux.org/alpine/v3.21/main
	http://dl-cdn.alpinelinux.org/alpine/v3.21/community
	Esc
	:wq
 ```

### 2. Обновим систему
```
apk update
apk upgrade
```

### 3. Впишем доп.папку для коммитов (эта папка по-умолчанию не включена в список для коммита)
```
lbu include /etc/init.d/
```

### 4. Установим нужные пакеты для работы
```
apk add htop nano mc curl git
```

### 5. Установим нужные пакеты
```
apk add python py3-pip sqlite3
python --version (>3.11)
pip3 --version
sqlite3 --version (>3)
```

### 6. Установим Adminer для контроля (http://localhost:8888/adminer.php)
```
apk add php php-cli php-session php-mysqli php-pdo php-pdo_mysql php-pdo_sqlite php-json php-openssl php-mbstring
mkdir -p /var/www/adminer
cd /var/www/adminer
curl -o adminer.php https://www.adminer.org/latest.php
php -S 0.0.0.0:8888 -t .
```

### 7. Настроим автозагрузку для Adminer

cd /etc/init.d

nano /etc/init.d/adminer

```
#!/sbin/openrc-run

description="Adminer PHP Server"

depend() {
    need net
}

start() {
    ebegin "Starting Adminer"
    start-stop-daemon --start --background --exec /usr/bin/php -- -S 0.0.0.0:8888 -t /var/www/adminer
    eend $?
}

stop() {
    ebegin "Stopping Adminer"
    start-stop-daemon --stop --exec /usr/bin/php
    eend $?
}
```
Запускаем:
```
chmod +x /etc/init.d/adminer
rc-update add adminer default
rc-service adminer start
lbu commit
reboot
```

http://192.168.4.155:8888/adminer.php

### 8. Создаем виртуальное окружение
```
cd test
python -m venv env
source env/bin/activate
pip list
pip install django (5.2)
python -m django --version
pip list
```

Будут установлены следующие пекеты:
```
asgiref  3.8.1
Django   5.2
pip      25.0.1
sqlparse 0.5.3
```

### 9. Подготовка проекта
```
python manage.py migrate
python example_init.py
```
