#encoding:utf-8
#material converter
import maya.cmds as mc
import pymel.core as pm
import sys
import json
mc.about(windows = 1)
scriptPath = mc.internalVar(usd = 1)
AbcMatToolPath = scriptPath + r'AbcMatTool'

# if the systerm is windows,then use \\ replace /
if mc.about(windows = 1):
	AbcMatToolPath = AbcMatToolPath.replace(r'/','\\')
else:
	pass
	
if AbcMatToolPath not in sys.path:
    sys.path.insert(0,AbcMatToolPath)

try:
    import UI
    
except:
    mc.error('the DW_MaterialManager folder is placed wrong,the right path is : {0}'.format(scriptPath))
    
reload(UI)
UI.UI()