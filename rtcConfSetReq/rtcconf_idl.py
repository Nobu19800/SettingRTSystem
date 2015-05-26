# Python stubs generated by omniidl from idl/rtcconf.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)

# #include "BasicDataType.idl"
import BasicDataType_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")

#
# Start of module "RTCConfData"
#
__name__ = "RTCConfData"
_0_RTCConfData = omniORB.openModule("RTCConfData", r"idl/rtcconf.idl")
_0_RTCConfData__POA = omniORB.openModule("RTCConfData__POA", r"idl/rtcconf.idl")


# struct confData
_0_RTCConfData.confData = omniORB.newEmptyClass()
class confData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTCConfData/confData:1.0"

    def __init__(self, id, data):
        self.id = id
        self.data = data

_0_RTCConfData.confData = confData
_0_RTCConfData._d_confData  = (omniORB.tcInternal.tv_struct, confData, confData._NP_RepositoryId, "confData", "id", (omniORB.tcInternal.tv_string,0), "data", (omniORB.tcInternal.tv_string,0))
_0_RTCConfData._tc_confData = omniORB.tcInternal.createTypeCode(_0_RTCConfData._d_confData)
omniORB.registerType(confData._NP_RepositoryId, _0_RTCConfData._d_confData, _0_RTCConfData._tc_confData)
del confData

# typedef ... confDataSeq
class confDataSeq:
    _NP_RepositoryId = "IDL:RTCConfData/confDataSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_RTCConfData.confDataSeq = confDataSeq
_0_RTCConfData._d_confDataSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:RTCConfData/confData:1.0"], 0)
_0_RTCConfData._ad_confDataSeq = (omniORB.tcInternal.tv_alias, confDataSeq._NP_RepositoryId, "confDataSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:RTCConfData/confData:1.0"], 0))
_0_RTCConfData._tc_confDataSeq = omniORB.tcInternal.createTypeCode(_0_RTCConfData._ad_confDataSeq)
omniORB.registerType(confDataSeq._NP_RepositoryId, _0_RTCConfData._ad_confDataSeq, _0_RTCConfData._tc_confDataSeq)
del confDataSeq

# interface ConfDataInterface
_0_RTCConfData._d_ConfDataInterface = (omniORB.tcInternal.tv_objref, "IDL:RTCConfData/ConfDataInterface:1.0", "ConfDataInterface")
omniORB.typeMapping["IDL:RTCConfData/ConfDataInterface:1.0"] = _0_RTCConfData._d_ConfDataInterface
_0_RTCConfData.ConfDataInterface = omniORB.newEmptyClass()
class ConfDataInterface :
    _NP_RepositoryId = _0_RTCConfData._d_ConfDataInterface[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_RTCConfData.ConfDataInterface = ConfDataInterface
_0_RTCConfData._tc_ConfDataInterface = omniORB.tcInternal.createTypeCode(_0_RTCConfData._d_ConfDataInterface)
omniORB.registerType(ConfDataInterface._NP_RepositoryId, _0_RTCConfData._d_ConfDataInterface, _0_RTCConfData._tc_ConfDataInterface)

# ConfDataInterface operations and attributes
ConfDataInterface._d_open = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_save = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_setConfData_Cpp = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:RTCConfData/confDataSeq:1.0"]), None)
ConfDataInterface._d_setConfData_Py = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:RTCConfData/confDataSeq:1.0"]), None)
ConfDataInterface._d_setData_Cpp = ((omniORB.typeMapping["IDL:RTCConfData/confData:1.0"], ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_getData_Cpp = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:RTCConfData/confData:1.0"]), None)
ConfDataInterface._d_setDataSeq_Cpp = ((omniORB.typeMapping["IDL:RTCConfData/confDataSeq:1.0"], ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_getDataSeq_Cpp = ((), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:RTCConfData/confDataSeq:1.0"]), None)
ConfDataInterface._d_setData_Py = ((omniORB.typeMapping["IDL:RTCConfData/confData:1.0"], ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_getData_Py = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:RTCConfData/confData:1.0"]), None)
ConfDataInterface._d_setDataSeq_Py = ((omniORB.typeMapping["IDL:RTCConfData/confDataSeq:1.0"], ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_getDataSeq_Py = ((), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:RTCConfData/confDataSeq:1.0"]), None)
ConfDataInterface._d_addModule_Cpp = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_addModule_Py = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_startRTCD_Cpp = ((), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_startRTCD_Py = ((), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_exitRTCD_Cpp = ((), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_exitRTCD_Py = ((), (omniORB.tcInternal.tv_boolean, ), None)
ConfDataInterface._d_getRelPath = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
ConfDataInterface._d_setSystem = ((), (omniORB.tcInternal.tv_boolean, ), None)

# ConfDataInterface object reference
class _objref_ConfDataInterface (CORBA.Object):
    _NP_RepositoryId = ConfDataInterface._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def open(self, *args):
        return _omnipy.invoke(self, "open", _0_RTCConfData.ConfDataInterface._d_open, args)

    def save(self, *args):
        return _omnipy.invoke(self, "save", _0_RTCConfData.ConfDataInterface._d_save, args)

    def setConfData_Cpp(self, *args):
        return _omnipy.invoke(self, "setConfData_Cpp", _0_RTCConfData.ConfDataInterface._d_setConfData_Cpp, args)

    def setConfData_Py(self, *args):
        return _omnipy.invoke(self, "setConfData_Py", _0_RTCConfData.ConfDataInterface._d_setConfData_Py, args)

    def setData_Cpp(self, *args):
        return _omnipy.invoke(self, "setData_Cpp", _0_RTCConfData.ConfDataInterface._d_setData_Cpp, args)

    def getData_Cpp(self, *args):
        return _omnipy.invoke(self, "getData_Cpp", _0_RTCConfData.ConfDataInterface._d_getData_Cpp, args)

    def setDataSeq_Cpp(self, *args):
        return _omnipy.invoke(self, "setDataSeq_Cpp", _0_RTCConfData.ConfDataInterface._d_setDataSeq_Cpp, args)

    def getDataSeq_Cpp(self, *args):
        return _omnipy.invoke(self, "getDataSeq_Cpp", _0_RTCConfData.ConfDataInterface._d_getDataSeq_Cpp, args)

    def setData_Py(self, *args):
        return _omnipy.invoke(self, "setData_Py", _0_RTCConfData.ConfDataInterface._d_setData_Py, args)

    def getData_Py(self, *args):
        return _omnipy.invoke(self, "getData_Py", _0_RTCConfData.ConfDataInterface._d_getData_Py, args)

    def setDataSeq_Py(self, *args):
        return _omnipy.invoke(self, "setDataSeq_Py", _0_RTCConfData.ConfDataInterface._d_setDataSeq_Py, args)

    def getDataSeq_Py(self, *args):
        return _omnipy.invoke(self, "getDataSeq_Py", _0_RTCConfData.ConfDataInterface._d_getDataSeq_Py, args)

    def addModule_Cpp(self, *args):
        return _omnipy.invoke(self, "addModule_Cpp", _0_RTCConfData.ConfDataInterface._d_addModule_Cpp, args)

    def addModule_Py(self, *args):
        return _omnipy.invoke(self, "addModule_Py", _0_RTCConfData.ConfDataInterface._d_addModule_Py, args)

    def startRTCD_Cpp(self, *args):
        return _omnipy.invoke(self, "startRTCD_Cpp", _0_RTCConfData.ConfDataInterface._d_startRTCD_Cpp, args)

    def startRTCD_Py(self, *args):
        return _omnipy.invoke(self, "startRTCD_Py", _0_RTCConfData.ConfDataInterface._d_startRTCD_Py, args)

    def exitRTCD_Cpp(self, *args):
        return _omnipy.invoke(self, "exitRTCD_Cpp", _0_RTCConfData.ConfDataInterface._d_exitRTCD_Cpp, args)

    def exitRTCD_Py(self, *args):
        return _omnipy.invoke(self, "exitRTCD_Py", _0_RTCConfData.ConfDataInterface._d_exitRTCD_Py, args)

    def getRelPath(self, *args):
        return _omnipy.invoke(self, "getRelPath", _0_RTCConfData.ConfDataInterface._d_getRelPath, args)

    def setSystem(self, *args):
        return _omnipy.invoke(self, "setSystem", _0_RTCConfData.ConfDataInterface._d_setSystem, args)

    __methods__ = ["open", "save", "setConfData_Cpp", "setConfData_Py", "setData_Cpp", "getData_Cpp", "setDataSeq_Cpp", "getDataSeq_Cpp", "setData_Py", "getData_Py", "setDataSeq_Py", "getDataSeq_Py", "addModule_Cpp", "addModule_Py", "startRTCD_Cpp", "startRTCD_Py", "exitRTCD_Cpp", "exitRTCD_Py", "getRelPath", "setSystem"] + CORBA.Object.__methods__

omniORB.registerObjref(ConfDataInterface._NP_RepositoryId, _objref_ConfDataInterface)
_0_RTCConfData._objref_ConfDataInterface = _objref_ConfDataInterface
del ConfDataInterface, _objref_ConfDataInterface

# ConfDataInterface skeleton
__name__ = "RTCConfData__POA"
class ConfDataInterface (PortableServer.Servant):
    _NP_RepositoryId = _0_RTCConfData.ConfDataInterface._NP_RepositoryId


    _omni_op_d = {"open": _0_RTCConfData.ConfDataInterface._d_open, "save": _0_RTCConfData.ConfDataInterface._d_save, "setConfData_Cpp": _0_RTCConfData.ConfDataInterface._d_setConfData_Cpp, "setConfData_Py": _0_RTCConfData.ConfDataInterface._d_setConfData_Py, "setData_Cpp": _0_RTCConfData.ConfDataInterface._d_setData_Cpp, "getData_Cpp": _0_RTCConfData.ConfDataInterface._d_getData_Cpp, "setDataSeq_Cpp": _0_RTCConfData.ConfDataInterface._d_setDataSeq_Cpp, "getDataSeq_Cpp": _0_RTCConfData.ConfDataInterface._d_getDataSeq_Cpp, "setData_Py": _0_RTCConfData.ConfDataInterface._d_setData_Py, "getData_Py": _0_RTCConfData.ConfDataInterface._d_getData_Py, "setDataSeq_Py": _0_RTCConfData.ConfDataInterface._d_setDataSeq_Py, "getDataSeq_Py": _0_RTCConfData.ConfDataInterface._d_getDataSeq_Py, "addModule_Cpp": _0_RTCConfData.ConfDataInterface._d_addModule_Cpp, "addModule_Py": _0_RTCConfData.ConfDataInterface._d_addModule_Py, "startRTCD_Cpp": _0_RTCConfData.ConfDataInterface._d_startRTCD_Cpp, "startRTCD_Py": _0_RTCConfData.ConfDataInterface._d_startRTCD_Py, "exitRTCD_Cpp": _0_RTCConfData.ConfDataInterface._d_exitRTCD_Cpp, "exitRTCD_Py": _0_RTCConfData.ConfDataInterface._d_exitRTCD_Py, "getRelPath": _0_RTCConfData.ConfDataInterface._d_getRelPath, "setSystem": _0_RTCConfData.ConfDataInterface._d_setSystem}

ConfDataInterface._omni_skeleton = ConfDataInterface
_0_RTCConfData__POA.ConfDataInterface = ConfDataInterface
omniORB.registerSkeleton(ConfDataInterface._NP_RepositoryId, ConfDataInterface)
del ConfDataInterface
__name__ = "RTCConfData"

#
# End of module "RTCConfData"
#
__name__ = "rtcconf_idl"

_exported_modules = ( "RTCConfData", )

# The end.
