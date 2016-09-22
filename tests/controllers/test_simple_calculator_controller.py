# -*- coding: utf-8 -*-

"""
    tests.controllers.test_simple_calculator_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 09/22/2016
"""

import jsonpickle
from .controller_test_base import *

class SimpleCalculatorControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SimpleCalculatorControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.simple_calculator

    # Test Case to see if summation works
    def test_summation_test(self):
        # Parameters for the API call
        options = {}
        options['operation'] = None
        options['x'] = None
        options['y'] = None

        # Perform the API call through the SDK function
        result = self.controller.get_calculate(options)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('11', self.response_catcher.response.raw_body)


