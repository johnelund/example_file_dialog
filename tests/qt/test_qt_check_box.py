#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from ..common import check_box
from enaml.toolkit import qt_toolkit

class TestQtCheckBox(check_box.TestCheckBox):
    """ QtCheckbox tests. """

    toolkit = qt_toolkit()

    def get_text(self, widget):
        """ Returns the text from the tookit widget.

        """
        return widget.text()

    def checked_status(self, widget):
        """ Returns the text from the tookit widget.


        """
        return widget.isChecked()

    def checkbox_pressed(self, widget):
        """ Press the checkbox programmatically.

        """
        self.widget.pressed.emit()

    def checkbox_released(self, widget):
        """ Release the button programmatically.

        """
        self.widget.released.emit()

    def checkbox_toggle(self, widget):
        """ Toggle the button programmatically.

        """
        self.widget.toggled.emit(True)
