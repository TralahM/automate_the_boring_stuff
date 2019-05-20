import logging
# additionally pass filename keyword arg to log to file instead of screen
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Some debug event")
logging.info("Some info event")
logging.warning("Some warning event")
logging.error("Some error event")
logging.critical("Some critical event")
