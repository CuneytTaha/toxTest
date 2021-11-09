import nmcli


class EthernetControl:
    @staticmethod
    def on():
        """
        This module turn on network
        """
        nmcli.networking.on()

    @staticmethod
    def off():
        """
        This module turn off network
        """
        nmcli.networking.off()

    @staticmethod
    def status():
        """
        This module get the ethernet status

        Returns:
            list: ethernet status list
        """
        ethernet_status = [device for device in nmcli.device.status() if device.device_type == 'ethernet']
        return ethernet_status[0]
