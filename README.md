# flask-docker qucikstart

## quick start


```
first: get docker and docker-compose
then: run
docker-compose up
```

Then you can see The Hello world from docker in localhost:80

## more 

this quickstart is for lazy man like me. I get tired of flask's  stupid design, when create a falsk-project, flask will not support Blueprint template option, as also, it make use of the docker's convenience. This integrate 

```
Flask-Login
Flask-Migrate
Flask-SQLAlchemy
```

Use mysql. you can change it easily if you like.

in docker, this has also something interesting, I set `net.core.somaxconn` to 1024 to support more connections.

## production

In production env, i suggest to open nginx in dockerfile-web(Don't forget write a nginx-conf file) , and set up uwsgi for production, I give a uwsgi-config file in uwsgi directory.

## study-Resource

[docker](https://docs.docker.com)

[flask](http://flask.pocoo.org)

## License

This project is licensed under the terms of the Apache license.

