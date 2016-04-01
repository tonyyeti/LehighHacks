# radar.py, by Tong, 4/1/2016 10:15 AM
# -*- coding=UTF-8 -*-

import pygal
from pygal.style import CleanStyle
from random import *

twname = 'KingJames'

def tweet_to_traits(twiiter_name):
    # consumer_key =  'PwR3kv9Zk8D1upqhjMb7Jo2gV'
    # consumer_secret = 'lpVsyVkrm4aucksA4DaNEmeH14RGJlsv3R0GmQ3cnmsIo9y08p'
    # access_token = '715914463531106305-W0ePPSizVVA1yfCX0geQfI1TzU7wdgd'
    # access_token_secret = 'otwoSgwU4w9M6LBFHTVrEIvr9V7hmVGef9UKw8wngGMYx'
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)
    # tweets = []
    # times = []
    # username = 'KingJames'
    # new_tweets = api.user_timeline(screen_name=username, count=200)
    # tweets.extend([i.text for i in new_tweets])
    # times.extend([i.created_at for i in new_tweets])
    # for i, tweet in enumerate(tweets):
    #     print tweet
    json1 = {
      "id": "*UNKNOWN*",
      "source": "*UNKNOWN*",
      "word_count": 2845,
      "word_count_message": "输入中包含 2,845 个字。但至少需要 3,500 个字，最好不少于 6,000 个字，这样才能得出有统计意义的估算结果",
      "processed_lang": "en",
      "tree": {
        "id": "r",
        "name": "root",
        "children": [
          {
            "id": "personality",
            "name": "大五人格模式",
            "children": [
              {
                "id": "Neuroticism_parent",
                "name": "情感范围",
                "category": "personality",
                "percentage": 0.2760242517284165,
                "children": [
                  {
                    "id": "Openness",
                    "name": "开放性",
                    "category": "personality",
                    "percentage": 0.6953228852166657,
                    "sampling_error": 0.0543160212,
                    "children": [
                      {
                        "id": "Adventurousness",
                        "name": "冒险",
                        "category": "personality",
                        "percentage": 0.7513763142988521,
                        "sampling_error": 0.0471895294
                      },
                      {
                        "id": "Artistic interests",
                        "name": "审美",
                        "category": "personality",
                        "percentage": 0.620985360427309,
                        "sampling_error": 0.096355655
                      },
                      {
                        "id": "Emotionality",
                        "name": "情感丰富",
                        "category": "personality",
                        "percentage": 0.3446450502558342,
                        "sampling_error": 0.0446753358
                      },
                      {
                        "id": "Imagination",
                        "name": "想象力",
                        "category": "personality",
                        "percentage": 0.604427806387743,
                        "sampling_error": 0.05884602
                      },
                      {
                        "id": "Intellect",
                        "name": "智力",
                        "category": "personality",
                        "percentage": 0.7341639904564015,
                        "sampling_error": 0.0512917252
                      },
                      {
                        "id": "Liberalism",
                        "name": "挑战权威",
                        "category": "personality",
                        "percentage": 0.5763137903712697,
                        "sampling_error": 0.0779455458
                      }
                    ]
                  },
                  {
                    "id": "Conscientiousness",
                    "name": "尽责性",
                    "category": "personality",
                    "percentage": 0.6959945150552648,
                    "sampling_error": 0.0703944962,
                    "children": [
                      {
                        "id": "Achievement striving",
                        "name": "追求成就",
                        "category": "personality",
                        "percentage": 0.6722011695808267,
                        "sampling_error": 0.09150909460000001
                      },
                      {
                        "id": "Cautiousness",
                        "name": "审慎",
                        "category": "personality",
                        "percentage": 0.6239061953013362,
                        "sampling_error": 0.08486678460000001
                      },
                      {
                        "id": "Dutifulness",
                        "name": "责任感",
                        "category": "personality",
                        "percentage": 0.6655356258869819,
                        "sampling_error": 0.0564758354
                      },
                      {
                        "id": "Orderliness",
                        "name": "条理性",
                        "category": "personality",
                        "percentage": 0.3826836710412458,
                        "sampling_error": 0.0651927246
                      },
                      {
                        "id": "Self-discipline",
                        "name": "自律",
                        "category": "personality",
                        "percentage": 0.7760980599748473,
                        "sampling_error": 0.043552813
                      },
                      {
                        "id": "Self-efficacy",
                        "name": "自我效能",
                        "category": "personality",
                        "percentage": 0.8090503428859004,
                        "sampling_error": 0.0852679312
                      }
                    ]
                  },
                  {
                    "id": "Extraversion",
                    "name": "外向性",
                    "category": "personality",
                    "percentage": 0.5218785977296307,
                    "sampling_error": 0.0517002538,
                    "children": [
                      {
                        "id": "Activity level",
                        "name": "活力程度",
                        "category": "personality",
                        "percentage": 0.6325875491704783,
                        "sampling_error": 0.0718298356
                      },
                      {
                        "id": "Assertiveness",
                        "name": "独断性",
                        "category": "personality",
                        "percentage": 0.5530487935927747,
                        "sampling_error": 0.0767379834
                      },
                      {
                        "id": "Cheerfulness",
                        "name": "热情",
                        "category": "personality",
                        "percentage": 0.33554373387693726,
                        "sampling_error": 0.0960853072
                      },
                      {
                        "id": "Excitement-seeking",
                        "name": "寻求刺激",
                        "category": "personality",
                        "percentage": 0.3340076354146114,
                        "sampling_error": 0.076655836
                      },
                      {
                        "id": "Friendliness",
                        "name": "开朗",
                        "category": "personality",
                        "percentage": 0.6340221435738663,
                        "sampling_error": 0.069672738
                      },
                      {
                        "id": "Gregariousness",
                        "name": "合群性",
                        "category": "personality",
                        "percentage": 0.5893888701456678,
                        "sampling_error": 0.054313705600000005
                      }
                    ]
                  },
                  {
                    "id": "Agreeableness",
                    "name": "宜人性",
                    "category": "personality",
                    "percentage": 0.43024411082420816,
                    "sampling_error": 0.0899906684,
                    "children": [
                      {
                        "id": "Altruism",
                        "name": "利他",
                        "category": "personality",
                        "percentage": 0.7511848389056778,
                        "sampling_error": 0.0654687576
                      },
                      {
                        "id": "Cooperation",
                        "name": "合作",
                        "category": "personality",
                        "percentage": 0.6745408190598642,
                        "sampling_error": 0.0748606568
                      },
                      {
                        "id": "Modesty",
                        "name": "谦逊",
                        "category": "personality",
                        "percentage": 0.37598650571521763,
                        "sampling_error": 0.0508480908
                      },
                      {
                        "id": "Morality",
                        "name": "坚定",
                        "category": "personality",
                        "percentage": 0.46814283412090957,
                        "sampling_error": 0.058208667400000004
                      },
                      {
                        "id": "Sympathy",
                        "name": "同情心",
                        "category": "personality",
                        "percentage": 0.6909636063704816,
                        "sampling_error": 0.08967030620000001
                      },
                      {
                        "id": "Trust",
                        "name": "信任",
                        "category": "personality",
                        "percentage": 0.6429928373902652,
                        "sampling_error": 0.051157015
                      }
                    ]
                  },
                  {
                    "id": "Neuroticism",
                    "name": "情感范围",
                    "category": "personality",
                    "percentage": 0.2760242517284165,
                    "sampling_error": 0.0826669734,
                    "children": [
                      {
                        "id": "Anger",
                        "name": "暴躁",
                        "category": "personality",
                        "percentage": 0.2666265857518407,
                        "sampling_error": 0.08674774560000001
                      },
                      {
                        "id": "Anxiety",
                        "name": "易焦虑",
                        "category": "personality",
                        "percentage": 0.27580125250983006,
                        "sampling_error": 0.0505291766
                      },
                      {
                        "id": "Depression",
                        "name": "忧郁",
                        "category": "personality",
                        "percentage": 0.21617048392094368,
                        "sampling_error": 0.053473036
                      },
                      {
                        "id": "Immoderation",
                        "name": "无节制",
                        "category": "personality",
                        "percentage": 0.3158539947221221,
                        "sampling_error": 0.0493977548
                      },
                      {
                        "id": "Self-consciousness",
                        "name": "自我意识",
                        "category": "personality",
                        "percentage": 0.1964571532673837,
                        "sampling_error": 0.051508329799999995
                      },
                      {
                        "id": "Vulnerability",
                        "name": "易受压力",
                        "category": "personality",
                        "percentage": 0.2967627708795476,
                        "sampling_error": 0.07836292660000001
                      }
                    ]
                  }
                ]
              }
            ]
          },
          {
            "id": "needs",
            "name": "需要",
            "children": [
              {
                "id": "Practicality_parent",
                "name": "实用",
                "category": "needs",
                "percentage": 0.16691401481149115,
                "children": [
                  {
                    "id": "Challenge",
                    "name": "挑战",
                    "category": "needs",
                    "percentage": 0.6143429617299166,
                    "sampling_error": 0.07759668659999999
                  },
                  {
                    "id": "Closeness",
                    "name": "亲密",
                    "category": "needs",
                    "percentage": 0.4506690761436349,
                    "sampling_error": 0.0766511708
                  },
                  {
                    "id": "Curiosity",
                    "name": "好奇心",
                    "category": "needs",
                    "percentage": 0.31721807571271216,
                    "sampling_error": 0.10924061580000001
                  },
                  {
                    "id": "Excitement",
                    "name": "刺激",
                    "category": "needs",
                    "percentage": 0.269919546159895,
                    "sampling_error": 0.09984143720000001
                  },
                  {
                    "id": "Harmony",
                    "name": "和谐",
                    "category": "needs",
                    "percentage": 0.19942297093529562,
                    "sampling_error": 0.0986701594
                  },
                  {
                    "id": "Ideal",
                    "name": "理想",
                    "category": "needs",
                    "percentage": 0.4066185167254665,
                    "sampling_error": 0.08967519
                  },
                  {
                    "id": "Liberty",
                    "name": "自由",
                    "category": "needs",
                    "percentage": 0.25422407904969657,
                    "sampling_error": 0.13338811720000002
                  },
                  {
                    "id": "Love",
                    "name": "爱",
                    "category": "needs",
                    "percentage": 0.24024482542469572,
                    "sampling_error": 0.0909738898
                  },
                  {
                    "id": "Practicality",
                    "name": "实用",
                    "category": "needs",
                    "percentage": 0.16691401481149115,
                    "sampling_error": 0.07994699300000001
                  },
                  {
                    "id": "Self-expression",
                    "name": "自我表现",
                    "category": "needs",
                    "percentage": 0.29094127605562586,
                    "sampling_error": 0.07514864660000001
                  },
                  {
                    "id": "Stability",
                    "name": "稳定性",
                    "category": "needs",
                    "percentage": 0.3441191073401852,
                    "sampling_error": 0.097250871
                  },
                  {
                    "id": "Structure",
                    "name": "结构",
                    "category": "needs",
                    "percentage": 0.3142495311397757,
                    "sampling_error": 0.0733410516
                  }
                ]
              }
            ]
          },
          {
            "id": "values",
            "name": "价值观",
            "children": [
              {
                "id": "Openness to change_parent",
                "name": "对改变持开放态度",
                "category": "values",
                "percentage": 0.22521246966430405,
                "children": [
                  {
                    "id": "Conservation",
                    "name": "保守",
                    "category": "values",
                    "percentage": 0.6953517676109432,
                    "sampling_error": 0.0646736114
                  },
                  {
                    "id": "Openness to change",
                    "name": "对改变持开放态度",
                    "category": "values",
                    "percentage": 0.22521246966430405,
                    "sampling_error": 0.0600118322
                  },
                  {
                    "id": "Hedonism",
                    "name": "享乐主义",
                    "category": "values",
                    "percentage": 0.27294559258067336,
                    "sampling_error": 0.1246786062
                  },
                  {
                    "id": "Self-enhancement",
                    "name": "自我提高",
                    "category": "values",
                    "percentage": 0.69276055455273,
                    "sampling_error": 0.094260322
                  },
                  {
                    "id": "Self-transcendence",
                    "name": "自我超越",
                    "category": "values",
                    "percentage": 0.5730308758871009,
                    "sampling_error": 0.0722276704
                  }
                ]
              }
            ]
          }
        ]
      },
      "warnings": [
        {
          "message": "输入中包含 2,845 个字。但至少需要 3,500 个字，最好不少于 6,000 个字，这样才能得出有统计意义的估算结果",
          "id": "WORD_COUNT_MESSAGE"
        }
      ]
    }
    traits_name = []
    traits = []
    if twiiter_name == 'KingJames':
        for i in range(5):
            traits_name.append(json1['tree']['children'][0]['children'][0]['children'][i]['id'])
            traits.append(json1['tree']['children'][0]['children'][0]['children'][i]['percentage'])
    else:
        traits = [random(), random(), random(), random(), random()]
    return traits

def radar_charter(trait):
    radar_chart = pygal.Radar(fill=True, style=CleanStyle,range=(.0001, 1))
    radar_chart.title = 'Big 5 Personality traits'
    radar_chart.x_labels = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
    radar_chart.add('Your Personality Traits', trait)
    radar_chart.render_to_file('radar.svg')

def risk_level(traits):
    return (traits[0] + traits[2] - traits[1] - traits[3] - traits[4] +3)/.5

def target_volatility(level):
    return level/10*0.06

target_vola = target_volatility(risk_level(tweet_to_traits(twname)))

