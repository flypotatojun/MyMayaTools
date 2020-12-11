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
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(['ComboBoxItem 1','ComboBoxItem 2', 'ComboBoxItem 3'] )

        self.ok_btn = QtWidgets.QPushButton('Ok')
        self.cancel_btn = QtWidgets.QPushButton('Cancel')

    def create_layouts(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('ComboBox:', self.combobox)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ok_btn)
        button_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.cancel_btn.clicked.connect(self.close)


if __name__ == "__main__":

    # try:
    #     test_dialog.close()
    #     test_dialog.deleteLater()
    # except:
    #     pass

        test_dialog = TestDialog()
        test_dialog.show()