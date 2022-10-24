## Описание программы

Сервис cli.py выводит информацию о пицце, времени приготовления и доставке

## Запуск программы

Программа запускается с помощью **Click** через терминал.

**Click** должен быть установлен:

```python
pip install click
```

Нужно не забыть перейти в папку, где находится программа

- запуск программы, вывести меню:

```python
python cli.py menu
```

Пример вывода программы:

```python
--- МЕНЮ ---
- Margherita ✨ tomato sauce, mozzarella, tomatoes
- Pepperoni ✨ tomato sauce, mozzarella, pepperoni
- Hawaiian ✨ tomato sauce, mozzarella, chicken, pineapples
```

- оформление заказа без доставки (забрать самому)

```python
python cli.py order pepperoni
```

Пример вывода программы:
```python
--- ЗАКАЗ пиццы pepperoni ---
Приготовили за 1c!
Забрали за 7c!
```

- оформление заказа с доставкой

```python
python cli.py order perreroni --delivery
```

Пример вывода программы:
```python
--- ЗАКАЗ пиццы perreroni ---
Приготовили за 7c!
Доставили за 6c!
```

## Дополнительно

Если в коде программы перед функцией написать декоратор @log, то он выведет время выполнения по следующему шаблону

```python
'bake — 2с!'
```

## Проводимые тесты

Запуск теста происходит через файл tests.py на основе UnitTest

Проводятся следующие тесты:

- тестирование класса Pizzas - test_pizza_eq1, test_pizza_eq2, test_pizza_eq3
- тестирование метода dict() - test_dict
- тестирование функций bake, - test_bake
- тестирование функций pickup - test_pickup
- тестирование функций deliver - test_deliver
- тестирование функций bake с использованым декоратором-шаблоном - test_bake_with_decorator
- тестирование функций pickup с использованым декоратором-шаблоном - test_pickup_with_decorator
- тестирование функций deliver с использованым декоратором-шаблоном - test_deliver_with_decorator




