import datetime
import locale
import sys

from ._ConsoleColors import ConsoleColors
from ._util import *
from .logPPPLevel import logPPPLevel

__all__ = ['__version__', 'logPPPLevel', 'info', 'warning', 'error', 'debug', 'critical']
__version__ = '1.0.4'
# 等级
level = logPPPLevel.INFO

# 设置控制台输出的编码为系统默认的本地化编码
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding=locale.getpreferredencoding())
# 设置控制台错误输出的编码为系统默认的本地化编码
sys.stderr = open(sys.stderr.fileno(), mode='w', encoding=locale.getpreferredencoding())


# 日志输出
def _base(args, sep=' ', end='\n', file=None, _level=logPPPLevel.INFO, color=ConsoleColors.RESET):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    args = "{:<20} {:<8} {}  {}".format(timestamp, get_caller_file_basename_path(), _level['name'], args)
    args = f"{color}{args}{ConsoleColors.RESET}"
    if _level['level'] >= level['level']:
        print(args, sep=sep, end=end, file=file)


# info等级
def info(args, sep=' ', end='\n', file=None):
    _base(args, sep, end, file, logPPPLevel.INFO, ConsoleColors.RESET)


# warning等级
def warning(args, sep=' ', end='\n', file=None):
    _base(args, sep, end, file, logPPPLevel.WARNING, ConsoleColors.YELLOW)


# error等级
def error(args, sep=' ', end='\n', file=None):
    _base(args, sep, end, file, logPPPLevel.ERROR, ConsoleColors.RED)


# debug等级
def debug(args, sep=' ', end='\n', file=None):
    _base(args, sep, end, file, logPPPLevel.DEBUG, ConsoleColors.RED)


# critical等级
def critical(args, sep=' ', end='\n', file=None):
    _base(args, sep, end, file, logPPPLevel.CRITICAL, ConsoleColors.RED)
