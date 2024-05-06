from django.shortcuts import render
from django.http.response import JsonResponse
import openai
from core.settings import API_KEY
from rest_framework import status

# Create your views here.

openai.api_key=API_KEY

def index(request):
    if is_ajax(request=request):
        que=request.POST.get("question")
        print(que)

        ask = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": que}
        ]
        )

        if ask.choices[0]["message"]!=None:
            answer = ask.choices[0]["message"]
        else :
            answer = None
    
        if not answer:
            return JsonResponse({'msg':'Server error'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'msg':que})
    return render(request, 'index.html')

#for ajax
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'