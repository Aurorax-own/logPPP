from logPPP import *

logger = get_logger(logging_level=INFO,
                    logging_is_output_sys_stdout=True,
                    logging_file="log.log",
                    logger_name=None,
                    logging_fmt=None,
                    logging_date_fmt=None)

logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
