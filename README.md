
# Тестовое задание реализация api товаров магазина
upd: вместо фикстур была использована 2 миграция 





## Товар (Item)

- Имя [не более 64 символов, обязательное]
- Дата добавления
- Дата последнего изменения
- Описание [текстовое поле, обязательное]
- Продавец [Seller**]
- Упорядочены по дате последнего изменения

## Продавец (Seller)
- Название магазина [не более 128 символов, обязательное]
- Дата создания
- Описание [текстовое поле, обязательное]
- Товары [Item]


## Run Locally

Clone the project

```bash
  git clone https://github.com/blade1death/django_storeapp
```

Go to the project directory

```bash
  cd django_storeapp
```

Install dependencies

```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

```

Start the server

```bash
  docker compose build
  docker compose up
```
