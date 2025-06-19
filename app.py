from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sales_result = None
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        transaction = int(request.form['transaction'])

        # Giả lập tính toán sales (vd: transaction // 800)
        sales_result = transaction // 800

    return render_template('index.html', sales=sales_result)

if __name__ == '__main__':
    app.run(debug=True)
