from django.http import JsonResponse
from django.shortcuts import render

from test import calcii

# def train_chatbot_api(request):
#     # Call your training function here
#     train()
#     return JsonResponse({'message': 'Chatbot training completed successfully'})

def test_calcii_api(request, query):
    # Call your testing function here
    response = calcii(query)
    return JsonResponse({'response': response})


# def input_form(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('all_members.html')
#     context = {
#     'mymembers': mymembers,
#   }
#     return HttpResponse(template.render(context, request))
#     return render(request, 'input_form.html')