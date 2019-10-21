import os.path
import platform


class system_information:
    #operating system name
    os_name = str()
    python_platform_name = str()
    current_working_directory = str()
    success_in_getting_os_name = False
    success_in_getting_python_platform_name = False
    success_in_getting_current_working_directory = False

    def __init__(self):
        self.get_pythonplatformname()
        self.get_current_working_directory()

    def get_pythonplatformname(self):
        self.python_platform_name = platform.system()
        self.success_in_getting_python_platform_name = True

        #windows
        if(self.python_platform_name.lower().startswith("windows")):
            self.set_os_name("windows")
        #linux
        if(self.python_platform_name.lower().startswith("linux")):
            self.set_os_name("linux")
        #mac---darwin(10182919)
        if(self.python_platform_name.lower().startswith("darwin")):
            self.set_os_name("mac")


    def set_os_name(self,osName):
        self.os_name = osName
        self.success_in_getting_os_name = True

    def get_current_working_directory_and_return(self):
        return os.getcwd()
        
    def get_current_working_directory(self):
        self.current_working_directory = os.getcwd()
        self.success_in_getting_current_working_directory = True