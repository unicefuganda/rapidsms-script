__author__ = 'argha'
from django.utils import unittest

from mock import Mock
from rapidsms.contrib.locations.models import Location
from script.utils.handling import find_closest_match


class TestRegistrationHandling(unittest.TestCase):

    def test_should_match_strings_that_are_closest_possible_matches(self):
        location = Location(name='Juba')
        value_to_match = 'jubaaa'
        location.values_list = Mock(return_value=['Juba', 'Kampala'])
        location.get = Mock(return_value=location)
        matched_values = find_closest_match(value_to_match, location)
        self.assertEquals(matched_values, location)