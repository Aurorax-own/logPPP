import logPPP

logPPP.LEVEL = logPPP.logPPPLevel.DEBUG
logPPP.IS_COLOR = True

logPPP.info("info", 'test', is_color=True)
logPPP.warning("warning")
logPPP.error("error")
logPPP.debug("debug")
logPPP.critical("critical")
logPPP.critical("critical", is_color=False)
