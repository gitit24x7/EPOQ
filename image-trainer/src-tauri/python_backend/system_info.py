import torch
import platform
import psutil
import sys
import json
import os

def get_system_info():
    info = {
        "python": {
            "version": sys.version.split()[0],
            "executable": sys.executable,
        },
        "torch": {
            "version": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "cuda_version": torch.version.cuda,
            "gpu_name": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        },
        "hardware": {
            "cpu": platform.processor(),
            "cores": psutil.cpu_count(logical=True),
            "ram_total_gb": round(psutil.virtual_memory().total / (1024**3), 2),
            "ram_available_gb": round(psutil.virtual_memory().available / (1024**3), 2),
        },
        "platform": {
            "os": platform.system(),
            "release": platform.release(),
            "architecture": platform.machine(),
            "hostname": platform.node(),
        }
    }

    print(json.dumps(info))


if __name__ == "__main__":
    get_system_info()