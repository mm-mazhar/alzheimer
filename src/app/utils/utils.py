# -*- coding: utf-8 -*-
# """
# utils.py
# Created on Dec 17, 2024
# @ Author: Mazhar
# """

import logging

# from configs import load_log_dictConfig

logger = logging.getLogger("app.logs")


def add(x, y) -> str:
    logger.warning("*utils.py* --> Adding two numbers inside src/app/utils/utils.py")
    return x + y
