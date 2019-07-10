from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = {}
    for word in wordlist:
        try:
            word_dict[word]+=1
        except:
            word_dict[word]=1
    sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 
                                          'sorted_word_dict': sorted_word_dict})

def about(request):
    return render(request, 'about.html')
