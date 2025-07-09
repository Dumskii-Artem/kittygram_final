[![Main KittyGram workflow](https://github.com/Dumskii-Artem/kittygram_final/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Dumskii-Artem/kittygram_final/actions/workflows/main.yml)


#  Социальная сеть для домашних животных Kittygram

Временный адрес сайта: https://catsonlynodogs.myddns.me/
Второй сайт: https://babybear.myddns.me/

## Смысл задания
Нужно на одном сервере запустить на удаленном сервере два проекта в докер контейнерах и обеспечить обновление проектов при внесении изменении в проект, а именно, при пуше на GitHub. Это было реализовано с помощью GitHib Actions. 
В этом репозитории содержится один из двух проектов. Второй проект https://github.com/Dumskii-Artem/taski-docker.git
Задание выполнено на временной виртуальной машине, которую скоро отнимут.
В результате, при обновлении этого или второго репозитория и при пройденных тестах на виртуальной машине окажутся работающие проекты.

## Описание проекта

Данный проект представляет собой социальную сеть для домашних животных Kittygram, которая позволяет пользователям: 
- просматривать фотографии и достижения домашних животных
- регистрироваться и авторизовываться
- делиться фотографиями своих питомцев
- добавлять достижения своих питомцев

## Использованные технологии

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) 
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)  
<br>
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) 
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) 
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)  
<br>
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) 
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) 
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)  
<br>
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) 
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)


### Использовался .env файл следующего содержания
```
POSTGRES_USER=<user name>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<database name>
# Добавляем переменные для Django-проекта:
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<secret key>
DEBUG=False
ALLOWED_HOSTS=catsonlynodogs.myddns.me,89.169.164.5,127.0.0.1,localhost
USE_POSTGRESQL_OR_SQLITE=postgresql
```
файл следует поместить в корневую папку проекта 

### Использованы следующие переменные (секреты) на GitHub

```
- DOCKER_USERNAME=your_docker_hub_username
- DOCKER_PASSWORD=your_docker_hub_password
- HOST=remote_server_host_ip
- USER=your_remote_server_user
- SSH_KEY=your_ssh_private_key
- SSH_PASSPHRASE=your_ssh_pass_phrase
- TELEGRAM_TO=your_telegram_chat_id
- TELEGRAM_TOKEN=your_telegram_token_to_access_api
```

## Автор проекта
[Думский Артём](https://github.com/Dumskii-Artem) в рамках обучения
на Яндекс.Практикум по программе Python-разработчик расширенный (когорта 57+).
