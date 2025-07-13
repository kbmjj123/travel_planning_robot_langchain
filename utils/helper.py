from datetime import datetime


def get_current_local_datetime():
    """获取当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")