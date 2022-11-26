## v0.2.0 (2022-11-26)

### Feat

- **crud/db/model**: remove type hint
- **crud/db/init_db.py**: add type: ignore
- **crud/repository/comment.py,-user.py**: add type: ignore
- **crud/tests/conftest.py**: add type: ignore
- **crud/service**: change return type enable optional
- change user: UserCreateDTO -> request: UserCreateDTO, comment: CommentCreateDTO
- **crud/apis/v1**: add api prefix "v1" for api versioning and remove useless slash
- **crud/db/model**: add type hint
- change project structure
- **crud/apis/v1/endpoints**: add http status code, add if condition
- **tests/test_apis/test_users.py**: remove import router
- **crud/apis**: add version through URI path
- **crud/apis**: add http status code
- change schema
- **db/model/user.py**: remove email validator
- change domain -> schema
- **crud/repository**: change if condition
- **crud/apis**: change if condition
- change project structure
- change structure db/model -> domain

## v0.1.0 (2022-11-21)

### Feat

- **crud/service**: change signature
- **crud/apis**: articles.py(user_id -> author_id)
- **db/model/articles.py**: change user_id -> author_id, add lazy="joined" about comments column
- change crud/repository
- change schemas
- **crud/apis**: change apis
- **db/model/users.py**: add lazy="joined"(articles, comments)
- change project structure
- **apis/articles.py**: remove unnecessary slash, add return status code
- add setup command, httpx 0.23.0 -> 0.23.1
- **service/articles.py**: change return type
- **test_apis**: add e2e test code
- **Makefile**: change run script
- change requests -> httpx
- **Makefile**: add clean command
- **Makefile**: add make run command(for run application)
- invoke isort, add __init__.py
- **add-Makefile**: Makefile
- change project structure -> layered architecture
- add httpexception

### Fix

- **crud/db/init_db.py**: drop_db() typo
- test commitizen pre hook
- **main.py**: fix import name
- add exception when user does not exist
- fix import names
- fix project structure
- project structure
- Fix main.py
- fix package name api -> apis
- spread apis structure
- change python version(3.10.8 -> 3.10.7) for pyenv(pyenv not support 3.10.8)
