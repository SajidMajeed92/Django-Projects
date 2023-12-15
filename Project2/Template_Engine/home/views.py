from django.shortcuts import render

# Create your views here.
# Create your views here.
def home(request):
    
    peoples = [
        {'name':'Muhammad Hussain','Profession':'Mechanical Engineer','age':24},
        {'name':'Farooq','Profession':'Software Engineer','age':26},
        {'name':'Orhan Farooq','Profession':'Student','age':17},
        {'name':'Usama','Profession':'Mechanical Engineer','age':24},
        {'name':'Asif','Profession':'Network Engineer','age':26},
        {'name':'Waqas','Profession':'Database Engineer','age':18},
    ]
    return render(request,"index.html" ,context={'peoples':peoples})