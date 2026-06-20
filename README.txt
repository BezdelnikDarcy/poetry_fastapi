alembic revision --autogenerate -m "text commit" #Создание миграции
alembic upgrade head #Применение миграции
uvicorn src.main:app --port %%%% --reload