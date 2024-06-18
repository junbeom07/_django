from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

grade_db = [
  {
    "_id": "b67c41fd-6112-46cb-A9c4-df75eb8e700e",
    "index": "1",
    "teacher": "모시호",
    "phone": "010-6958-9650",
    "grade": "3",
    "num": "8",
    "contents": "뼈 국가안위에 하지 예우에 20일을 소리다이것은 뼈 끝에. 살 국민의"
  },
  {
    "_id": "1a3d58bb-fd20-4241-A0b9-aa619b928cf3",
    "index": "2",
    "teacher": "뢰승기",
    "phone": "010-7272-5750",
    "grade": "3",
    "num": "1",
    "contents": "뛰노는 위하여서 아니면 심장의 날카로우나 아니하며 정한 가을. 관하여 만물은"
  },
  {
    "_id": "3fdc9481-9190-4a37-Abf5-1c42e017cda5",
    "index": "3",
    "teacher": "로찬솔",
    "phone": "010-7367-0057",
    "grade": "3",
    "num": "6",
    "contents": "개인과 싸인 사는가 조직·권한 기쁘며 헌법재판소에 새워 무덤. 기관의 인생에"
  },
  {
    "_id": "37b0607f-52ef-40f8-A15b-4c9acf2742a6",
    "index": "4",
    "teacher": "예선미",
    "phone": "010-3851-0938",
    "grade": "1",
    "num": "11",
    "contents": "발생한다 타인의 연임할 정하여 만료되는 생활의 존중함을 기타의. 끝까지 봅니다"
  },
  {
    "_id": "287ba956-ff87-4ac5-Bf7d-3c218a4b06fe",
    "index": "5",
    "teacher": "당정인",
    "phone": "010-5582-6405",
    "grade": "2",
    "num": "7",
    "contents": "임시회는 통하여 법률에 위하여 계집애들의 안전보장과 아니한 기준은. 석가는 의한"
  }
]
def index(request):
    return render(request,'main/index.html')

def jejuohyun(request):
    return render(request,'main/jejuohyun.html')

def g_1st(request):
    return render(request,'main/g_1st.html')

def g_2nd(request):
    return render(request,'main/g_2nd.html')

def g_3rd(request):
    return render(request,'main/g_3rd.html')

def my_page(request):
    return render(request,'main/my page.html')

def grade(request):
    return render(request,'main/grade.html')


index, jejuohyun, g_1st, g_2nd, g_3rd, my_page