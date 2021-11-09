import time
from unittest import TestCase

import network


class TestNetwork(TestCase):
    def test_airplane_mode_status(self):
        self.assertIn(network.airplane_mode_status(), ['on', 'off'])

    def test_radio_all_status(self):
        self.assertNotEqual(network.radio_all_status(), [])

    def test_airplane_mode_on(self):
        network.airplane_mode_on()
        self.assertEqual(network.airplane_mode_status(), 'on')

    def test_airplane_mode_off(self):
        network.airplane_mode_off()
        self.assertEqual(network.airplane_mode_status(), 'off')

    @classmethod
    def tearDownClass(cls):
        network.airplane_mode_off()
