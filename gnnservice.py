import win32serviceutil
import win32service
import os
import sys
import subprocess
import servicemanager
import win32event
from utils import logging
import time
from configreader import write_hellos
import platform

def log_system_info():
    """Log system information."""
    system_info = platform.uname()
    logging.info(f"System Information: {system_info}")

class PythonScriptService(win32serviceutil.ServiceFramework):
    _svc_name_ = "GNNService"  # Service name
    _svc_display_name_ = "GNN Service"  # Display name
    _svc_description_ = "Runs the specified Python script as a service."

    def __init__(self, args):
        super().__init__(args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.is_alive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        while self.is_alive:
            logging.debug(os.getcwd())
            write_hellos()
            time.sleep(3600)

if __name__ == '__main__':
    try:
        log_system_info()
        if len(sys.argv) == 1:
            logging.debug(f"run service .....")
            # Running as service
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(PythonScriptService)
            servicemanager.StartServiceCtrlDispatcher()
        else:
            # Running from the command line
            logging.debug(f"run service from command line.....")
            win32serviceutil.HandleCommandLine(PythonScriptService)
    except :
        logging.exception("exception receivedS")

