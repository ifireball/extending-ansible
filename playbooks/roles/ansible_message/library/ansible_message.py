#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Barak Korren <bkorren@redhat.com>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
module: ansible_message

short_description: Send a message with an Ansible FTL communications device

version_added: "2.8"

author:
    - "Barak Korren <bkorren@redhat.com>"

description:
    - Send a message to distant planets using an 'Ansible' interplanetary
      faster-then-light communications device

options:
    destination:
        description:
            - The planet name to send the message to
        required: yes
    message:
        description:
            - The message text to send
        required: yes

requirements:
    - Run directly on the Ansoble device controller host
    - Have the ansible-device Python module installed
'''

EXAMPLES = '''
- name: Message to Earth
  ansible_message:
    destination: Earth
    message: Hi from Marse!
'''
from ansible_device import send_message, AnsibleDeviceException

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            destination=dict(type='str', required=True),
            message=dict(type='str', required=True),
        )
    )

    try:
        send_message(**module.params)
        module.exit_json(changed=True)
    except AnsibleDeviceException as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
