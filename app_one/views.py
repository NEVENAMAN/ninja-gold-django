from django.shortcuts import render ,redirect
from datetime import datetime
import random

def index(request):

    request.session['totalGold'] = 0
    request.session['farmGold'] = 0
    request.session['caveGold'] = 0
    request.session['houseGold'] = 0
    request.session['casinoGold'] = 0
    request.session['activitesCasino'] = 0
    request.session['casinoCurrentGoldsend'] = []
    request.session['activeCurrentGoldsend'] = []
    return render(request,'index.html')

def collectGold(request):
    request.session['activeCurrentGold'] = ''
    request.session['casinoCurrentGold'] = ''

    if request.POST['which_form'] == 'farm' :
        request.session['farmGold'] = random.randint(10,15)
        request.session['totalGold'] += int(request.session['farmGold'])
        print(request.session['totalGold'])
        request.session['activeCurrentGold'] ='Earned '+ str(int(request.session['farmGold'])) +' golds from the farm !  '+ str(datetime.now())

    elif request.POST['which_form'] == 'cave':
        request.session['caveGold'] = random.randint(5,10)
        request.session['totalGold'] += int(request.session['caveGold'])
        request.session['activeCurrentGold'] ='Earned '+ str(int(request.session['caveGold'])) +' golds from the cave !  '+ str(datetime.now())

    elif request.POST['which_form'] == 'house':
        request.session['houseGold'] = random.randint(2,5)
        request.session['totalGold'] += int(request.session['houseGold'])
        request.session['activeCurrentGold'] ='Earned '+ str(int(request.session['houseGold'])) +' golds from the house !  '+ str(datetime.now())

    elif request.POST['which_form'] == 'casino':
        request.session['casinoGold'] = random.randint(-50,50)
        request.session['totalGold'] += int(request.session['casinoGold'])
        request.session['casinoCurrentGold'] ='Earned '+ str(int(request.session['casinoGold'])) +' golds from the casino !  '+ str(datetime.now())

    if request.session['casinoCurrentGold']!=None:     
        request.session['casinoCurrentGoldsend'].insert(0,request.session['casinoCurrentGold'])
    if  request.session['activeCurrentGold']!=None:
        request.session['activeCurrentGoldsend'].insert(0, request.session['activeCurrentGold'])
    
    return redirect('/postGold')

def return_gold(request):
    return render(request,'index.html')




