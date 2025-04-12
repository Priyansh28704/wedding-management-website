from django.shortcuts import render
from django.http import JsonResponse

def chatbot_view(request):
    return render(request, 'chatbot/chatbot.html')

def chatbot_response(request):
    user_input = request.GET.get('message', '').lower()

    # Smart keyword-based response logic
    responses = {
        "wedding services": "We offer a range of wedding services!you can check them out! on our website",
        "wedding catering": "We have excellent catering services!you can check them out! on our website",
        "wedding planning": "We have amazing wedding planning services! you can check them out! on our website",
        "wedding photography": "We have professional photographers! Would you like to see their portfolios?",
        "wedding venue": "We have beautiful wedding venues! Do you prefer indoor or outdoor?",
        "wedding decoration": "We provide stunning wedding decorations. you can check them out! on our website",
        "wedding planner": "We have the best wedding planners! Would you like to know more?",
        "wedding packages": "We offer various wedding packages. Would you like to know more?",
        "help": "Sure! What do you need help with?",
        "services": "We offer a variety of services.Would you like to know more?",
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What can I do for you?",
        "wedding": "We have a variety of wedding packages!Would you like to know more?",
        "dj": "Our DJs are the best in town! Do you want to see their profiles?",
        "venue": "We have beautiful venues! Do you prefer indoor or outdoor?",
        "photographer": "Our photographers capture the best memories! Want to view some portfolios?",
        "planner": "Our expert planners will take care of everything. Would you like to contact one?",
        "catering": "We offer delicious catering packages. Veg or non-veg?",
        "mehendi": "We have professional Mehendi artists. Want to see designs?",
        "makeup": "Bridal makeup packages are available. Do you want details?",
        "outdoor": "We have stunning outdoor venues. you can check them out! on our website",
        "indoor": "We have beautiful indoor venues. you can check them out! on our website",
        "veg": "We have a variety of vegetarian options.you can check them out! on our website",
        "non-veg" : "We have a variety of non-vegetarian options. you can check them out! on our website",
        "yes": "you can check them out! on our website",
        "no": "Okay! If you have any questions, feel free to ask.",
    }

    response = "Sorry, I didn't get that. Can you rephrase your question?"

    for keyword, reply in responses.items():
        if keyword in user_input:
            response = reply
            break

    return JsonResponse({'response': response})
