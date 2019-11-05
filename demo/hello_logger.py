#!/usr/bin/env python3

import logging, logging.handlers
from pprint import pprint

logger = None

if __name__ == "__main__":

    logger = logging.getLogger( __name__ )
    formatter = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

    outhandler = logging.StreamHandler()
    syshandler = logging.handlers.SysLogHandler( address='/dev/log', facility=logging.handlers.LOG_USER )

    outhandler.setFormatter( formatter )
    syshandler.setFormatter( formatter )

    outhandler.setLevel( logging.DEBUG )

    logger.addHandler( outhandler )
    logger.addHandler( syshandler )


    for i in range(:2048):
        logger.info( "Log message %s" % (i) )
