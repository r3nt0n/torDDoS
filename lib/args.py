#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TorDDos (https://www.github.com/R3nt0n/torddos) (14/07/2019)
# R3nt0n (https://www.github.com/R3nt0n)

import argparse


parser = argparse.ArgumentParser(description='Order your own DDos Atack through Tor Network.')

parser.add_argument('-t', '--target', action="store", metavar='', type=str, dest='target',
                    help='server to kick-out', default=False)

parser.add_argument('-n', '--attempts', action="store", metavar='', type=int, dest='max_attempts',
                    default=5, help='number of attempts of attack (default: 5)')