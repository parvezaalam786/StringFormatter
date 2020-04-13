from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse("Hello Parvez")

def text(request):
    with open("E:\CWH Django\\textutils\\textutils\\tester.txt","r") as r:
        cont = r.readlines()
        return HttpResponse(cont)
def analyze(request):
    text1 = request.POST.get('text','default text is when we reload the removepunctuation without text')
    removepunc = request.POST.get('removepunctuations','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_`~|'''
    analyzed = ""
    purposes = []
    cnt = 0
    text2 = text1
    if(removepunc=="on"):
        cnt += 1
        for char in text1:
            if char not in punctuations:
                analyzed = analyzed+char
        text1 = analyzed
        purposes.append("Removed Punctuations")

    
    if(fullcaps == "on"):
        cnt += 1
        analyzed = ""
        for char in text1:
            analyzed = analyzed + char.upper()
        text1 = analyzed
        purposes.append("Upper case converted")
        
        
    if(newlineremover == "on"):
        cnt += 1
        analyzed = ""
        for char in text1:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        text1 = analyzed
        purposes.append("New lines removed")


    if(extraspaceremover == "on"):
        analyzed = ""
        for i in range(len(text1)):
            if text1[i] == ' ':
                if i+1<len(text1) and text1[i+1] == ' ':
                    continue
                analyzed = analyzed + text1[i]
            else:
                analyzed = analyzed + text1[i]          
        text1 = analyzed
        purposes.append("Extra spaces removed")

    charcounter = 0
    charcount = {}
    if(charactercounter == "on"):
        charcounter = 1
        cnt +=1 
        for i in text2:
            if(i in charcount.keys()):
                charcount[i] += 1
            else:
                charcount[i] = 1
        purposes.append("Characters counted")
   

    if cnt == 0:
        text1 = "No text entered"
        params = {'purpose':purposes,'analyzed_text':text1}
        return render(request,'analyze.html',params)
    if charcounter == 1:
        s2 = " Counting = "
        for i in sorted(charcount.keys()):
            s2 = s2 + " " + i +":"+str(charcount[i])    
        text1 = text1+s2
    params = {'purpose':purposes,'analyzed_text':text1}
    return render(request,'analyze.html',params)


def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')
