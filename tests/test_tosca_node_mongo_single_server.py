import unittest

from .test_tosca_base import Test_Orchestrator


class Test_Node_Mongo_Single_Server(Test_Orchestrator):

    def setUp(self):
        super(self.__class__, self).setUp()
        self.file = 'data/examples/node-mongo/node-mongo-single-server.yaml'

    def test(self):
        self.create()
        self.start()
        self.stop()
        self.start()
        self.stop()
        self.delete()


if __name__ == '__main__':
    unittest.main()
