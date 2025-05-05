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

### 4. Установим нужные дл работы пакеты
```
apk add htop nano mc
```

### 5. Установим нужную версию Python (>3.11)
```
apk add python py3-pip sqlite3
python --version
pip3 --version
sqlite3 --version
```

### 6. Создаем виртуальное окружение
```
cd test
python -m venv env
source env/bin/activate
pip list
pip install django
django-admin --version
pip list
```

