"""
PyGotham PyQt Tutorial

This example is a simple cookie checkout
application using PyQt5 without any of the
behaviour implemented.

author: Monica Chelliah
"""

import sys

# Import PyQt widgets
from PyQt5 import QtWidgets

# Import the designer UI file
import cookie_ui


class CookieCheckout(QtWidgets.QWidget):
    """
    This is an example class, which inherits from a QWidget. The
    basic function of this class is to setup the QWidget to run and show the
    designer UI file we have already created.
    """

    def __init__(self, parent=None):
        """
        This is the constructor for CookieCheckout.
        """
        # First call the superclass' constructor
        super(CookieCheckout, self).__init__(parent)

        # Initialize all the UI elements that we created in Qt Designer.
        self.ui = cookie_ui.Ui_Form()
        self.ui.setupUi(self)

        # Set the title of the panel window
        self.setWindowTitle('PyGotham Cookies')


def main():
    # Initialize an application object and the widget
    app = QtWidgets.QApplication(sys.argv)
    cookie_widget = CookieCheckout()
    # Display the widget on the screen
    cookie_widget.show()
    # This enters the main event loop and waits until the application exits.
    # This starts the event handling.
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
