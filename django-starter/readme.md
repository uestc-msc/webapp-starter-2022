# django starter

创建 PostgreSQL 数据库服务：

```sh
docker run -d --name django_starter_postgres -p 5432:5432 -e POSTGRES_PASSWORD=test --restart always postgres
```

