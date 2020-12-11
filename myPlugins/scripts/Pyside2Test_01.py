from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

def maya_main_window():
    """
    Return the Maya main window widget as a python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle('Test Dialog')
        self.setMinimumHeight(100)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox1 = QtWidgets.QCheckBox('Checkbox1')
        self.checkbox2 = QtWidgets.QCheckBox('Checkbox2')
        self.ok_btn = QtWidgets.QPushButton('Ok')
        self.cancel_btn = QtWidgets.QPushButton('Cancel')

    def create_layouts(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ok_btn)
        button_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.lineedit)
        main_layout.addWidget(self.checkbox1)
        main_layout.addWidget(self.checkbox2)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.lineedit.editingFinished.connect(self.print_hello_name)
        self.checkbox1.toggled.connect(self.print_is_hidden)
        
        self.cancel_btn.clicked.connect(self.close)

    def print_hello_name(self):
        name = self.lineedit.text()
        print('Hello {0}!'.format(name))

    def print_is_hidden(self, checked):
        # hidden = self.checkbox1.isCheckable()
        if checked:
            print('Visible')
        else:
            print('Hidden')






if __name__ == "__main__":

    # try:
    #     test_dialog.close()
    #     test_dialog.deleteLater()
    # except:
    #     pass

        test_dialog = TestDialog()
        test_dialog.show()