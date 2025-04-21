from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    name = request.form.get('name')
    interest = request.form.get('interest')

    advice = generate_advice(interest)

    return render_template('response.html', name=name, advice=advice)

def generate_advice(interest):
    if interest == 'software':
        return "Software Development is a great field. Start with Python or JavaScript."
    elif interest == 'ai':
        return "AI is the future! Learn Python, Machine Learning, and start small projects."
    elif interest == 'design':
        return "Design is about creativity. Explore Figma, Adobe XD, and web design."
    elif interest == 'marketing':
        return "Digital Marketing includes SEO, content creation, and analytics."
    elif interest == 'cybersecurity':
        return "Cyber Security is in demand. Learn about networks, Kali Linux, and CEH."
    else:
        return "Please select a valid interest area."

if __name__ == '__main__':
    app.run(debug=True)
