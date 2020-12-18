from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.OpenMaya as om
import maya.cmds as cmds
import sys



cmds.about(windows = 1)
scriptPath = cmds.internalVar(usd = 1)
AbcMatToolPath = scriptPath + r'AbcMatTool'

# if the systerm is windows,then use \\ replace /
if cmds.about(windows = 1):
	AbcMatToolPath = AbcMatToolPath.replace(r'/','\\')
else:
	pass
	
if AbcMatToolPath not in sys.path:
    sys.path.insert(0,AbcMatToolPath)

try:
#     import UI
    pass
    
except:
    cmds.error('the AbcMatTool folder is placed wrong,the right path is : {0}'.format(scriptPath))





def maya_main_window():
    """
    Return the Maya main window widget as a python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
    
class BatchAbcTool(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(BatchAbcTool, self).__init__(parent)

        self.setWindowTitle('BatchAbcTool_v02')
        self.setMinimumSize(250,80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        
    def create_widgets(self):
        self.projectPath = QtWidgets.QLineEdit()
        self.add_mat_info_btn = QtWidgets.QPushButton('AddInfo')
        self.export_btn = QtWidgets.QPushButton('Export')
        
        self.select_file_path_btn = QtWidgets.QPushButton()
        self.select_file_path_btn.setIcon(QtGui.QIcon(':fileOpen.png'))
        self.select_file_path_btn.setToolTip('Output File')

        
    def create_layouts(self):
        file_path_layout = QtWidgets.QHBoxLayout()
        file_path_layout.addWidget(self.projectPath)
        file_path_layout.addWidget(self.select_file_path_btn)
                
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('File:', file_path_layout)

        button_layout = QtWidgets.QHBoxLayout()
        # button_layout.addStretch()
        button_layout.addWidget(self.add_mat_info_btn)
        button_layout.addWidget(self.export_btn)        
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        
        
    def create_connections(self):
        self.select_file_path_btn.clicked.connect(self.show_file_select_dialog)
        self.projectPath.editingFinished.connect(self.get_path)
        self.add_mat_info_btn.clicked.connect(self.addShaderNameAttr)
        self.export_btn.clicked.connect(self.batchExportAbcWithAttr)
        
    # def addShaderNameAttr(self):
    #     AddShaderNameAttr()
    #     print('addMatInfo Complete!')
    
    
    def show_file_select_dialog(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory()
        if file_path:
            self.projectPath.setText(file_path)



    def get_path(self):
        self.outputpath = self.projectPath.text()
        print(self.outputpath)
        
        


    def addShaderNameAttr(self):
        selectShape=cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
        listSelected= cmds.ls (sl=True, dag=True, leaf=True)
        newAttr = "MaterialName"
        
        for i in listSelected:
            shadeEng = cmds.listConnections(i, type="shadingEngine")
            shaderName = str(cmds.ls(cmds.listConnections(shadeEng), materials = True))[3:-2]
            if 'MaterialName' in cmds.listAttr(i):
                cmds.setAttr(i+"."+newAttr, shaderName, type="string",e=True, keyable=False, lock=False)            
                print('i have')
            else:
                print('not')
                cmds.addAttr(i, ln=newAttr, dt="string")
                cmds.setAttr(i+"."+newAttr, shaderName, type="string",e=True, keyable=False, lock=False)


        
    def batchExportAbcWithAttr(self):
        selected = cmds.ls(sl=True,long=True)
        start = 1
        end = 1
        attributeName = "MaterialName"
        #Choose your own path HERE
        for i in selected:
            root ="-root "+str(i)
            # If geo in group and you want the geo name
            # save_name = self.outputpath+i[1:-4]+".abc"
            save_name = self.outputpath + "/" + i.split('|')[-1] + ".abc"
            print(save_name)
            command = "-frameRange " + str(start) + " " + str(end) +" -attr " + attributeName + " -uvWrite -worldSpace " + root + " -file " + save_name
            cmds.AbcExport ( j = command )
        print('Export Finish')

        



if __name__ == "__main__":

    try:
        Batch_Abc_Tool.close()
        Batch_Abc_Tool.deleteLater()
    except:
        pass
    Batch_Abc_Tool = BatchAbcTool()
    Batch_Abc_Tool.show()