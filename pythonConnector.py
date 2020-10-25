#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:27:07 2020

@author: jacobfericy
"""

import snowflake.connector
import pandas as pd



def snowflake_to_df(user, password, account, warehouse, database, table):
    

    # defines the connection after inputting user, password and account in string form
    ctx = snowflake.connector.connect(
        user = user,
        password = password,
        account = account,
        )

    #defines the snowflake query when inputting warehouse, database and table information in string form
    query = '''
    SELECT * FROM ''' + warehouse + '''.''' + database + '''.''' + table

    cur = ctx.cursor().execute(query)
    df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
    return df

