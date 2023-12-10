import unittest
from unittest import TestCase

from src.qwertypy.greetings import hello

class TestMethods(TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello from qwertypy!")