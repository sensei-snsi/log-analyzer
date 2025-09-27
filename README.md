# Log Analyzer API

Инструмент для анализа логов Apache и простого текстового формата.
Работает как **CLI** и как **REST API (Flask)**.

## Установка
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

## CLI
```bash
python log_analyzer.py examples/access.log --top 10
```

## API (Flask)
```bash
python app.py
# http://localhost:5000
```

### Примеры запросов
**curl**
```bash
curl -X POST "http://localhost:5000/analyze?top=5" -F "file=@examples/access.log"
```

**Postman**
Импортируйте `postman_collection.json` и используйте запрос **Analyze logs**.

## Тесты
```bash
pytest -q
```

## Деплой
- Render: используйте deploy/render.yaml или укажите Build: `pip install -r requirements.txt`, Start: `python app.py`
- Railway: Start Command `python app.py`
- Docker: см. deploy/Dockerfile

## Отчёт
PDF-отчёт — в `report/`.
