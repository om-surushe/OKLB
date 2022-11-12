import aspose.words as aw
import spacy
import csv
import random

doc = aw.Document("./r2.docx")

resume = doc.to_string(aw.SaveFormat.TEXT)
resume = resume.replace("Evaluation Only. Created with Aspose.Words. Copyright 2003-2022 Aspose Pty Ltd.",'')
resume = resume.replace("Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/",'')
resume = resume.strip()

# nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("en_core_web_md")

total = [] # for random questions from set

with open("../Data/HR/type1.csv", 'r') as file:
    csvreader = list(csv.reader(file))
    total.append(csvreader[random.randint(0,len(csvreader)-1)])
with open("../Data/HR/type2.csv", 'r') as file:
    csvreader = list(csv.reader(file))
    total.append(csvreader[random.randint(0,len(csvreader)-1)])
with open("../Data/HR/type3.csv", 'r') as file:
    csvreader = list(csv.reader(file))
    total.append(csvreader[random.randint(0,len(csvreader)-1)])
with open("../Data/HR/type4.csv", 'r') as file:
    csvreader = list(csv.reader(file))
    total.append(csvreader[random.randint(0,len(csvreader)-1)])


ans_res = []
res = []

for i in range(len(total)):
    print("================================================================")
    res.append(str(input(total[i][0])))

for i in range(len(total)):
    ans_res.append([nlp(total[i][1]),nlp(res[i])])

for i in range(len(ans_res)):
    print(ans_res[i][0].similarity(ans_res[i][1]))