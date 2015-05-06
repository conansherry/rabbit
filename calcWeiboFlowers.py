# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:22:19 2015

@author: Administrator
"""


""" Simulate a user login to Sina Weibo with cookie.
You can use this method to visit any page that requires login.
"""


import urllib2
import re
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
    'cookie': 'your cookies'
}

idol_array = [
#1102667861
5224711950,	#	黄艺林-菟籽琳
5224726370,	#	魏雨欣-球球
1102667861,	#	马剑越-越萧
1010458283,	#	韩净丹-茉然
5224033947,	#	陈怡凡-兜兜
1117762841,	#	闫莉-女王
5224038600,	#	赵亚男-猫仔
5224664043,	#	覃婵婵-夏天
3134143705,	#	范薇-小巴
5224168666,	#	苏鑫-素素
5224027047,	#	王筱月-早喵
5224650891,	#	李-玲-铛铛
5223382374,	#	张扬-暖暖
5223403679,	#	宫冬雪-太阳
5223352142,	#	姜京京-11
5224648500,	#	吴茜-茜茜
5223603084,	#	严文竹-叶子
5312010896,	#	代雨丹-小雨

2010988863,   #	SNH48--宫泽佐江
3145968457,   #	SNH48-铃木玛莉亚-
3050708243,   #	SNH48-陈观慧
3050731261,   #	SNH48-吴哲晗
3669102477,   #	SNH48-鞠婧祎
3700231960,   #	SNH48-孟玥
3050792913,   #	SNH48-李宇琪
5221053921,   #	SNH48-陈怡馨-
3675584885,   #	SNH48-董艳芸
3050758665,   #	SNH48-徐_晨辰
5230465572,   #	SNH48-王柏硕
3668820134,   #	SNH48-沈之琳
3675573934,   #	SNH48-蒋芸
3675885002,   #	SNH48-何晓玉
5225534295,   #	SNH48-张雨鑫
5230468891,   #	SNH48-刘佩鑫
5230874533,   #	SNH48-谢妮
5227765832,   #	SNH48-杨惠婷-
3058127927,   #	SNH48-孔肖吟
3705941004,   #	SNH48-万丽娜
3050783091,   #	SNH48-张语格
3055272517,   #	SNH48-钱蓓婷
3668822213,   #	SNH48-黄婷婷
3053424305,   #	SNH48-莫寒
3675868752,   #	SNH48-冯薪朵
5103897733,   #	SNH48-陈问言
3054571717,   #	SNH48-赵嘉敏-
5228057280,   #	SNH48-徐伊人
3669076064,   #	SNH48-曾艳芬
5221220112,   #	SNH48-赵晔
3675865547,   #	SNH48-林思意
5225886388,   #	SNH48-袁丹妮
5229579490,   #	SNH48-郝婉晴
5230456780,   #	SNH48-徐晗-
3050737061,   #	SNH48-许佳琪
3668830595,   #	SNH48-陈佳莹
5228056212,   #	SNH48-许杨玉琢
3720838047,   #	SNH48-袁雨桢
3669091483,   #	SNH48-孙芮
3675601605,   #	SNH48-易嘉爱
3675603887,   #	SNH48-温晶婕
3062769307,   #	SNH48-邱欣怡
3675905275,   #	SNH48-徐子轩
3050742117,   #	SNH48-陈思
5228234876,   #	SNH48-张昕
5229864870,   #	SNH48-王璐-
5230875267,   #	SNH48-吴燕文
5225561029,   #	SNH48-杨吟雨
5227767332,   #	SNH48-李豆豆
5230466807,   #	SNH48-刘炅然-
5231168847,   #	SNH48-李清扬
5231176541,   #	SNH48-林楠
5490234918,   #	SNH48-王晓佳
5460950220,   #	SNH48-陈琳
3700233717,   #	SNH48-李艺彤
3050709151,   #	SNH48-戴萌
3669120105,   #	SNH48-陆婷
3675587802,   #	SNH48-唐安琪
3668829440,   #	SNH48-赵粤
3705939425,   #	SNH48-龚诗淇
3705935353,   #	SNH48-罗兰
5460950557,   #	SNH48-张韵雯--
5461287018,   #	SNH48-冯晓菲
5461288256,   #	SNH48-张丹三
5461873197,   #	SNH48-张瑾-
5490615346,   #	SNH48-谢天依
5460951688,   #	SNH48-李钊-
5460952383,   #	SNH48-邵雪聪-
5461873487,   #	SNH48-孙静怡
5462211905,   #	SNH48-李晶
5478873704,   #	SNH48-汪佳翎
5479678683,   #	SNH48-宋昕冉
5490958194,   #	SNH48-杨韫玉--
5491330253    #	SNH48-汪束--
]

def visit(idol, saveFile):
    url = 'http://weibo.com/u/'+str(idol)
#    url = 'http://club.starvip.weibo.com/flowerranklist?id=1005055224711950&_random=14307510135426'
    print url
    req = urllib2.Request(url, headers=headers)
    text = urllib2.urlopen(req).read()
    
    soup = BeautifulSoup(text)
    title = soup.title.string.replace(u'的微博_微博','')
    print title
    saveFile.write(title.encode('utf-8') + ' ')
    
    #使用正则表达式解析
    pattern = re.compile(r'class=\\\"W_f14 fl_color1\\\">(.*?)<')
    flowerRes = pattern.search(text)
    if flowerRes:
        flowerInfo = flowerRes.group(1)
        print flowerInfo
        saveFile.write(' '+flowerInfo)
        
        pattern = re.compile(r'lovenum\\\" >(.*?)<')
        lovenum = pattern.search(text).group(1)
        print lovenum
        saveFile.write(' '+lovenum+'\n')
    else:
        saveFile.write(' 0')
        saveFile.write(' 0\n')
    
#    pattern = re.compile(r'S_txt1(.*?)本周送花榜')
#    rankList = pattern.search(text)
#    if rankList:
#        linkInfo = rankList.group(1)
#        urlPattern = re.compile(r'href=\\\"(.*)\\\">')
#        gifturl = urlPattern.search(linkInfo).group(1).replace('\\','')
#        print gifturl
#        
#        req = urllib2.Request(gifturl, headers=headers)
#        text = urllib2.urlopen(req).read()
#        
#        urlPattern = re.compile(r'_src=\\\"(.*)\\\">')
#        gifturl = urlPattern.search(text).group(1).replace('\\','')
#        print gifturl
#        
#        req = urllib2.Request(gifturl, headers=headers)
#        text = urllib2.urlopen(req).read()
#        
#        fans = re.findall(r'class=\"fc_name S_func1\">(.*?)</a>', text)
#        flowers = re.findall(r'class=\"W_fb W_Yahei\">(.*?)</b>', text)
#        index = 0
#        saveFile.write('粉丝贡献:\n')
#        for fan in fans:
#            print fan.decode('utf-8'), flowers[index*2], flowers[index*2+1]
#            saveFile.write('  id:'+fan+' 本周送花数:'+flowers[index*2]+' 爱慕值:'+flowers[index*2+1]+'\n')
#            index = index + 1

if __name__ == '__main__':
    currentTime = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
    saveFile = open('flower_' + str(currentTime) + '.txt', 'w')
    saveFile.write(currentTime + '\n')
    for idol in idol_array:
        visit(idol, saveFile)
    saveFile.close()