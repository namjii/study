import unittest

from django.forms.widgets import Widget


class DefaultWidgetSizeTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('the widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))