from konlpy.tag import Okt
okt=Okt()
corpus = "상품경제를 발전시킨 은의 영구성을 제시하고 있어 그 효용적 측면을 간과하지 않고 있다."
print(okt.morphs(corpus, stem=True))

keyword=[['없어지다+않다','영구적','보존'],['은'],['상품', '시장', '경제'], ['발전'], ['효용'], ['고려', '강조']]
#corpus = "없어지다"
#print(okt.morphs(corpus, stem=True))
print(keyword[0][1].split('+'))

def iscore(self, essay, threshold):
    self.essay=essay
    self.threshold=threshold
    words=okt.morphs(essay, stem=True)
    number=0
    for i in range(len(keyword)):
        checker=0
        for j in range(len(keyword[i])):
            phrase=keyword[i][j].split('+')
            if len(phrase)>1:
                for k in range(len(phrase)):
                    if phrase[k] in words:
                        checker=1
                    else:
                        checker=0
            if len(phrase)==1:
                if phrase in words:
                    checker=1
            if checker==1:
                number+=1
    percent=number/len(keyword)
    if percent<threshold:
        print("fail with %f words",percent)
    else:
        print("success with %f words", percent)
    
    
a.score("상품경제를 발전시킨 은의 영구성을 제시하고 있어 그 효용적 측면을 간과하지 않고 있다.",0.5)

def score(self, threshold):
    self.threshold=threshold
    words=okt.morphs(self, stem=True)
    number=0
    for i in range(len(keyword)):
        checker=0
     for j in range(len(keyword[i])):
            phrase=keyword[i][j].split('+')
            if len(phrase)>1:
                for k in range(len(phrase)):
                    if phrase[k] in words:
                        checker=1
                    else:
                        checker=0
            if len(phrase)==1:
                if phrase in words:
                    checker=1
            if checker==1:
                number+=1
    percent=number/len(keyword)
    if percent<self.threshold:
        print("fail with %f words",percent)
    else:
        print("success with %f words", percent)

a=["상품경제를 발전시킨 은의 영구성을 제시하고 있어 그 효용적 측면을 간과하지 않고 있다."]
a.score(0.5)
    
    
