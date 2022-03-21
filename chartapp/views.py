from django.shortcuts import render, redirect
from . models import Customers, Product
from . forms import ProductForm
from django.db.models import Count
from django.db.models import Sum

# Create your views here.
def index(request):
    
    total = Customers.objects.aggregate(total_price=Sum('TotalCharges'))
    # customers = Customers.objects.values('PaymentMethod').order_by('PaymentMethod').annotate(name_count=Count('PaymentMethod')).filter(name_count__gt=1)
    customers = Customers.objects.all().values('PaymentMethod').annotate(total=Count('PaymentMethod'))
    
    customers2 = Customers.objects.values('Area').annotate(name_count=Count('Area')).filter(name_count__gt=1).order_by('-Area')
    customers3 = Customers.objects.values('InternetService').annotate(name_count=Count('InternetService')).filter(name_count__gt=1)
    customers4 = Customers.objects.values('Area').order_by('Area').annotate(total_price=Sum('TotalCharges')).order_by('-Area')
    customers5 = Customers.objects.values('Area').annotate(total_fault=Sum('FaultPowerOutagePerMonth')).order_by('-Area')
    customers6 = Customers.objects.values('Area').annotate(total_fault2=Sum('FaultCableCutPerMonth')).order_by('-Area')
    customers7 = Customers.objects.aggregate(totaldata=Count('id'))
    Mdata = Customers.objects.filter(MultipleLines__startswith='Y')  
    count = 0
    for i in Mdata:
        count = count + 1 
    customers8 = count
    Mdata2 = Customers.objects.filter(PhoneService__startswith='Y')  
    count2 = 0
    for i in Mdata2:
        count2 = count2 + 1 
    customers9 = count2
    Mdata3 = Customers.objects.filter(StreamingTV__startswith='Y')  
    count3 = 0
    for i in Mdata3:
        count3 = count3 + 1 
    customers10 = count3
    Mdata4 = Customers.objects.filter(StreamingMovies__startswith='Y')  
    count4 = 0
    for i in Mdata4:
        count4 = count4 + 1 
    customers11 = count4
    Mdata5 = Customers.objects.filter(TechSupport__startswith='Y')  
    count5 = 0
    for i in Mdata5:
        count5 = count5 + 1 
    customers12 = count5
    Mdata6 = Customers.objects.filter(PaperlessBilling__startswith='Y')  
    count6 = 0
    for i in Mdata6:
        count6 = count6 + 1 
    customers13 = count6
  
  
    # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))
    
    context = {
        "total":total,
        "customers":customers,
        "customers2":customers2,
        "customers3":customers3,
        "customers4":customers4,
        "customers5":customers5,
        "customers6":customers6,
        "customers7":customers7,
        "customers8":customers8,
        "customers9":customers9,
        "customers10":customers10,
        "customers11":customers11,
        "customers12":customers12,
        "customers13":customers13,
    }
    return render(request, 'chartapp/index.html', context)

def databoard(request):
    alldata = Customers.objects.all()
    context = {
        "alldata":alldata,
    }
    return render(request, 'chartapp/databoard.html', context)

