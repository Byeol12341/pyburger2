# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def burger_list(request):
    return render(request, "burger_list.html")