from django.shortcuts import render
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Load the model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def index(request):
    return render(request, 'detector/index.html')

def predict(request):
    if request.method == 'POST':
        news_text = request.POST['news']
        vectorized_text = vectorizer.transform([news_text])
        prediction = model.predict(vectorized_text)[0]
        prob = model.predict_proba(vectorized_text)[0]

        # Plot probability distribution
        labels = ['Fake', 'Real']
        plt.figure(figsize=(5, 5))
        plt.pie(prob, labels=labels, autopct='%1.1f%%', colors=['#FF6B6B', '#6BCB77'])
        plt.title('News Authenticity Probability')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graph = base64.b64encode(image_png).decode('utf-8')

        result = 'Real' if prediction == 1 else 'Fake'

        return render(request, 'detector/index.html', {
            'result': result,
            'graph': graph
        })
    return render(request, 'detector/index.html')