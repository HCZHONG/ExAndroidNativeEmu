from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def, JavaMethodDef

class Boolean(metaclass=JavaClassDef, jvm_name='java/lang/Boolean'):
    
    def __init__(self, value):
        self.__value = value
    #

#


class Integer(metaclass=JavaClassDef, jvm_name='java/lang/Integer'):
    
    def __init__(self, value):
        self.__value = value
    #

#


class String(metaclass=JavaClassDef, jvm_name='java/lang/String'):
    
    def __init__(self, value):
        self.__value = value
    #

#