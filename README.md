# Foodgram

[![Foodgram Workflow](https://github.com/nnnastt/foodgram/actions/workflows/main.yml/badge.svg)](https://github.com/nnnastt/foodgram/actions/workflows/main.yml)
Сервис для публикации рецептов: пользователи публикуют рецепты, подписываются на других, добавляют в «Избранное» и скачивают список покупок.

## Демо

- **Сайт:** https://foodgram-yp-2026.duckdns.org
- **Админка:** https://foodgram-yp-2026.duckdns.org/admin/

## Стек

- **Backend:** Python 3.12, Django 5.1, DRF, Djoser, PostgreSQL, Gunicorn
- **Frontend:** React, Node.js 18
- **Инфра:** Docker, Docker Compose, Nginx, GitHub Actions

## Запуск локально

```bash
git clone https://github.com/nnnastt/foodgram.git
cd foodgram/infra
cp .env.example .env

docker compose -f docker-compose.yml up -d --build

docker compose -f docker-compose.yml exec backend python manage.py migrate
docker compose -f docker-compose.yml exec backend python manage.py load_ingredients
docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
docker compose -f docker-compose.yml exec backend python manage.py collectstatic --noinput
```

## Переменные `.env`

POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_HOST=db
DB_PORT=5432
DJANGO_SECRET_KEY=а тут секрет
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,foodgram-yp-2026.duckdns.org,158.160.207.178
DJANGO_CORS_ALLOWED_ORIGINS=https://foodgram-yp-2026.duckdns.org
DJANGO_CSRF_TRUSTED_ORIGINS=https://foodgram-yp-2026.duckdns.org


**Генерация ключа:**

```bash
python3 -c "import secrets; print('django-insecure-' + secrets.token_urlsafe(50))"
```

## Деплой

```bash
git add .
git commit -m "Название коммита"
git push
```

Workflow сам:

1. Прогонит тесты
2. Соберёт образы
3. Запушит на Docker Hub
4. Задеплоит на сервер
5. Отправит уведомление в Telegram



## Автор
https://github.com/nnnastt