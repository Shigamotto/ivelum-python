# Ivelum Python challenge

Этот проет появился на задачу поставленную https://github.com/ivelum/job/blob/master/challenges/python.md

### Hacker™ News proxy
Реализовать простой http-прокси-сервер, запускаемый локально, который показывает содержимое страниц Hacker News. Прокси должен модицифировать текст на страницах следующим образом: после каждого слова из шести букв должен стоять значок «™». Пример™:

Исходный текст: https://news.ycombinator.com/item?id=13713480

> The visual description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked it out.
> 
> Basically, each PDF contains a single large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format is
merely incidental here. Extracting out the two images shows two
JPG files with different contents (but different SHA-1 hashes
since the necessary prefix is missing). Each PDF consists of a
common prefix (which contains the PDF header, JPG stream
descriptor and some JPG headers), and a common suffix (containing
image data and PDF display commands).

Через ваш прокси™: http://127.0.0.1:8232/item?id=13713480

> The visual™ description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked™ it out.
>
> Basically, each PDF contains a single™ large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format™ is
merely™ incidental here. Extracting out the two images™ shows two
JPG files with different contents (but different SHA-1 hashes™
since the necessary prefix™ is missing). Each PDF consists of a
common™ prefix™ (which contains the PDF header™, JPG stream™
descriptor and some JPG headers), and a common™ suffix™ (containing
image data and PDF display commands).

Условия:

- Python™ 3.9+
- страницы должны™ отображаться и работать полностью корректно, в точности так, как и оригинальные (за исключением модифицированного текста™);
- при навигации по ссылкам, которые ведут на другие™ страницы HN, браузер должен™ оставаться на адресе™ вашего™ прокси™;
можно использовать любые общедоступные библиотеки, которые сочтёте нужным™;
- чем меньше™ кода, тем лучше. PEP8 — обязательно;
- если в условиях вам не хватает каких-то данных™, опирайтесь на здравый смысл.
- Если задачу™ удалось сделать быстро™, и у вас еще остался энтузиазм - как насчет™ написания тестов™?

Задача не сложная, но показалась мне интересной.

## Для запуска проекта необходимо

Склонруйте себе проект.

Выполните в терминале:
```shell
docker compose up -d
```

Для просмотра логов замен, выставите значение `DJ_LOGGER_HACKER_NEWS_RULES_RENDERER_LEVEL=DEBUG`.

Для остановки запущенного проекта выполните
```shell
docker compose down
```

Затем открыть в терминале http://127.0.0.1:8232/

## Для созданя среды разработки

Склонруйте себе проект.

Произведите установку пакетов:
- Install https://taskfile.dev
- Install https://github.com/pyenv/pyenv
- Install https://github.com/pyenv/pyenv-virtualenv
- Install https://python-poetry.org

Выполните в терминале:
```shell
task setup:python
task poetry:install
```

### Вспомогательные команды

- `task test` - запуск тестов
- `task format` - форматирование кода
- `task lint` - запуск линтеров

