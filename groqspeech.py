import os
from dotenv import load_dotenv 
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

speech_file_path = "speech.wav" 
model = "playai-tts"
voice = "Chip-PlayAI"
text = "በጉጉት ሲጠበቅ የነበረው የመጀመሪያ ዙር የFree style ውድድር የመጀመሪያ ትንቅንቅ ወደ ቀጣይ ዙር አላፊው ታውቋልበዚህም YNK Black ፉክክሩን በዝረራ ማሸነፍ ችሏል! በ ተመልካች ድምፅም እንዲሁም በዳኛ ( Yak ) ድምፅ YNK Black የበላይ ሆኖ በመገኘቱ ወደቀጣይ ዙር ተቀላቅሏል!!"
response_format = "wav"
response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text,
    response_format=response_format
)

response.write_to_file(speech_file_path)
print("ee")