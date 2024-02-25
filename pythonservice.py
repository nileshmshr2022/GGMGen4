import win32serviceutil
import win32service
import os
import sys
import subprocess
import servicemanager
import win32event


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
        script_path = os.path.join(os.path.dirname(__file__), "configparser.py")

        try:
            with subprocess.Popen([sys.executable, script_path], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
                output, error = process.communicate()

                if output:
                    print("Script output:", output.decode())
                else:
                    print("Script did not produce any output.")

                if error:
                    print("Script error:", error.decode())

        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            # Perform cleanup or additional actions
            pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # Running as service
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PythonScriptService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        # Running from the command line
        win32serviceutil.HandleCommandLine(PythonScriptService)

