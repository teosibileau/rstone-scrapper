# A (rocking) example of how to use Django (rocking) ORM to store in a db results from a Scrapy (rocking) spider 

As an example, i set up this project to scrap all over rolling stone lists/rankings and store them in a relational db with proper data models
 
## Why

Because when people denies you access to datastores, it's super fun and useful to steal from them.

## Non pip requirements

+ Python 2.7
+ pip
+ virtualenv
+ Some messaging service compatible with celery, i use [redis](http://redis.io)
+ a db compatible with django, i use sqlite 3 in dev, postgres or mongodb in prod. If you are not familiar how django manages dbs go [here](https://docs.djangoproject.com/en/1.3/ref/databases/)

## Installation

Clone project and install requirements in virtualenv

```bash
git clone git://github.com/drkloc/rstone_scrapper.git
cd rstone_scrapper
# initialize virtualenv
virtualenv . --distribute
# activate enviroment
source bin/activate
# install dependencies
pip install -r requirements.txt
# install django
cd rstone
python manage.py syncdb
python manage.py migrate
```

Any settings override (Database config, broker message config, etc) are conveniently made inside **settings_local.py**. Just copy the demo file:

```bash
cp settings_local_demo.py settings_local.py
```

and start customizing whatever you want/need.

## Start redis-server and celery deamon

```bash
redis-servergit ad
```

```bash
python manage.py celeryd
```

## Initialization

```bash
scrapy runspider scrap.py
```

## That's about it, enjoy.