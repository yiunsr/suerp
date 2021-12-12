## 성능 확인

```
hey -c 50 -n 2000 -m GET http://192.168.142.11:8000/
```


## alembic 사용

### SQL 파일 생성(offline mode)

```
alembic revision  --autogenerate -m "first sql"
```


### 마이그레이션 적용(online mode)

* 최신 버전 적용
```
alembic upgrade head
```

* 한 버전 업그레이드
```
alembic upgrade +1
```

* 한 버전 rollback
```
alembic downgrade -1
```
