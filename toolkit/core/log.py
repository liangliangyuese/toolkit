# coding = utf-8
import os
import logging
import logging.handlers
import os.path
import datetime


# suffix
class MyLog:
    """when 是一个字符串的定义如下：
                    “S”: Seconds 秒
                    “M”: Minutes 分
                    “H”: Hours 小时
                    “D”: Days 天
                    “W”: Week day (0=Monday)
                    “midnight”: Roll over at midnight 每天
                interval 等待单位时间后，logger自动重建文件
                backupCount 保留日志文件个数-默认为0  不删除日志文件 """

    def __init__(self, log_name=None, level="WARNING", time_handle=False, time_handle_type="midnight", interval=1,
                 backup_count=7):
        # 生成日志文件夹
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 获取文件所在目录
        if not os.path.exists(log_path):
            print('--生成日志文件夹--')
            os.makedirs(log_path)
        if not log_name:
            raise ValueError("请使用正确日志名称")
        if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise ValueError("请设置正确的输入日志等级--DEBUG，INFO，WARNING，ERROR，CRITICAL--")
        if time_handle_type not in ["S", "M", "H", "D", "W", "midnight"]:
            raise ValueError("请使用正确的日期切割选项")
        self.logger = logging.getLogger(log_name)
        # 设置 日志名称
        log_name = log_path + log_name + datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        if time_handle:
            # 记录日志至处理器(按照日期分割)
            log_handle = logging.handlers.TimedRotatingFileHandler(log_name, when=time_handle_type, interval=interval,
                                                                   backupCount=backup_count)
        else:
            # 设置日志处理器
            log_handle = logging.FileHandler(log_name)
        # 设置日志记录等级
        log_handle.setLevel(eval("logging.{}".format(level)))
        print_handle = logging.StreamHandler()  # 输出日志至控制台
        print_handle.setLevel(logging.DEBUG)  # 设置日志最低级别>info
        # 设置日志格式器
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")
        log_handle.setFormatter(formatter)
        print_handle.setFormatter(formatter)
        self.logger.addHandler(print_handle)  # 添加日志
        self.logger.addHandler(log_handle)


if __name__ == '__main__':
    a = MyLog("测试日志", time_handle=True)
    a.logger.debug('debug message')
    a.logger.info('info message')
    a.logger.warning('warning message')
    a.logger.error('error message')
    a.logger.critical('critical message')
