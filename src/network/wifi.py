import nmcli


class Wifi:
    @staticmethod
    def get_wifi_list():
        """
        This module lists the connectable wifis.

        Returns:
            list: connectable wifi list
        """

        device_wifi_list = nmcli.device.wifi()
        wifi_list = Wifi.__make_wifi_unique(wifi_list=device_wifi_list)
        connection_wifi_list = []
        connected_wifi_ssid = Wifi.status().connection
        for i in range(len(wifi_list)):
            connection_wifi_list.insert(
                0 if wifi_list[i].ssid == connected_wifi_ssid else i,
                {
                    'wifiName': wifi_list[i].ssid,
                    'bssid': wifi_list[i].bssid,
                    'freq': wifi_list[i].freq,
                    'rate': wifi_list[i].rate,
                    'signal': wifi_list[i].signal,
                    'security': wifi_list[i].security,
                    'connection': "connected" if wifi_list[i].ssid == connected_wifi_ssid else "none",
                },
            )

        return connection_wifi_list

    @staticmethod
    def get_connected_wifi_list():
        connected_wifi_list = dict()
        for wifi in nmcli.connection():
            connected_wifi_list[wifi.name] = wifi
        return connected_wifi_list

    @staticmethod
    def connect(wifi_name, password):
        """
        This module allows to connect to Wi-Fi

        Args:
            wifi_name (string): connection wifi name
            password (string): password
        """
        nmcli.device.wifi_connect(ssid=wifi_name, password=password)

    @staticmethod
    def up(wifi_name):
        """
        This module disconnects wifi

        Args:
            wifi_name (string): connected wifi name
        """
        nmcli.connection.up(name=wifi_name)

    @staticmethod
    def down(wifi_name):
        """
        This module disconnects wifi

        Args:
            wifi_name (string): connection wifi name
        """
        nmcli.connection.down(name=wifi_name)

    @staticmethod
    def forget(wifi_name):
        """
        This module forget wifi connection

        Args:
            wifi_name (string): connected wifi name
        """
        nmcli.connection.delete(name=wifi_name)

    @staticmethod
    def modify(wifi_name, option_dic):
        """
        This module changes wifi settings according to incoming parameters

        Args:
            wifi_name (string): connected wifi name
            option_dic (dictionary): wifi features to change
        """
        nmcli.connection.modify(name=wifi_name, options=option_dic)

    @staticmethod
    def detail(wifi_name):
        """
        This module shows detailed information of connected wifi.

        Args:
            wifi_name (string): connected wifi name

        Returns:
            list: wifi detail list
        """

        def split_addresses(addresses):
            addresses_dic = {}
            addresses_dic["ip"], addresses_dic["netmask"] = addresses.split("/")
            return addresses_dic

        def str_routes_convert_to_dict(routes):
            routes = routes.replace(" ", "").replace("=", ":").replace("{", "").replace("}", "").split(",")
            routes_dic = {}
            for i in routes:
                routes_dic[i.split(":")[0].strip('\'').replace("\"", "")] = i.split(":")[1].strip('"\'')
            routes_dic['ip'], routes_dic["netmask"] = routes_dic['ip'].split("/")

            if not "mt" in routes_dic.keys():
                routes_dic["mt"] = ""
            return routes_dic

        wifi_detail_list = nmcli.connection.show(name=wifi_name)
        device_wifi_list = Wifi.get_wifi_list()
        device_wifi_detail_list = [
            device_wifi for device_wifi in device_wifi_list if device_wifi['wifiName'] == wifi_name
        ]

        filtered_wifi_detail_list = {
            "signal": device_wifi_detail_list[0]['signal'],
            "rate": device_wifi_detail_list[0]['rate'],
            "security": device_wifi_detail_list[0]['security'],
            "ipv4_address": wifi_detail_list['IP4.ADDRESS[1]'],
            "ipv6_address": wifi_detail_list['IP6.ADDRESS[1]'],
            "freq": device_wifi_detail_list[0]['freq'],
            "dns": wifi_detail_list['IP4.DNS[1]'],
            "autoconnect": wifi_detail_list['connection.autoconnect'],
            "metered": wifi_detail_list['connection.metered'],
            "ipv4_method": wifi_detail_list["ipv4.method"],
            "ipv4_addresses": ""
            if wifi_detail_list["ipv4.addresses"] == None
            else split_addresses(wifi_detail_list["ipv4.addresses"]),
            "ipv4_gateway": "" if wifi_detail_list["ipv4.gateway"] == None else wifi_detail_list["ipv4.gateway"],
            "ipv4_dns": "" if wifi_detail_list["ipv4.dns"] == None else wifi_detail_list["ipv4.dns"],
            "ipv4_routes": ""
            if wifi_detail_list["ipv4.routes"] == None
            else str_routes_convert_to_dict(wifi_detail_list["ipv4.routes"]),
            "ipv6_method": wifi_detail_list["ipv6.method"],
            "ipv6_addresses": ""
            if wifi_detail_list["ipv6.addresses"] == None
            else split_addresses(wifi_detail_list["ipv6.addresses"]),
            "ipv6_gateway": "" if wifi_detail_list["ipv6.gateway"] == None else wifi_detail_list["ipv6.gateway"],
            "ipv6_dns": "" if wifi_detail_list["ipv6.dns"] == None else wifi_detail_list["ipv6.dns"],
            "ipv6_routes": ""
            if wifi_detail_list["ipv6.routes"] == None
            else str_routes_convert_to_dict(wifi_detail_list["ipv6.routes"]),
        }
        return filtered_wifi_detail_list

    @staticmethod
    def __make_wifi_unique(wifi_list):
        """
        If there is more than one wifi with the same name, this module chooses the one with the highest signal.

        Args:
            wifi_list (list): raw wifi list

        Returns:
            list: unique wifi list
        """
        unique_wifi_list = dict()
        for wifi in wifi_list:
            if wifi.ssid not in unique_wifi_list.keys() and wifi.ssid != '':
                unique_wifi_list[wifi.ssid] = wifi

        return list(unique_wifi_list.values())

    @staticmethod
    def on():
        """
        This module turn on wifi
        """
        nmcli.radio.wifi_on()

    @staticmethod
    def off():
        """
        This module turn off wifi
        """
        nmcli.radio.wifi_off()

    @staticmethod
    def status():
        """
        This module get the wifi status

        Returns:
            list: wifi status list
        """

        wifi_status = [device for device in nmcli.device.status() if device.device_type == 'wifi']
        return wifi_status[0]
