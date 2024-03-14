# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import dropbox
from .models import Question, TestCase
from io import BytesIO

def read_file_content(request):
    question = Question.objects.get(id=1)
    testcases = TestCase.objects.filter(question=question)
    op={}
    for testcase in testcases:
        op[testcase.input_data.name] = testcase.input_data.read().decode('utf-8').strip()

    return JsonResponse(op)
    # for i in testcase:
    #     # with open(i.input_data.path, "r") as correct_output:
    #     #     print(correct_output.read().strip())
    #     print(i.input_data.read().decode('utf-8').strip())
    #     print("vm1",i.input_data.path)
    #     op[i.input_data]=i.input_data.read().decode('utf-8').strip()


    # return HttpResponse(f"done")
