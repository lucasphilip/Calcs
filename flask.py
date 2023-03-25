from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        scr = float(request.form['scr'])
        target = float(request.form['target'])
        
        dose = round((target * (0.06 * weight)) / (scr + 0.7), 2)
        
        return render_template('result.html', dose=dose)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)


