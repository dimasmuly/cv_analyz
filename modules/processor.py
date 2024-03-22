from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModel
import torch
import nltk
from nltk.corpus import stopwords

access_token = "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"

# Pemrosesan Data
tokenizer = AutoTokenizer.from_pretrained("guriko/autotrain-cv_resume-56492130967", token=access_token)
model_sequence = AutoModelForSequenceClassification.from_pretrained("guriko/autotrain-cv_resume-56492130967", token=access_token)
model = AutoModel.from_pretrained("guriko/autotrain-cv_resume-56492130967", token=access_token)

nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))

def process_text(text):
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model_sequence(**inputs)
    return torch.nn.functional.softmax(outputs.logits, dim=-1)


