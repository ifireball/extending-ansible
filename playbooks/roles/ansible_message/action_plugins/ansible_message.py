# ansible_message.py - Ansible action plugin for sending messages with an
#                      Ansible FTL communications device
#
import planetdb

from ansible.plugins.action import ActionBase
from ansible.config.manager import ensure_type
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleActionFail


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)
        module_args = self._task.args.copy()
        result = {}

        if 'destination' in module_args:
            given_name = ensure_type(module_args['destination'], 'str')
            if not isinstance(given_name, string_types):
                raise AnsibleActionFail('destination must be a string')

            try:
                destination = planetdb.lookup(given_name)
            except planetdb.PlanetdbLookupError:
                raise AnsibleActionFail('Failed to lookup destination planet')
            module_args['destination'] = destination
            result['message_destination'] = destination

        module_return = self._execute_module(
            module_name='ansible_message',
            module_args=module_args,
            task_vars=task_vars,
            tmp=tmp
        )

        result.update(module_return)
        return result
