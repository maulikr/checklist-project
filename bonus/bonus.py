contents = ["Doc : All the contents go here.",
            "Presentation : All the contents go here.",
             "Report : All the contents go here."]

filenames = ["doc.txt", "presentation.txt", "report.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", 'w')
    file.write(content)