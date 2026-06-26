from django.shortcuts import render

def home(request):
    message = ""
    result = ""

    if request.method == "POST":
        message = request.POST.get("message")

        spam_words = ["win", "free", "prize", "money", "offer"]

        if any(word in message.lower() for word in spam_words):
            result = "Spam Detected!"
        else:
            result = "Not Spam"

    return render(request, "home.html", {
        "message": message,
        "result": result
    })