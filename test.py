import random
import re


# 문장을 입력하세요: cat dog

# 모의고사 문제: cat ___ 

# 답: dog

# 정답 / 오답 



def normalization(text):
    text = re.sub(r"\([\w\s$\.]+\)",'', text)
    text = re.sub(r"[,]+",'', text)
    text = re.sub(r"([A-z]+)\.([A-z]+)","\\1_\\2",text)
    text = re.sub(r"(\w+)(\.)",'\\1 \\2', text)
    text = re.sub(r"([A-z]+)_([A-z]+)","\\1.\\2",text)
    text = re.sub(r'\s+',' ',text)
    return text


def isAlphabet(text):
    return re.fullmatch(r'[A-z]+\.?',text)

def choice_random(index_list:list, n=1):
    return random.sample(index_list, n)



def generate_problem(sentence:str , sub_str="_______", n=1):
    words = sentence.split()
    eng_idxs = [ i for i , word in  enumerate(words) if isAlphabet(word)]
    picked_idxs = choice_random(eng_idxs,n)
    
    answers = []
    for picked_idx in picked_idxs:
        answers.append(words[picked_idx])
        words[picked_idx]= sub_str
    
    return " ".join(words),  answers

sentences=[]
with open('examples.txt','r') as f:
    
    for line in f:
        line = normalization(line.strip()) 
        sentences.append(line)


problems = []
N= 5
for sentence in sentences:
    problem, answer = generate_problem(sentences[0],n=N)
    
    problems.append((problem, answer))
    # print(f"sentence: {sentences[0]}\nproblem: {problem}\nanswer: {answer}\n")

total_score=0
for item in problems:
    
    try:
        problem, answer_list = item
        
        score = 0
        print(f"문제: \n{problem}")
        print(f"정답: {', '.join(answer_list)}")

        answer_trys = input(f"정답: ")
        
        answer_trys_list = answer_trys.split(',')
        pair = zip(answer_list,answer_trys_list)
        for answer, answer_try in pair:
            if answer.lower() == answer_try.strip().lower():
                score += 1
        print(f"점수: [{score} / {N} ]\n")
        total_score += score # total_score = total_score + score
    except KeyboardInterrupt:
        break 
print(f"\n\n최종점수: {total_score} ")
   
