from django.shortcuts import render
from .comparealgorithm import compare_model
# Create your views here.

def compare_time(start, end):
    s = str(start).split(":")
    e = str(end).split(":")
    res = ((int(s[0]) * 60) + int(s[1])) - ((int(e[0]) * 60) + int(e[1]))
    print(res)
    return res
def index(request):
    pid = request.GET.get("pid", "0")
    start = request.GET.get("start", "")
    end = request.GET.get("end", "")
    car_type = request.GET.get("car_type", "")
    ensure_type = request.GET.get("ensure_type", "")
    driving_km = request.GET.get("driving_km", "")
    rental_day = request.GET.get("rental_day", "")
    print(start,end)
    error = ""
    greencar = list()
    socar = list()

    if int(pid):
        if compare_time(start, end) > 0 :
            context = {
                'start' : start,
                'end' : end,
                'car_type': car_type,
                'ensure_type' : ensure_type,
                'driving_km' : driving_km,
                'rental_day' : rental_day,
                'error' : "대여시작시간이 대여종료시간보다 빠릅니다."
            }
            return render(request, "index.html", context)

        if car_type == "중형":
            error = "쏘카는 대여할 수 있는 중형 차량 없음!"

        result = compare_model(str(start), str(end), car_type, int(ensure_type), int(driving_km), rental_day)
        print(result[0], result[1])

        if result[0]:
            for i in range(len(result[0]["car"])):
                greencar.append(result[0]["car"][i])
                greencar.append(int(result[0]["totalpay"][i]))
                greencar.append(result[0]["coupon"][i])

        if result[1]:
            for i in range(len(result[1]["car"])):
                socar.append(result[1]["car"][i])
                socar.append(int(result[1]["totalpay"][i]))
                socar.append(result[1]["coupon"][i])

    context = {
        'start' : start,
        'end' : end,
        'car_type': car_type,
        'ensure_type' : ensure_type,
        'driving_km' : driving_km,
        'rental_day' : rental_day,
        'error' : error,
        'greencar': greencar,
        'socar': socar,
    }
    return render(request, "index.html", context)