## 성능 확인

```
hey -c 50 -n 2000 -m GET http://localhost:8090/
```

## 환경변수 설정

### 맥, 리눅스

```
export FASTAPI_CONFIG=development
```

### 윈도우즈 cmd

```
SET FASTAPI_CONFIG=development
```

### 윈도우즈 Powershell

```
$env:FASTAPI_CONFIG="development"
```


## front 만 실행

```
cd front/super
```

## alembic 사용
* 꼭 위의 환경변수 설정이 필요하다.


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
