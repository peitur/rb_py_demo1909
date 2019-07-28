#!/usr/bin/env python3

import logging
from pprint import pprint

if __name__ == "__main__":
    logging.basicConfig( datefmt="%Y%m%d:%H%M%S %z",  level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    logging.info("Testing")
    logging.warning("Not as expected")
    logging.debug("knowing your stuff?")
    logging.critical("Oooops!")
