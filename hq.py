from requests_futures.sessions import FuturesSession
from bs4 import BeautifulSoup

def make_search_query(str_array):
    return " AND ".join(["\"" + x + "\"" for x in str_array])

def safe_divide(p, q):
    if p == 0 or q == 0:
        return 0
    else:
        return p / q

def get_result_number(request):
    try:
        soup = BeautifulSoup(request.text, "lxml")
        results_str = soup.find('div',{'id':'resultStats'}).text.split(" ")[1].replace(",","")
        return int(results_str)
    except:
        return 0

session = FuturesSession(max_workers=4)
negate = False
question_keywords = input().split(",")
if "not" in question_keywords:
    negate = True
    question_keywords.remove("not")

answer1 = input()
answer1_keywords = answer1.split(",")
answer1_urls = ["https://www.google.com/search?q=" + make_search_query(question_keywords + answer1_keywords), "https://www.google.com/search?q=" + make_search_query(answer1_keywords)]
answer1_requests = [session.get(url) for url in answer1_urls]

answer2 = input()
answer2_keywords = answer2.split(",")
answer2_urls = ["https://www.google.com/search?q=" + make_search_query(question_keywords + answer2_keywords), "https://www.google.com/search?q=" + make_search_query(answer2_keywords)]
answer2_requests = [session.get(url) for url in answer2_urls]

answer3 = input()
answer3_keywords = answer3.split(",")
answer3_urls = ["https://www.google.com/search?q=" + make_search_query(question_keywords + answer3_keywords), "https://www.google.com/search?q=" + make_search_query(answer3_keywords)]
answer3_requests = [session.get(url) for url in answer3_urls]

answer1_results = [get_result_number(request.result()) for request in answer1_requests]
answer2_results = [get_result_number(request.result()) for request in answer2_requests]
answer3_results = [get_result_number(request.result()) for request in answer3_requests]

score1 = safe_divide(answer1_results[0], answer1_results[1])
score2 = safe_divide(answer2_results[0], answer2_results[1])
score3 = safe_divide(answer3_results[0], answer3_results[1])

answer_array = [answer1, answer2, answer3]
score_array = [score1, score2, score3]

print(score1)
print(score2)
print(score3)

if negate:
    max_score = min([0, 1, 2], key=lambda x: score_array[x])
    print(answer_array[max_score])    
else:
    max_score = max([0, 1, 2], key=lambda x: score_array[x])
    print(answer_array[max_score])
