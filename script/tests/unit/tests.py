# coding=utf-8

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

    def test_should_match_strings_that_are_closest_possible_matches_in_arabic(self):
        location = Location(name=u'مصر')
        value_to_match = u'مصر'
        location.values_list = Mock(return_value=[u'مصر', u'المغرب', u'الجزائر'])
        location.get = Mock(return_value=location)
        matched_values = find_closest_match(value_to_match, location)
        self.assertEquals(matched_values, location)

    def test_should_match_strings_that_are_closest_possible_matches_in_french(self):
        location = Location(name=u'Là Frêîçós')
        value_to_match = u'Là Frêîçós'
        location.values_list = Mock(return_value=[u'Brésil', u'Là Frêîçós', u'Israël'])
        location.get = Mock(return_value=location)
        matched_values = find_closest_match(value_to_match, location)
        self.assertEquals(matched_values, location)

