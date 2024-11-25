from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Sorular ve cevaplar
questions = [
    {
        'question': "Python, yapay zeka modelleri geliştirmek için neden tercih edilir?",
        'options': ['Hızlı çalıştığı için', 'Büyük bir topluluğa sahip olduğu için', 'Oyun yapımı için tasarlandığı için', 'Grafik tasarımı için kullanıldığı için'],
        'answer': 'Büyük bir topluluğa sahip olduğu için'
    },
    {
        'question': "Yapay zeka projelerinde hangi Python kütüphanesi en yaygın kullanılır?",
        'options': ['Pandas', 'Matplotlib', 'TensorFlow', 'BeautifulSoup'],
        'answer': 'TensorFlow'
    },
    {
        'question': "AI modeli eğitmeden önce veri ön işleme neden önemlidir?",
        'options': ['Eğitim verilerini optimize etmek için', 'Hızlı çalışmasını sağlamak için', 'Yapay zeka kodunu azaltmak için', 'Veri boyutunu küçültmek için'],
        'answer': 'Eğitim verilerini optimize etmek için'
    },
    {
        'question': "Python'da bir sinir ağı modeli geliştirmek için hangi kütüphane kullanılır?",
        'options': ['Django', 'Keras', 'Flask', 'Requests'],
        'answer': 'Keras'
    },
    {
        'question': "Overfitting, bir AI modelinde hangi soruna yol açar?",
        'options': ['Veri kaybı', 'Genel performansın düşmesi', 'Bellek sızıntısı', 'Yavaş işlem hızı'],
        'answer': 'Genel performansın düşmesi'
    },
    {
        'question': "Bir yapay zeka modelini bir web uygulamasında kullanmak için hangi framework kullanılabilir?",
        'options': ['Flask', 'Pandas', 'NumPy', 'Matplotlib'],
        'answer': 'Flask'
    },
    {
        'question': "Python'da bir modeli kaydetmek için hangi format sıklıkla kullanılır?",
        'options': ['.json', '.h5', '.txt', '.csv'],
        'answer': '.h5'
    },
    {
        'question': "Python'da yapay zeka modelinin düşük doğruluk sorununu nasıl çözebilirsiniz?",
        'options': ['Daha fazla veri kullanarak', 'Grafikler oluşturarak', 'Kütüphane güncelleyerek', 'Yeni bir model indirmek'],
        'answer': 'Daha fazla veri kullanarak'
    }
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Kullanıcının ismini al ve oturuma kaydet
        session['username'] = request.form['username']
        session['high_score'] = session.get('high_score', 0)
        return redirect(url_for('quiz'))
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    username = session.get('username', 'Misafir')
    high_score = session.get('high_score', 0)
    return render_template('quiz.html', questions=questions, username=username, high_score=high_score, enumerate=enumerate)

@app.route('/submit', methods=['POST'])
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        selected_option = request.form.get(f'question-{i}')
        if selected_option == question['answer']:
            score += 1


    if score > session.get('high_score', 0):
        session['high_score'] = score

    username = session.get('username', 'Misafir')
    high_score = session['high_score']
    return render_template('submit.html', score=score, total=len(questions), username=username, high_score=high_score)


if __name__ == '__main__':
    app.run(debug=True)