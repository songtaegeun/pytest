foods ={
    "떡복이" : "순대",
    "짜장면" : "단무지",
    "라면" : "김치",
    "피자" : "피클",
    "맥주" : "땅꽁",
    "치킨" : "무",
    "삼겹살": "쌈장"
};

while(True):
    myfood = input(str(list(foods.keys()))+"중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s> 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝":
        break
    else:
        print("없음")