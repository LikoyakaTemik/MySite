from django.shortcuts import render
time = {"times": 0}
def Menu(request):
    if request.method == "GET":
        times = time["times"]
        data = {"times": times}
        return render(request, "Menu.html", data)
    else:
        if request.method == "POST":
            time["times"]+=1
            times = time["times"]
            data = {"times": times}
        return render(request, "Menu.html", data)