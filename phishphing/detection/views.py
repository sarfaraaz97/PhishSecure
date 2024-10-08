import numpy as np
import joblib
from django.shortcuts import render
from .feature import FeatureExtraction

gbc = joblib.load(filename="detection/model_new.pkl")

def predict(request):
    if request.method == "POST":
        url = request.POST.get("url")
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1, 30)
        print(x.shape)
        y_pred = gbc.predict(x)[0]
        y_pro_phishing = gbc.predict_proba(x)[0, 0]
        y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

        response_data = {
            'url': url,
            'prediction': y_pred,
            'probability_phishing': y_pro_phishing,
            'probability_non_phishing': y_pro_non_phishing
        }
        
        print(response_data)
        
        return render(request, "result.html", {"response": response_data})
    return render(request, "index.html")
def about(request):
    return render(request,'about.html')
def usecase(request):
    return render(request,'usecase.html')

