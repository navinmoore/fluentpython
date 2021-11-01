# Celery

## 运行worker

运行worker：celery -A celery_app worker -l INFO
 -A 后面指APP的位置，及这行代码的位置：app = Celery('my_task', broker=broker, backend=backend) ,
 -l 后面试日志级别默认warning。

## 定时任务

运行beat：celery beat -A celery_app -l INFO 定时把任务提交到消息队列中

## 组合命令

celery -A celery_app worker -B

## 分别启动
```
celery -A tasks worker -l info -n workerA.%h -Q for_task_A // for_task_A 是Queue  默认的名字celery
```


# Django

## 运行worker （组合命令）
celery -A proj worker -B      

# Flower

## 安装
```
pip install flower
```

## 后台运行
```
celery multi start w1 -A proj -l info
```

```
celery  multi restart w1 -A proj -l info
```

```
celery multi stop w1 -A proj -l info
```

stop 命令是异步的，所以不会等待职程（Worker）关闭。可以通过 stopwait 命令进行停止运行，可以保证在退出之前完成当前正在执行的任务：
```
celery multi stopwait w1 -A proj -l info
```

