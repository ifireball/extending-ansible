# ansible_device.py - Python API for controlling an Ansible device
import os
from datetime import datetime

MSG_LOCATION = '/ansible_messages'


class AnsibleDeviceException(Exception):
    pass


def send_message(destination, message):
    """Send a message over the Ansible device

    :param str destination: The destination planet to send the message to
    :param str message:     The message text to send
    """
    msg_file = datetime.now().isoformat() + '.txt'
    msg_dir = os.path.join(MSG_LOCATION, str(destination))
    try:
        os.makedirs(msg_dir)
    except OSError as e:
        if e.errno == 17:
            # Ignore 'file exists' errors
            pass
        else:
            raise
    msg_path = os.path.join(msg_dir, msg_file)
    with open(msg_path, 'w') as f:
        f.write(str(message))
