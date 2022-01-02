from langdetect import detect

all_language_code ={
    "ar" : "Arab",
    "en" : "English",
    "de" : "German",
    "ru" : "Russian",
    "es" : "Spanish",
    "id" : "Indonesia",
    "fr" : "France"
}

input_sentences =[
    "Arif Fadillah, Decision Support System Semester Final Exam assignment",
    "Arif Fadillah, Tarea del examen final del semestre del sistema de apoyo a la toma de decisiones",
    "Arif Fadillah, Tugas Akhir Semester Sistem Pendukung Keputusan",
    "Arif Fadillah, devoir d'examen final du semestre du système d'aide à la décision"
    
]
lemmatizer_names = ['language Code','Input Sentence']
format_text = "{:24}" * (len(lemmatizer_names)+1)
print ("\n",format_text.format("Language Name", *lemmatizer_names),'\n','*'*120)
for data in input_sentences:
    language_code = detect(data)
    sentence = [all_language_code.get(language_code), language_code, data]
    print(format_text.format(*sentence))
