# -*- coding: utf-8 -*-
"""
创建一个突出北美、中美和南美的简单地图：
# @Date    : 2022年01月18日
# @Author  : Christal
"""
import pygal_maps_world.maps


wm = pygal_maps_world.maps.World()
wm.title = "China and North, Central, and South America"

# 中国、中国香港、中国澳门、中国台湾省
wm.add("China", ['cn', 'hk', 'mo', 'tw'])
# 显示北美加拿大、墨西哥、美国三个国家的人口数量
wm.add("North America", {'ca': 34126000, 'mx': 309349000, 'us': 113423000})
wm.add("Central America", ['bz', 'cr', 'gt', 'hm', 'ni', 'pa', 'sv'])
wm.add("South America", ['ar', 'bo', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('./Fig/americas.svg')
