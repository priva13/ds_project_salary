# -*- coding: utf-8 -*-
"""
Created on Sun May 16 22:12:28 2021

@author: Pia
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/Pia/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)