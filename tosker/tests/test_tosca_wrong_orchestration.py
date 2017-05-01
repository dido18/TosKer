import unittest
from tosker.orchestrator import Orchestrator
from .test_tosca_base import Test_Orchestrator


class Test_Software_Linkcycle(Test_Orchestrator):

    def setUp(self):
        super(self.__class__, self).setUp()
        self.orchestrator.parse(
            'tosker/tests/TOSCA/hello.yaml')

    def test(self):
        self.create()
        self.assertRaises(Exception, self.orchestrator.create)
        self.delete()
        self.assertRaises(Exception, self.orchestrator.delete)


if __name__ == '__main__':
    unittest.main()