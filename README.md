# Юнит-тесты Stellar Burgers

Исходный код находится в пакете `praktikum`. В каталоге `tests` для каждого из классов `Bun`, `Burger`, `Ingredient` и `Database` есть отдельный тестовый модуль.

## Запуск

Из корня репозитория выполните команды в активном окружении Python.

```sh
python -m pip install -r requirements.txt
python -m pytest --cov=praktikum --cov-report=term-missing --cov-report=html --cov-fail-under=70
```

HTML-отчёт создаётся в `htmlcov/index.html`. Тесты покрывают все исполняемые строки четырёх проверяемых классов. Покрытие всего пакета с учётом демонстрационного сценария в `praktikum/praktikum.py` составляет 77,53%.
