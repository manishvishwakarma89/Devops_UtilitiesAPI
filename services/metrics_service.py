import psutil
def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    
    """
    This function retrieves system metrics including CPU, memory, and disk usage.
    It also checks if any of these metrics exceed predefined thresholds.
    """
    
    cpu_threshold = 10  # 10%
    memory_threshold = 20  # 20%
    disk_threshold = 15  # 15%
    
    if cpu_percent > cpu_threshold:
        print(f"Warning: CPU usage is high at {cpu_percent}%")
    elif memory_percent > memory_threshold:
        print(f"Warning: Memory usage is high at {memory_percent}%")
    elif disk_percent > disk_threshold:
        print(f"Warning: Disk usage is high at {disk_percent}%")
    else:
        print("System is Healthy")    

    return {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent
    }