"""
PyGotham PyQt Tutorial

This example is a simple cookie checkout
application using PyQt5.

author: Monica Chelliah
"""

import sys

# Import PyQt widgets
from PyQt5 import QtWidgets, QtGui

# The images_rc import loads the images into Qt
import images_rc

# Import the designer UI file
import cookie_ui

# Note: All prices are represented in cents

# Cookie constants
RAISIN_PRICE = 100
CHOCOLATE_CHIP_PRICE = 125
CHOCOLATE_PRICE = 125
LINZER_PRICE = 175
GENEVA_PRICE = 175
PEANUT_PRICE = 150

# Shipping cost constants
BASE_SHIPPING_COST = 399
PER_COOKIE_SHIPPING_COST = 10


class CookieCheckout(QtWidgets.QWidget):
    """
    This is an example class, which inherits from a QWidget. The
    basic function of this class is to setup the QWidget to run and show the
    designer UI file we have already created.
    """

    def __init__(self, parent=None):
        """
        This is the constructor for CookieCheckout.

        @param parent: to be set as the parent of this widget. If parent is
            None, this widget becomes a window.
        @type parent: QtWidgets.QWidget()
        """
        # First call the superclass' constructor
        super(CookieCheckout, self).__init__(parent)

        # Initialize all the UI elements that we created in Qt Designer.
        self.ui = cookie_ui.Ui_Form()
        self.ui.setupUi(self)

        # Set the title of the panel window
        self.setWindowTitle('PyGotham Cookies')

        # Add any additional data to the widgets
        self.setupGUIElements()

        # All signal and slot connections will be done inside this method
        self.connectSignalsAndSlots()

        # Modify the default color scheme and set custom style
        self.setupStyleSheet()

    def setupGUIElements(self):
        """
        Set up and input necessary data to ready the panel.
        """
        # Insert all the cookie count options in to the six combo boxes /
        # drop down menus.
        self.cookie_combo_boxes_and_prices = (
            (self.ui.raisin_cb, RAISIN_PRICE),
            (self.ui.choc_chip_cb, CHOCOLATE_CHIP_PRICE),
            (self.ui.choc_cb, CHOCOLATE_PRICE),
            (self.ui.linzer_cb, LINZER_PRICE),
            (self.ui.geneva_cb, GENEVA_PRICE),
            (self.ui.peanut_cb, PEANUT_PRICE))
        for (combo_box, price) in self.cookie_combo_boxes_and_prices:
            for option in range(0, 13):
                # QComboBoxes have the option of adding the given text as
                # well as the data associated with each entry. So, we will be
                # passing the str type of the option for the text,
                # while keeping the int type for easy access without type
                # conversion. See PyQt docs for more info.
                combo_box.addItem(str(option), option)

    def connectSignalsAndSlots(self):
        """
        Connect the necessary signals to slots.
        """
        # Connect the 'Add to cart' button's click signal to the custom slot
        # for calculating the total cost of the cart and updating the labels
        self.ui.add_to_cart_btn.clicked.connect(self.updateCostLabels)

        # Connect the 'Checkout' button's click signal to the CookieCheckout
        # widget's close method
        self.ui.checkout_btn.clicked.connect(self.close)

    def updateCostLabels(self):
        """
        Calculate the subtotal and shipping costs and update the respective
        labels.
        """
        # Get the calculated values
        subtotal = self.calculateSubtotal()
        shipping = self.calculateShipping()
        total = subtotal + shipping

        # Update the QLabels in the panel
        self.ui.subtotal_val_lbl.setText(self.formatLabel(subtotal))
        self.ui.shipping_val_lbl.setText(self.formatLabel(shipping))
        self.ui.total_val_lbl.setText(self.formatLabel(total))

    def calculateSubtotal(self):
        """
        Calculate the subtotal for the current cart and return value.

        @return: the subtotal of the current cart
        @rtype: int
        """
        subtotal = 0
        for (combo_box, price) in self.cookie_combo_boxes_and_prices:
            per_cookie_total = combo_box.currentData() * price
            subtotal += per_cookie_total
        return subtotal

    def calculateShipping(self):
        """
        Calculate the shipping and handling cost for the current cart.

        @return: the shipping cost.
        @rtype: int
        """
        total_num_cookies = 0
        for (combo_box, price) in self.cookie_combo_boxes_and_prices:
            total_num_cookies += combo_box.currentData()
        if total_num_cookies == 0:
            return 0
        return BASE_SHIPPING_COST + total_num_cookies*PER_COOKIE_SHIPPING_COST

    def formatLabel(self, cents):
        """
        Given an int input, format it from cents into human readable
        dollars: $0.00

        @param cents: value to be formatted
        @type cents: int

        @return: the input formatted into dollars
        @rtype: str
        """
        return '${0}'.format(str(cents/100))

    def setupStyleSheet(self):
        """
        Changes the widget's default grey color scheme to a custom colourful
        scheme.
        """
        # Set the background to an image
        pixmap = QtGui.QPixmap(':images/cookies_background.png')
        brush = QtGui.QBrush(pixmap)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, brush)
        self.setPalette(palette)

        # Add a transparent background to all the labels
        style = "QLabel {background: rgba(255, 255, 255, 40%);}"
        self.setStyleSheet(style)

        # Change color of total cost label
        cost_style = "QLabel {color: #0099CC; font-weight: bold;}"
        self.ui.total_val_lbl.setStyleSheet(cost_style)
        self.ui.total_lbl.setStyleSheet(cost_style)


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
