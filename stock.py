# -*- coding:utf-8 -*-

from jqdatasdk import *
auth('18010073691','sunyanzi')

df = finance.run_query(query(finance.SW1_DAILY_PRICE).filter(finance.SW1_DAILY_PRICE.date>='2018-01-01', finance.SW1_DAILY_PRICE.code == '801752'))
