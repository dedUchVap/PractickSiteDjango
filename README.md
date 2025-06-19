Конечно! Вот обновлённый `README.md` в Markdown для твоего Django-проекта с **готовой базой данных** и **предустановленным админом**:

---

````markdown
# 🏗️ Сайт строительной компании на Django

Готовый проект сайта для строительной компании на Django, с подключённой базой данных и учётной записью администратора.

---

## 🚀 Быстрый запуск

### 1. Клонировать репозиторий

```bash
git clone git@github.com:username/repo.git
cd repo
````

---

### 2. Создать и активировать виртуальное окружение (опционально)

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

---

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Запустить сервер

```bash
python manage.py runserver
```

Открой в браузере: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Админ-панель

* URL: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
* Логин: `admin`
* Пароль: `123`

---

## 🗃️ База данных

Проект использует **уже готовую SQLite-базу** (`db.sqlite3`), в которой:

* Есть созданный суперпользователь (`admin`)

---

## 📁 Структура проекта

```
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
├── apps/
│   └── core/
├── templates/
├── static/
└── myproject/  # Папка с настройками Django
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## ⚙️ Примечания

* Миграции не требуются — база уже собрана
* Не забудьте добавить `SECRET_KEY` в `.env` для продакшена (если нужно)

---

