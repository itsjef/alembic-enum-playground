# alembic-enum-playground

## Play

Start PostgreSQL database using Docker:
```bash
$ docker run -d -e POSTGRES_PASSWORD=secret -p 5432:5432 postgres:14
```

Run migrations:
```base
$ alembic upgrade head
```
