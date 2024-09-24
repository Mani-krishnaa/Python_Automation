import logging


class Log_Maker:  # here im creating logmaker class it is a static method I can cl anywhere without crating a class
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="/home/manikrishna/Pycharm/Python_Automation/logs/QafoxLogs.py", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%Y-%m-%d %H:%M:%S", force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
