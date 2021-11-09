import time
from unittest import TestCase

import network


class TestWifi(TestCase):
    @classmethod
    def setUpClass(cls):
        time.sleep(4)
        cls.wifi_ssid = "3BFab-General"
        cls.wifi_password = "20193BFab*"

    def test_get_wifi_list(self):

        wifi_list = network.wifi.get_wifi_list()
        self.assertNotEqual(wifi_list, [])

    def test_status(self):
        self.assertNotEqual(network.wifi.status(), [])

    def test_connect(self):
        network.wifi.get_wifi_list()
        network.wifi.connect(wifi_name=self.wifi_ssid, password=self.wifi_password)
        self.assertEqual(network.wifi.status().state, 'connected')

    def test_down(self):

        network.wifi.down(wifi_name=self.wifi_ssid)
        self.assertEqual(network.wifi.status().state, 'disconnected')

    def test_up(self):
        network.wifi.up(wifi_name=self.wifi_ssid)
        self.assertEqual(network.wifi.status().state, 'connected')

    def test_forget(self):
        network.wifi.connect(wifi_name=self.wifi_ssid, password=self.wifi_password)
        network.wifi.forget(wifi_name=self.wifi_ssid)
        self.assertIn(network.wifi.status().state, ['deactivating', 'disconnected'])

    def test_detail(self):
        network.wifi.connect(wifi_name=self.wifi_ssid, password=self.wifi_password)
        self.assertEqual(len(network.wifi.detail(wifi_name=self.wifi_ssid)), 10)

    def test_modify(self):
        network.wifi.connect(wifi_name=self.wifi_ssid, password=self.wifi_password)
        network.wifi.modify(wifi_name=self.wifi_ssid, option_dic={'connection.metered': 'yes'})
        self.assertEqual(network.wifi.detail(wifi_name=self.wifi_ssid)[8], 'yes')

    def test_on(self):
        network.wifi.on()
        self.assertEqual(network.radio_all_status().wifi, True)

    def test_off(self):
        network.wifi.off()
        self.assertEqual(network.radio_all_status().wifi, False)
