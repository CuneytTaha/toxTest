import subprocess

import nmcli

from .ethernet import EthernetControl
from .wifi import Wifi

nmcli.set_lang('C.UTF-8')
nmcli.disable_use_sudo()

wifi = Wifi()
ethernet = EthernetControl()


def airplane_mode_on():
    """
    This module turn on airplane mode
    """
    subprocess.call(['rfkill', 'block', 'all'])


def airplane_mode_off():
    """
    This module turn off airplane mode
    """
    subprocess.call(['rfkill', 'unblock', 'all'])


def airplane_mode_status():
    """
    This module get wifi, wwan and bluetooth statuses

    Returns:
        string: on/off status
    """

    output = subprocess.check_output(['rfkill', 'list'], stderr=subprocess.STDOUT).decode()
    wifi_status = True if 'phy0: Wireless LAN\n\tSoft blocked: yes' in output else False
    wwan_status = True if 'tpacpi_wwan_sw: Wireless WAN\n\tSoft blocked: yes' in output else False
    bluetooth_status = True if 'tpacpi_bluetooth_sw: Bluetooth\n\tSoft blocked: yes' in output else False

    return 'on' if wifi_status and wwan_status and bluetooth_status == True else 'off'


def radio_all_status():
    """
    This module get status of all radio switches

    Returns:
        Radio(object): status of all switches
    """
    return nmcli.radio.all()
