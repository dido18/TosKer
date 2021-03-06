# from ..helper import Logger
from .. import docker_interface
from ..graph.nodes import Volume


class Volume_manager:

    @staticmethod
    def create(node):
        assert isinstance(node, Volume)
        docker_interface.create_volume(node)

    # @staticmethod
    # def delete(self, node):
    #     assert isinstance(node, Volume)
    #     docker_interface.delete_volume(node)
