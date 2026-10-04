![CI](https://github.com/BansheedL/ci-lab-temperature/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![Code style](https://img.shields.io/badge/code%20style-flake8-informational)

# ci-lab-temperature

Практична робота №1 з дисципліни «Інноваційні інформаційні технології»:
створення репозиторію та найпростішого CI-пайплайна на GitHub Actions.

**Варіант 3** — модуль конвертації температур `temperature.py`.

## Функції

| Функція | Опис |
|---|---|
| `celsius_to_fahrenheit(c)` | °C → °F (`c * 9/5 + 32`) |
| `fahrenheit_to_celsius(f)` | °F → °C (`(f - 32) * 5/9`) |
| `celsius_to_kelvin(c)` | °C → K (`c + 273.15`); `ValueError`, якщо `c` нижче абсолютного нуля |

## Тести

Файл `test_temperature.py` містить 7 тестів (pytest): типові значення
(0 °C, 100 °C, 37 °C), від'ємні та межові значення (−40 °C, абсолютний нуль),
перевірку «туди й назад» °C → °F → °C та виняток для температури нижче −273.15 °C.

Локальний запуск:

```bash
pip install -r requirements.txt
pytest -v
```

## CI

Workflow `.github/workflows/ci.yml` запускається автоматично при кожному
`push` і `pull_request` у гілку `main`: встановлює залежності («збірка»)
і запускає тести. Поточний статус показує бейдж на початку цього файлу.

Розширення (крок 16):

- перевірка стилю коду за допомогою **flake8**;
- **матриця версій** Python (3.10, 3.11, 3.12) — тести запускаються
  паралельно на кожній версії.

Після успішних тестів job `build-and-push-image` збирає Docker-образ
і публікує його в GitHub Container Registry.

## Запуск через Docker

```bash
docker pull ghcr.io/bansheedl/ci-lab-app:latest
docker run --rm ghcr.io/bansheedl/ci-lab-app:latest
```
