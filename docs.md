# Clinic Appointments


## 1. Архитектура

[ FastAPI app ]\
   |\
   |---> [models.py] (Appointment модель)\
   |---> [schemas.py] (Pydantic input/output)\
   |---> [crud.py] (create_appointment, get_appointment)\
   |---> [database.py] (session + engine)

## 2. ER-диаграмма

appointments
- id (PK)
- patient_name (varchar)
- doctor_id (int)
- start_time (datetime)
- created_at (datetime)\
UNIQUE (doctor_id, start_time)

## 3. Activity-диаграмма

https://miro.com/app/board/uXjVIgOFsTU=/?share_link_id=892957116023


## 4. Документ бизнес-процесса

https://miro.com/app/board/uXjVIgXH0Xs=/?share_link_id=391194102766


## 5. Проектирование → реализация

1. Определил бизнес-требования (запись к врачу без пересечений).
2. Нарисовал ER-диаграмму.
3. Создал FastAPI проект.
4. Написал CRUD и эндпойнты.
5. Подготовил тесты.
6. Добавил Dockerfile, docker-compose и CI/CD.


