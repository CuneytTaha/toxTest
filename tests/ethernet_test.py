from unittest import TestCase

import network


class TestEthernetControl(TestCase):
    def test_status(self):
        self.assertNotEqual(network.ethernet.status(), [])

    def test_off(self):
        network.ethernet.off()
        self.assertEqual(network.ethernet.status().state, 'unmanaged')

    def test_on(self):
        network.ethernet.on()
        self.assertIn(network.ethernet.status().state, ['unavailable', 'connected'])

    @classmethod
    def tearDownClass(cls) -> None:
        network.ethernet.on()
