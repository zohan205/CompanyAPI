from django.http import JsonResponse

def home_page(request):
    test = [
        "Ram",
        "Shyam",
        "Jodu",
        "Madhu"
        ]
    
    print(type(test))
    return JsonResponse(test,safe=False)