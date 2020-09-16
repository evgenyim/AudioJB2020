# AudioJB2020
Это приложение, которое умеет делать некоторые преобразования с аудиозаписями.
Использование:

  1. Склонируйте репозиторий
  
  2. Можно запускать с помощью 
  ```
  python3 ./src/main.py
  ```
  Или через docker образ.
  
  Чтобы запустить через docker, соберите образ используя 
  ```
  docker build -t <name> .
  ```
  А затем запустите с помощью 
  ```
  docker run -v <path to clonned repository>:/usr/src/JBAudio -t -i <name>
  ```
  Все файлы созданные в docker контейнере будут и в вашей системе в папке resources
  
  Приложение работает со всеми файлами в папке resources, сохраняет файлы туда же
  
  Возможные комманды:
  ```
  Commands:
          help
               show help
          show
               shows resources
          merge <output file> <file1> <file2> ...
               merge files and place result to <output file>
          cut <file> [<start>;<finish>] [<start>;<finish>] ...
               split file to intervals, which would be saved automatically
          reverse <file> <output file>
               reverse <file>
          exit
               exit form app
  ```
