from fastapi import FastAPI, UploadFile, File
import pickle
import PyPDF2

app = FastAPI()

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def extract_text(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

@app.get("/")
def home():
    return {"message": "API Running Online 🚀"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    text = extract_text(file.file)
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]

    return {
        "category": prediction,
        "status": "Processed Online"
    }