from bitmovin.utils import Serializable
from . import AbstractInfrastructure


class KubernetesInfrastructure(AbstractInfrastructure, Serializable):

    def __init__(self, name, description=None, online=None, connected=None, agent_run_command=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.online = online
        self.connected = connected
        self.agentRunCommand = agent_run_command

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        name = json_object['name']
        description = json_object.get('description')
        online = json_object.get('online')
        connected = json_object.get('connected')
        agent_run_command = json_object.get('agentRunCommand')

        kubernetes_infrastructure = KubernetesInfrastructure(name=name, description=description, online=online,
                                                             connected=connected, agent_run_command=agent_run_command,
                                                             id_=id_)

        return kubernetes_infrastructure

    def serialize(self):
        serialized = super().serialize()
        return serialized
