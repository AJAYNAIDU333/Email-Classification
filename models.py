import joblib
from utils import mask_pii

model = joblib.load("email_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def classify_email(email_body):
    masked_email, entity_list = mask_pii(email_body)
    input_vector = vectorizer.transform([masked_email])
    predicted_category = model.predict(input_vector)[0]

    return {
        "input_email_body": email_body,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_email,
        "category_of_the_email": predicted_category
    }
