import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

def confirm(parent):
    # question
    # yes / no
    # return true / false
    reply = QMessageBox.question(parent,
                                 'Confirm',
                                 'Are you sure ?',
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No
                                 )
    return reply == QMessageBox.Yes
