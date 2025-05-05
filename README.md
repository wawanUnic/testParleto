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
apk add htop nano mc curl
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

nano /etc/systemd/system/phpserver.service

```
[Unit]
Description=PHP Built-in Server
After=network.target

[Service]
ExecStart=/usr/bin/php -S 0.0.0.0:8888 -t /var/www/adminer
Restart=always
User=www-data
Group=www-data

[Install]
WantedBy=multi-user.target
```

systemctl enable phpserver

systemctl start phpserver


### 8. Создаем виртуальное окружение
```
cd test
python -m venv env
source env/bin/activate
pip list
pip install django
django-admin --version
pip list
```

