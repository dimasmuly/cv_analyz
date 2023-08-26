from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import nltk
from nltk.corpus import stopwords

# Pemrosesan Data
tokenizer = AutoTokenizer.from_pretrained("guriko/autotrain-cv_resume-56492130967", use_auth_token=True)
model = AutoModelForSequenceClassification.from_pretrained("guriko/autotrain-cv_resume-56492130967", use_auth_token=True)
nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))

def process_text(text):
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    return torch.nn.functional.softmax(outputs.logits, dim=-1)
