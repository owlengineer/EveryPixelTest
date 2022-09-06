## Демон-трекер для EveryPixel

Ход мыслей
0. Взял заготовку с докерфайлом и компоуз-файлом для масштабирования
1. Решить ручными проверками через listdir наличия файлов с расширением картинок (отбросил)
2. Использовать готовое решение watchdog, судя по докам (https://pypi.org/project/watchdog/) хорошо параллелится и удобные ивент-трекеры есть

В итоге:
1. while true с демоном-слушателем в отдельном потоке (watchdog из коробки), таймаут -- 1 сек 
2. Docker (и docker-compose) для масштабирования и универсальности, вывел в параметры входную (где файлы трекаюся) и выходную (куда сохраняется) директории. 
3. requirements подгружает все зависимости (команда в докерфайле)

*Какие отрицательные эффекты в приведенной задаче случайно могут получиться?*

- При распараллеливании коллизии могут быть (когда один и тот же файл берется несколькими потоками). Решается созданием общей очереди -- 1 поток дергает файловую систему и кладет в очередь путь к картинке, 10 потоков обработки слушают очередь и берут оттуда файлы.

## Deploy

```docker-compose up```

## Демо

https://drive.google.com/file/d/11WquHzeLHO0MKpiAIU5v9GD5dzwwqoiU/view?usp=sharing
