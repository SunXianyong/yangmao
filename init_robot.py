from werobot import WeRoBot
from wecaht_setting import APP_ID, APP_SECRET

# robot = WeRoBot(token='yangmao')
#
# robot.config["APP_ID"] = APP_ID
# robot.config["APP_SECRET"] = APP_SECRET
#
# # 让服务器监听
# robot.config['HOST'] = '0.0.0.0'
# robot.config['PORT'] = 80
#
#

# 初始按钮
# client = robot.client
# client.create_menu({
#     "button": [
#         {
#             "name": "外卖",
#             "sub_button": [
#                 {'type': 'click',
#                  'name': '美团',
#                  "key": "HB_meituan",
#                  "url": "http://wx.tangkuai.info/"},
#                 {'type': 'click',
#                  'name': '饿了吗',
#                  'key': 'HB_elema',
#                  "url": "http://wx.tangkuai.info/my_miner"}
#             ]
#         },
#         {
#             "name": "购物",
#             "sub_button": [
#                 {'type': 'click',
#                  'name': '京东',
#                  "key": "miner_info",
#                  "url": "http://wx.tangkuai.info/"},
#                 {'type': 'click',
#                  'name': '淘宝',
#                  'key': 'miner_profit',
#                  "url": "http://wx.tangkuai.info/my_miner"},
#                 {'type': 'click',
#                  'name': '拼多多',
#                  'key': 'miner_profit',
#                  "url": "http://wx.tangkuai.info/my_miner"}
#             ]
#         },
#     ]
# })