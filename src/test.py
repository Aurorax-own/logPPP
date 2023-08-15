from logPPP import *

Config(logging_is_output_sys_stdout=True, logging_is_output_file=False, logging_level=DEBUG)
logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")
logger.critical("critical")

import logPPP

logPPP.Config(logging_is_output_sys_stdout=True, logging_is_output_file=False, logging_level=logPPP.DEBUG)
logPPP.logger.info("info")
logPPP.logger.debug("debug")
logPPP.logger.warning("warning")
logPPP.logger.error("error")
logPPP.logger.critical("critical")
