# -*- coding: utf-8 -*-
import demjson
import json

# from
js_obj = '''[
    {
      navTitle: '红宝石',
      itemContent: [
        {
          liText: '戒指',
          linkParam: '/hongbaoshi/?attr=356620'
        },
        {
          liText: '手链',
          linkParam: '/hongbaoshi/?attr=356633'
        },
        {
          liText: '耳饰',
          linkParam: '/hongbaoshi/?attr=357125'
        },
        {
          liText: '吊坠',
          linkParam: '/hongbaoshi/?attr=362284'
        },
        {
          liText: '项链',
          linkParam: '/hongbaoshi/?attr=356606'
        }
      ]
    },
    {
      navTitle: '蓝宝石',
      itemContent: [
        {
          liText: '戒指',
          linkParam: '/lanbaoshi/?attr=356607'
        },
        {
          liText: '手链',
          linkParam: '/lanbaoshi/?attr=357565'
        },
        {
          liText: '耳饰',
          linkParam: '/lanbaoshi/?attr=357547'
        },
        {
          liText: '吊坠',
          linkParam: '/lanbaoshi/?attr=356613'
        },
        {
          liText: '项链',
          linkParam: '/lanbaoshi/?attr=356713'
        },
        {
          liText: '裸石/戒面',
          linkParam: '/lanbaoshi/?attr=355953'
        }
      ]
    },
    {
      navTitle: '祖母绿',
      itemContent: [
        {
          liText: '戒指',
          linkParam: '/zumulv/?attr=356608'
        },
        {
          liText: '手链',
          linkParam: '/zumulv/?attr=387264'
        },
        {
          liText: '耳饰',
          linkParam: '/zumulv/?attr=356701'
        },
        {
          liText: '吊坠',
          linkParam: '/zumulv/?attr=356612'
        },
        {
          liText: '项链',
          linkParam: '/zumulv/?attr=356706'
        }
      ]
    },
    {
      navTitle: '海蓝宝石',
      itemContent: [
        {
          liText: '戒指', // ***************暂无
          linkParam: ''
        },
        {
          liText: '手链',
          linkParam: '/hailanbao'
        },
        {
          liText: '耳饰',
          linkParam: '' // ***************暂无
        },
        {
          liText: '吊坠',
          linkParam: '/hailanbaoshi'
        },
        {
          liText: '项链',
          linkParam: '/hailanbaoshi'
        }
      ]
    },
    {
      navTitle: '坦桑石',
      itemContent: [
        {
          liText: '戒指', // ***************暂无
          linkParam: ''
        },
        {
          liText: '耳饰',
          linkParam: '' // ***************暂无
        },
        {
          liText: '吊坠', // ***************暂无
          linkParam: ''
        },
        {
          liText: '裸石/戒面', // ***************暂无
          linkParam: ''
        }
      ]
    },
    {
      navTitle: '绿松石',
      itemContent: [
        {
          liText: '手链',
          linkParam: '/lvsongshi'
        },
        {
          liText: '吊坠',
          linkParam: '/lvsongshi-diaozhui'
        },
        {
          liText: '',
          linkParam: ''
        },
        {
          liText: '',
          linkParam: ''
        }
      ]
    },
    {
      navTitle: '钻石',
      itemContent:  [
        {
          liText: '戒指',
          linkParam: '' // ***************暂无
        },
        {
          liText: '手环',
          linkParam: '' // ***************暂无
        },
        {
          liText: '耳饰',
          linkParam: '' // ***************暂无
        },
        {
          liText: '吊坠',
          linkParam: '' // ***************暂无
        },
        {
          liText: '项链',
          linkParam: '' // ***************暂无
        }
      ]
    },
    {
      navTitle: '翡翠',
      itemContent: [
        {
          liText: '手镯',
          linkParam: '/so-%E7%BF%A1%E7%BF%A0%E6%89%8B%E9%95%AF'
        },
        {
          liText: '手链',
          linkParam: '/so-%E7%BF%A1%E7%BF%A0%E6%89%8B%E9%93%BE'
        },
        {
          liText: '挂件',
          linkParam: '/feicui/?attr=331540-0-0'
        },
        {
          liText: '佛公',
          linkParam: '/feicui/?attr=91077-0-0'
        },
        {
          liText: '如意',
          linkParam: '/feicui/?attr=325006-0-0'
        },
        {
          liText: '平安扣',
          linkParam: '/feicui/?attr=313991-0-0'
        }
        ,
        {
          liText: '金枝绿叶',
          linkParam: '/feicui/?attr=279388-0-0'
        },
        {
          liText: '生肖',
          linkParam: '/feicui/?attr=354381-0-0'
        },
        {
          liText: '福瓜福豆',
          linkParam: '/feicui/?attr=337702-0-0'
        },
        {
          liText: '葫芦',
          linkParam: '/feicui/?attr=352970-0-0'
        },
        {
          liText: '观音',
          linkParam: '/feicui/?attr=91099-0-0'
        },
        {
          liText: '貔貅',
          linkParam: '/feicui/?attr=337597-0-0'
        },
        {
          liText: '路路通',
          linkParam: '/feicui/?attr=383848-0-0'
        }
      ]
    },
    {
      navTitle: '和田玉',
      itemContent: [
        {
          liText: '手镯',
          linkParam: '/hetianyu-shoulian'
        },
        {
          liText: '金镶玉',
          linkParam: '' // ***************暂无
        },
        {
          liText: '吊坠',
          linkParam: '/hetianyu'
        },
        {
          liText: '平安扣',
          linkParam: '/hetianyu/?attr=359171-0-0'
        },
        {
          liText: '貔貅',
          linkParam: '/hetianyu/?attr=378900-0-0'
        },
        {
          liText: '观音',
          linkParam: '/hetianyu/?attr=359692-0-0'
        },
        {
          liText: '佛公',
          linkParam: '/hetianyu/?attr=359932-0-0'
        },
        {
          liText: '平安牌',
          linkParam: '/hetianyu/?attr=376346-0-0'
        },
        {
          liText: '关公',
          linkParam: '/hetianyu/?attr=379337-0-0'
        }
      ]
    }
  ]'''

# to
py_obj = demjson.decode(js_obj)
# print(py_obj)
# print(json.dumps(py_obj))
j = json.dumps(py_obj).decode("unicode-escape")
print j
