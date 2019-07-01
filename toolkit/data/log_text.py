# coding = utf-8
import logging, os, sys
import logging.handlers
import os.path
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


class MyLog:
    """
    https://www.cnblogs.com/yyds/p/6901864.html
    日志配置类
    log_name 计划储存目标名称
    """

    def __init__(self, log_name):
        self.log_name = log_name
        self.logger = logging.getLogger(log_name)  # 设置 日志名称
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 获取文件所在目录
        if not os.path.exists(log_path):
            os.makedirs(log_path)
            print('---文件夹已创建！')
        log_name = log_path + self.log_name + '.log'
        """when 是一个字符串的定义如下：
            “S”: Seconds
            “M”: Minutes
            “H”: Hours
            “D”: Days
            “W”: Week day (0=Monday)
            “midnight”: Roll over at midnight
        interval 间隔时间 
        backupCount 保留日志文件个数-默认为0  不删除日志文件
            """
        # 记录日志至处理器(按照日期分割)
        # save_handle = logging.handlers.TimedRotatingFileHandler(log_name, when='midnight', interval=1, backupCount=7)
        save_handle = logging.FileHandler(log_name)  # 记录日志至处理器
        save_handle.setLevel(logging.DEBUG)  # 设置日志最低级别=debug
        print_handle = logging.StreamHandler()  # 输出日志至控制台
        print_handle.setLevel(logging.INFO)  # 设置日志最低级别>info
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")  # 定义日志输出格式
        # formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")  # 定义日志输出格式
        save_handle.setFormatter(formatter)
        print_handle.setFormatter(formatter)
        self.logger.addHandler(print_handle)  # 添加日志
        self.logger.addHandler(save_handle)


if __name__ == '__main__':
    a = MyLog("测试日志")
    a.logger.debug('debug message')
    a.logger.info('info message')
    a.logger.warning('warning message')
    a.logger.error('error message')
    a.logger.critical('critical message')
