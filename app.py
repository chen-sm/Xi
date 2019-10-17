

# 封装请求路径前缀
import logging
import logging.handlers
import os
import time



BASE_PATH="http://182.92.81.159/api/sys/"

# 封装路径
File_Path=os.path.dirname(os.path.abspath(__file__))
# print("File_Path当前父级路径",File_Path)
TOKEN=None
USER_ID=None

# 日志封装
def my_log_config():
    # 获取日志器对象
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    # 设置日志处理器（控制输出目标）
    to1=logging.StreamHandler() #默认控制台
    filename=File_Path+"/Log/myAuto"+time.strftime("%Y%m%d%H%M%S")+".log"
    to2=logging.handlers.TimedRotatingFileHandler(filename=filename,when="h",
                                                  interval=10,backupCount=20,encoding="utf-8")
    #设置格式化器
    fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter=logging.Formatter(fmt)

    # 组织上述对象
    to1.setFormatter(formatter)
    to2.setFormatter(formatter)
    logger.addHandler(to1)
    logger.addHandler(to2)