from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hey guys!!")

# def page(request):
#     return HttpResponse("Hello Everyone! Good morning.")

# def youtube(request):
#     return HttpResponse("https://www.youtube.com/watch?v=3pGAEyVtlwM&list=RD3pGAEyVtlwM&start_radio=1")
def home(request):
    return render(request,'index.html')

def about(request):
    
    return render(request,'about.html')
