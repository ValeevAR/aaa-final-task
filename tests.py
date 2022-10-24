import unittest
import cli


class TestPizzaClass(unittest.TestCase):
    """тестирование класса Pizzas"""

    def test_pizza_eq1(self):
        """тестирование метода __eq__"""
        pizza1 = cli.Pizzas('Margherita')
        pizza2 = cli.Pizzas('Margherita', size='XL')
        self.assertEqual(pizza1 == pizza2, 'две одинаковые пиццы, но разного размера')

    def test_pizza_eq2(self):
        """тестирование метода __eq__"""
        pizza1 = cli.Pizzas('Margherita')
        pizza2 = cli.Pizzas('Margherita')
        self.assertEqual(pizza1 == pizza2, 'две одинаковые пиццы')

    def test_pizza_eq3(self):
        """тестирование метода __eq__"""
        pizza1 = cli.Pizzas('Margherita')
        pizza2 = cli.Pizzas('Pepperoni')
        self.assertEqual(pizza1 == pizza2, 'две разные пиццы')

    def test_dict(self):
        """тестирование метода dict()"""
        pizza1 = cli.Pizzas('Margherita')
        result = pizza1.dict()
        self.assertEqual(result, {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']})


class TestFunctions(unittest.TestCase):
    """тестирование функций bake, pickup, deliver"""

    def test_bake(self):
        """тестирование функций bake без декоратора-шаблона"""
        result = cli.bake.__closure__[0].cell_contents('Margherita')
        self.assertIsInstance(result, int)

    def test_pickup(self):
        """тестирование функций pickup без декоратора-шаблона"""
        result = cli.pickup.__closure__[0].cell_contents('Margherita')
        self.assertIsInstance(result, int)

    def test_deliver(self):
        """тестирование функций deliver без декоратора-шаблона"""
        result = cli.deliver.__closure__[0].cell_contents('Margherita')
        self.assertIsInstance(result, int)

    def test_bake_with_decorator(self):
        """тестирование функций bake с использованым декоратором-шаблоном"""
        result = cli.bake('Margherita')
        for d in '1234567890':
            result = result.replace(d, '')
        self.assertEqual(result, 'Приготовили за c!')

    def test_pickup_with_decorator(self):
        """тестирование функций pickup с использованым декоратором-шаблоном"""
        result = cli.pickup('Margherita')
        for d in '1234567890':
            result = result.replace(d, '')
        self.assertEqual(result, 'Забрали за c!')

    def test_deliver_with_decorator(self):
        """тестирование функций deliver с использованым декоратором-шаблоном"""
        result = cli.deliver('Margherita')
        for d in '1234567890':
            result = result.replace(d, '')
        self.assertEqual(result, 'Доставили за c!')
