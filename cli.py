import click
import random
import re


def log(function):
    """Декоратор, который выводит имя функции и время выполнения, например:

    @log

    def bake(pizza):

    то выдаст следующее:

    bake(Margherita) - 3с!
    """

    def _wrapper(*args, **kwargs):
        local_variables = locals()
        function_name = local_variables['function']

        # если функция обернута в декоратор, то надо сначала извлечь фукнцию:
        if 'decorator' in str(function_name):
            function_name = function_name.__closure__[0].cell_contents

        function_name = str(function_name).split(' ')[1]

        function_result = function(*args, **kwargs)

        if isinstance(function_result, int):
            time_of_implementation = function_result
        else:  # если результат функции - строка
            time_of_implementation = re.search(r'\d+', function_result).group()
            time_of_implementation = int(time_of_implementation)

        name = args[0].name

        result = f'{function_name}({name}) - {time_of_implementation}с!'
        click.echo(result)

    return _wrapper


def template(temp):
    """Декоратор, который создает шаблон для вывода значений функции по следующему виду:

    template('Доставили за {}с!')

    Наличие фигурных скобок {} обязательно
    """

    def template_decorator(function):
        def _wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            answer = temp.replace('{}', str(result))
            # click.echo(answer)
            return answer

        return _wrapper

    return template_decorator


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    click.echo(f'--- ЗАКАЗ пиццы {pizza} ---')
    click.echo(bake(pizza))
    if delivery:
        click.echo(deliver(pizza))
    else:
        click.echo(pickup(pizza))


@cli.command()
def menu():
    """Выводит меню"""
    click.echo('--- МЕНЮ ---')
    for pizza, recipe in PizzaDatabase.full_recipes().items():
        click.echo(f'- {pizza} ✨ {", ".join(recipe)}')


@template('Доставили за {}c!')
def deliver(pizza):
    """Доставляет пиццу"""
    t = random.randint(1, 10)
    return t


@template('Забрали за {}c!')
def pickup(pizza):
    """Самовывоз"""
    t = random.randint(1, 10)
    return t


@template('Приготовили за {}c!')
def bake(pizza):
    """Готовит пиццу"""
    t = random.randint(1, 10)
    return t


class PizzaDatabase:
    """Класс - сборник информации о пиццах и рецептах"""

    @staticmethod
    def full_recipes() -> dict:
        data = {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes'],
                'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni'],
                'Hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'],
                }
        return data

    @staticmethod
    def get_pizza_list() -> list:
        return list(PizzaDatabase.full_recipes().keys())

    @staticmethod
    def get_recipe(pizza: str) -> list:
        return PizzaDatabase.full_recipes()[pizza]


class Pizzas:
    """Класс работы с конкретными пиццами"""

    def __init__(self, name: str, size='L'):
        self.name = name
        self.recipe = PizzaDatabase.get_recipe(name)
        self.size = size

    def dict(self) -> dict:
        return {self.name: self.recipe}

    def __eq__(self, other):
        equal_name = self.name == other.name
        equal_recipe = self.recipe == other.recipe
        equal_size = self.size == other.size

        if equal_name:
            if equal_size:
                return 'две одинаковые пиццы'
            else:
                return 'две одинаковые пиццы, но разного размера'

        if equal_recipe:
            return 'две разные пиццы, но рецепт одинаковый'
        return 'две разные пиццы'


if __name__ == '__main__':
    cli()
