#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日
@author: duang
'''
from scipy.constants.constants import calorie
class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
        ]
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))
   
class CaffeineFree(CocaCola): #继承
    calories=0
    
    
print(CocaCola.caffeine)
coke_for_me=CocaCola('coca')
print(coke_for_me.local_logo)
