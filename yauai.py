import requests
import json
import time
import random
from wxauto import WeChat

# 获取百度的 access_token
def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ZZ934SoFKcdKowzRRuXy6l7R&client_secret=YSS5qEDZANHrHYayT2U7amFvcQDJt2VY"
    response = requests.get(url)
    return response.json().get("access_token")


# 获取百度 AI 的回复
def get_baidu_ai_response(content):
    access_token = get_access_token()
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token={access_token}"
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    })
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return response.json()['result']
    else:
        return "对不起，无法获取AI回复。"


# 设置微信自动回复
def main():
    wx = WeChat()

    self_introduction='输入AI提示词:yau或直接@ 以使用若至AI'

    listen_list = []
    listen_list.append('好香的兄弟')

    for mem in listen_list:
        wx.AddListenChat(who=mem)
        wx.SendMsg(msg=self_introduction,who=mem)

    send_contents = [
        '',
        '我們的教育確有問題！',
        '這種成績，令人汗顔！',
        '我宣佈你已經不是我的學生了',
        '已經到了無恥的地步',
        '羞也不羞',
        '好可愛的孩子們',
        '獎勵一塊華爲手錶',
        '聞鷄起舞！',
        '季理真花了五年寫一本書，刚刚出版，'
        '講到很多和我有關而又完全錯误的事情。大多詆毁我的做人原则，無非向楊振寧拍馬屁!大概知道自己無恥，從頭到尾，秘密行動，書出版了.都沒有告訴過我!已經到了無恥的地步，'
        '我宣布他已經不是我的學生了',
        '由家長牵着手一步一步走的孩子始终长不大!',
        '这个是“富不过三代”的理由，中国歷代皇帝一般在三代以後不行也是同様理由。好的学者要在学術的天地中闖出一條有自己特色的路!开始時在導師幫忙，开始走研究的路，以后就要吸收全世界学者的養分，向前冲警，才有大成!',
        '现在同学还未成熟，就自满，不学习最前沿的学問，守着一畝三分地，如何成大器?(其实連一畝三分地都还没有.!)',
        '章台柳，章台柳，昔日青青今在否。纵使长條似旧垂，也应攀折他人手。',
        '1976 年我剛結婚，完成了calabi猜想的证明。当时正在考虑如何用它做一些事情。我聼说 Mumford在 Irvine 做演讲，我不知道他要讲甚么，但是从我家里开事子聴演讲，一程要开重三个钟，我剛到落杉机，不熟地方，还是一个人开重子去聽课。一个钟头的演讲，讓我知道代数儿何学家注意的前沿問题，，發现它和我做好的 calabiconjecture 有密切关系，我可以解决它。这个演讲，给我一个机会一举成名!我引进微分几何的方法到代数几何，就是这个時候。从此mumford 对我印象深刻。以后他在fields committee 解释我的工作。这个机遇不可特意去求!但是假如我不願意浪費六個鐘頭開車子，恐怕这些工作会给别人做去了!',
        '今日中国，强敞环伺，科技卡膀，海疆未靖，幼苗未长，此誠危急存亡之秋也。中央领导，日夜焦虑。基础未成，壯士扼腕求真書院子弟，必须放眼世界，求天人之際，建我中华筹学大業，引领全国。何其斤斤计较於一餐之饱食，抱怨建連?昔日孔子称道颜回，豈在一飲一食乎?德業之未張，有志者之耻也!求真子弟，必须寻天人樂處，拓万古心胸!\n發自我的手機',
        '求真的同學們不許打手槍！傷身而且影響你的數學思維！這樣會讓你半年一篇四大都沒有！\n發自我的手機',
        '【[补档]求真书院恩情课文《丘爷爷用初等数学证明卡拉比-丘猜想》】 https://www.bilibili.com/video/BV11LSiYGEcx/?share_source=copy_web&vd_source=4020d4eb9905c14ca36ac9e6e6da109a',
        '尼丘孕灵兮横流启圣，\n洙泗风传兮大道始正。\n忠恕仁爱兮君臣父子，\n允执厥中兮至善始止。\n传习六艺兮固守五伦，\n行遵礼乐兮泛爱仁人。\n春秋断恶兮易测玄机，\n存亡继绝兮东西可依。\n夫子高山兮百代嘉名，\n后学轨范兮万世太平。\n儒道昭远兮华夏纪纲，\n绳墨规矩兮求真不忘！',
    ]#18

    funny_things = [
        '【头 尖 尖 阿 诺】 https://www.bilibili.com/video/BV1miqBYpEb7/',
        '【震颤症】 https://www.bilibili.com/video/BV185C2YwEkJ/',
        '【越来越多面数的韭菜盒子落在说的道理头上】 https://www.bilibili.com/video/BV1rBzgYNEP5/',
        '【圣诞节那天发给你的好朋友吧~】 https://www.bilibili.com/video/BV18tkGYhEvm/',
    ]
    
    wait = 3  # 等待时间
    hint='yau'
    
    while True:
        msgs = wx.GetListenMessage()

        if msgs == {}:
            continue

        for chat in msgs:
            one_msgs = msgs.get(chat)
            for msg in one_msgs:
                msgtype = msg.type    
                if msgtype == 'sys' and msg.content != '以下为新消息':
                    break
                if msgtype == 'friend':
                    print(f'[{msg.sender_remark}]: {msg.content}')
                    
                    # 调用百度 AI 获取回复
                    if hint or '@丘成桐' in msg.content:  # 可以根据实际需要更改条件
                        ai_response = get_baidu_ai_response(msg.content)
                        chat.SendMsg(ai_response)
                        continue
                    
                    # 根据其他关键词发送预设的内容
                    if '手枪' in msg.content or '说过' in msg.content:
                        chat.SendMsg(send_contents[16])
                        continue
                    elif '滚' in msg.content:
                        chat.SendMsg(send_contents[3])
                        continue
                    elif '恩情' in msg.content:
                        chat.SendMsg(send_contents[17])
                        continue
                    elif '奖励' in msg.content or '华为' in msg.content:
                        chat.SendMsg(send_contents[7])
                        continue
                    elif '教育' in msg.content:
                        chat.SendMsg(send_contents[1])
                        continue
                    elif '6' in msg.content:
                        chat.SendMsg(send_contents[2])
                        continue
                    elif '自己' in msg.content or '不熟' in msg.content:
                        chat.SendMsg(send_contents[14])
                        continue
                    elif '学生' in msg.content:
                        chat.SendMsg(send_contents[9])
                        continue
                    elif '发自' in msg.content or '發自' in msg.content:
                        chat.SendMsg(send_contents[4])
                        continue
                    elif '早' in msg.content or '起' in msg.content:
                        chat.SendMsg(send_contents[8])
                        continue
                    elif '先师' in msg.content:
                        chat.SendMsg(send_contents[18])
                        continue
                    elif '诗' in msg.content:
                        chat.SendMsg(send_contents[13])
                        continue
                    elif '喜欢' in msg.content or '爱' in msg.content:
                        chat.SendMsg(send_contents[5])
                        continue
                    elif '抽象' in msg.content or '视频' in msg.content:
                        chat.SendMsg(random.choice(funny_things))
                        continue

        time.sleep(wait)


if __name__ == '__main__':
    main()
