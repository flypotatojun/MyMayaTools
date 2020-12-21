

import maya.cmds as cmds


def AddShaderNameAttr():
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

if __name__ == "__main__":

    run = AddShaderNameAttr()
