#!/usr/bin/env python
# Usage example for using the ansible_device module
#
from ansible_device import (
    send_message,
    AnsibleDeviceException
)

try:
    send_message(
        'Earth',
        'Hello world!\n'
    )
except AnsibleDeviceException:
    print('Failed to send!')
