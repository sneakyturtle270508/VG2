# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-29 19:58:05
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-29 19:58:11
import random
import time
import os

chars = "01abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

while True:
    # random line of characters
    line = "".join(random.choice(chars) for _ in range(80))
    print("\033[32m" + line)  # green text
    time.sleep(0.05)

