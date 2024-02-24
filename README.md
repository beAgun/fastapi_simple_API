<<<<<<< HEAD
# Описание системы

Реализована система учёта и анализа данных, поступающих с условного устройства. Полученные данные привязываются к временной метке и устройству, с которого пришли данные, 
и сохраняются в БД. Набор данных используется для дальнейшего анализа.
<br>
Схема БД:

![drawSQL-task-export-2024-02-24](https://github.com/beAgun/fastapi_simple_API/assets/140337252/1da64ac2-f30e-4e02-a105-b395df9e712e)


# Требования, которым удовлетворяет система

## Функциональные
<ul>
  <li>
    В системе реализован сбор статистики с устройства по его идентификатору (формат получаемой статистики - <strong>json</strong>). <br>
    Для этого реализованы методы:
      <ul>
        <li> <strong>Add Device</strong> для добавления устройства<br>
          <img style='height: 70px; width: auto;' src='https://github.com/beAgun/fastapi_simple_API/assets/140337252/fba1f682-07a4-4875-b8e9-3feb5fa68b76'>
        </li>
        <li> <strong>Add Data</strong> для сбора статистики с устройства<br>
          <img style='height: 70px; width: auto;' src='https://github.com/beAgun/fastapi_simple_API/assets/140337252/565415f3-3492-4a6f-918b-b6dc62d97204'>
        </li>
      </ul>
  </li>
  
  <li>
    В системе реализован анализ собранной статистики с устройства за определённый период и за всё время.<br>
    Для этого реализованы методы:
      <ul>
        <li> <strong>Get Data</strong> для получения анализа данных на определённом устройстве за всё время<br>
          <img style='height: 70px; width: auto;' src='https://github.com/beAgun/fastapi_simple_API/assets/140337252/ae8e6f4a-1ad7-4057-a05e-48106aa4edf2'>
        </li>
        <li> <strong>Get Data Certain Period</strong> для получения анализа данных на определённом устройстве за определённый период<br>
          <img style='height: 70px; width: auto;' src='https://github.com/beAgun/fastapi_simple_API/assets/140337252/99f453be-88ab-4868-b788-f8ae01e00401'>
        </li>
      </ul>
  </li>
  
  <li>
    Результатами анализа являются числовые характеристики величины:
    <ul>
      <li>минимальное значение</li>
      <li>максимальное значение</li>
      <li>количество</li>
      <li>сумма</li>
      <li>медиана</li>
    </ul>
  </li>
    
  <li>
    Система поддерживает добавление пользователей устройств.<br>
    Для этого реализованы методы:
      <ul>
        <li> <strong>Add User</strong> для добавления нового пользователя<br>
          <img style='height: 70px; width: auto;' src='https://github.com/beAgun/fastapi_simple_API/assets/140337252/7cecd0b1-34ab-4e31-8192-7c6422ac8d45'>
        </li>
        <li> <strong>Add Device User</strong> для связывания пользователя и устройства<br>
          <img style='height: 70px; width: auto;' src='https://github.com/beAgun/fastapi_simple_API/assets/140337252/9cc55245-8221-49bc-9858-d89781beaa98'>
        </li>
      </ul>
  </li>
  
  <li>
    В системе реализован функционал получения анализа показаний устройств по идентификатору пользователя:
    <ul>
      <li>агрегированные результаты для всех устройств</li>
      <li>для каждого устройства отдельно</li>
    </ul>
    Для этого реализованы методы:
      <ul>
        <li> <strong>Get User Data</strong> с параметром <strong>user_id</strong> и необязательным параметром <strong>device_id</strong><br>
          <img style='height: 70px; width: auto;' src='https://github.com/beAgun/fastapi_simple_API/assets/140337252/0872347b-0578-4141-8264-c3e3935534f6'>
        </li>
      </ul>
      </li>
    </ul>
  </li>
</ul>

## Нефункциональные
<ul>
  <li>Архитектура <strong>REST</strong></li>
  <li>Фреймворк реализации сервиса <strong>FastApi</strong>
  <li>Собранные данные хранятся в БД <strong>sqlite</strong>
  <li>Подготовлен <strong>Dockerfile</strong>
</ul>
=======
"# fastapi-test" 
>>>>>>> 033b090 (commit)
