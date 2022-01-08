//ОБРАЗЫ
    docker images	                                //Список локальных Images     
    docker commit 5267e21d140  newimage_v2:latest	//Создать Image с именем newimage_v2:latest из контейнера с ID 5267e21d140
    docker build -t my-python-app_1003 .            //собрать образ


//КОНТЕЙНЕР
    docker ps	    запущенные
    docker ps -a	ВСЕ

//ЗАПУСК
docker run -d -p 12345:80 nginx
    //режимы запуска
    -it                                                         //- интерактивно (по умолчанию)
    -d                                                          //- detach без вывода логов
    -p 12345:80 (Переназначение на 1234 внеш. с 80 внутр.)      //порты
    --rm                                                        //можно сразу удалить, чтобы не засорять контейнеры
	docker run -it --network host ocr_pak						//проброс сети

docker run -t -i ocr_pak /bin/bash

//win запуск
docker run -d --name tg2 -v D:\temp\db:/home/db tgfinance
    -v D:\temp\db:/home/db (проброс папки "D:\temp\db" в "/home/db")

//УДАЛЕНИЕ
    docker --rm hello-world       //сначала удаляем контейнер, т.к.  контейнер использует образ
    docker --rmi hello-world      //потом образ

//сети
docker network ls 					//все сети докера
docker network inspect bridge		//информация по сети (bridge - создается по умолчанию)


//ссылки на хорошие материалы
https://habr.com/ru/company/ruvds/blog/441574/
https://habr.com/ru/company/ruvds/blog/440660/
https://habr.com/ru/post/310460/
https://github.com/alexey-goloburdin/telegram-finance-bot (пример)

```
docker build -t tgfinance ./
docker run -d --name tg -v / D:\temp\db:/home/db tgfinance

--network host

//win запуск
docker run -d --name tg2 -v D:\temp\db:/home/db tgfinance

```