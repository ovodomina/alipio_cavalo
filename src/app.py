from flask import Flask, request, render_template_string
import threading
import webbrowser

app = Flask(__name__)


def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return round(peso / (altura ** 2), 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"


HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Calculadora de IMC</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            width: 380px;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #1f2937;
        }

        label {
            display: block;
            margin-top: 15px;
            margin-bottom: 5px;
            font-weight: bold;
            color: #374151;
        }

        input {
            width: 100%;
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 10px;
            box-sizing: border-box;
            font-size: 16px;
        }

        button {
            width: 100%;
            margin-top: 25px;
            padding: 14px;
            border: none;
            border-radius: 10px;
            background: #4f46e5;
            color: white;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background: #4338ca;
        }

        .resultado {
            margin-top: 25px;
            padding: 20px;
            border-radius: 12px;
            background: #eef2ff;
            text-align: center;
        }

        .imc {
            font-size: 32px;
            font-weight: bold;
            color: #4f46e5;
        }

        .classificacao {
            margin-top: 10px;
            font-size: 18px;
            color: #111827;
            font-weight: bold;
        }

        .erro {
            margin-top: 20px;
            padding: 15px;
            background: #fee2e2;
            color: #b91c1c;
            border-radius: 10px;
            text-align: center;
        }

        .rodape {
            margin-top: 20px;
            font-size: 12px;
            color: #6b7280;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Calculadora de IMC</h1>

        <form method="post">
            <label>Peso (kg)</label>
            <input type="number" step="0.01" name="peso" required>

            <label>Altura (m)</label>
            <input type="number" step="0.01" name="altura" required>

            <button type="submit">Calcular IMC</button>
        </form>

        {% if erro %}
            <div class="erro">{{ erro }}</div>
        {% endif %}

        {% if imc %}
            <div class="resultado">
                <div>Seu IMC é</div>
                <div class="imc">{{ imc }}</div>
                <div class="classificacao">{{ classificacao }}</div>
            </div>
        {% endif %}

        <div class="rodape">
            IMC = peso ÷ altura²
        </div>
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    classificacao = None
    erro = None

    if request.method == "POST":
        try:
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])

            if peso <= 0 or altura <= 0:
                raise ValueError

            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)

        except ValueError:
            erro = "Informe valores válidos para peso e altura."

    return render_template_string(
        HTML,
        imc=imc,
        classificacao=classificacao,
        erro=erro
    )


def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.5, abrir_navegador).start()
    app.run(host="127.0.0.1", port=5000, debug=False)