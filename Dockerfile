FROM python:3.7
MAINTAINER Evgeny Im <evgenyim6456@gmail.com>

# устанавливаем параметры сборки
RUN apt-get update
RUN apt-get install -y ffmpeg

# задаем рабочую директорию для контейнера
WORKDIR  /usr/src/JBAudio

# устанавливаем зависимости python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копируем все файлы из корня проекта в рабочую директорию
COPY src/ ./src/
COPY resources/ ./resources/
#RUN ls -la /src/*

# запускаем приложение Python
CMD ["python3", "src/main.py"]