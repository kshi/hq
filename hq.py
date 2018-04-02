#key = "AIzaSyDIhNXRzrUidGyxOrZqRwJp3st4kjiK45A"
import requests
from bs4 import BeautifulSoup

def make_search_query(str_array):
    return " ".join(["\"" + x + "\"" for x in str_array])

def get_result_number(html):
    soup = BeautifulSoup(html.text,"lxml")
    results_str = soup.find('div',{'id':'resultStats'}).text.split(" ")[1].replace(",","")
    return int(results_str)

question_keywords = input().split(",")
answer1 = input()
answer1_keywords = answer1.split(",")
p1 = requests.get("https://www.google.com/search?q=" + make_search_query(question_keywords + answer1_keywords))
q1 = requests.get("https://www.google.com/search?q=" + make_search_query(answer1_keywords))
answer2 = input()
answer2_keywords = answer2.split(",")
p2 = requests.get("https://www.google.com/search?q=" + make_search_query(question_keywords + answer2_keywords))
q2 = requests.get("https://www.google.com/search?q=" + make_search_query(answer2_keywords))
answer3 = input()
answer3_keywords = answer3.split(",")
p3 = requests.get("https://www.google.com/search?q=" + make_search_query(question_keywords + answer3_keywords))
q3 = requests.get("https://www.google.com/search?q=" + make_search_query(answer3_keywords))
score1 = get_result_number(p1) / get_result_number(q1)
score2 = get_result_number(p2) / get_result_number(q2)
score3 = get_result_number(p3) / get_result_number(q3)
answer_array = [answer1, answer2, answer3]
score_array = [score1, score2, score3]
print(score1)
print(score2)
print(score3)
max_score = max([0, 1, 2], key=lambda x: score_array[x])
print(answer_array[max_score])
