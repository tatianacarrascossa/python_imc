from http import HTTPStatus
from flask import Flask, jsonify, request
from coffee_shop.models import Pessoa
from coffee_shop.helpers import calculaIMC,verificaNivel
import sqlite3

SQL_LISTA_PESSOA = 'SELECT * FROM pessoa'
SQL_INSERE_PESSOA = 'INSERT INTO pessoa VALUES (?, ?, ?, ?, ?)'
SQL_CRIA_TABELA = 'CREATE TABLE IF NOT EXISTS pessoa(nome TEXT, idade TEXT, sexo TEXT, numero TEXT, peso TEXT)'
DATABASE = 'database.db'

app = Flask(__name__)

with sqlite3.connect(DATABASE) as conn:
    cursor = conn.cursor()
    cursor.execute(SQL_CRIA_TABELA)
    cursor.close()
conn.close()


@app.route('/listar', methods=['GET'])
def listar():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(SQL_LISTA_PESSOA)
        pessoas = list(map(lambda pessoa: Pessoa(pessoa).converteDicionario(), cursor.fetchall()))

        for i in range(0, len(pessoas)):
            pessoas[i]['imc'] = calculaIMC(pessoas[i]['peso'],pessoas[i]['numero'])
            pessoas[i]['nivel'] = verificaNivel(pessoas[i]['imc'])

        listaOrdenada = sorted(pessoas, key=lambda objeto: objeto['imc'], reverse=False)
        cursor.close()
    conn.close()

    return jsonify(listaOrdenada), HTTPStatus.CREATED

@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    nome = request.json.get("nome")
    idade = request.json.get("idade")
    sexo = request.json.get("sexo")
    numero = request.json.get("numero")
    peso = request.json.get("peso")

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(SQL_INSERE_PESSOA, (nome, idade, sexo, numero, peso))
        cursor.execute(SQL_LISTA_PESSOA)
        pessoas = list(map(lambda pessoa: Pessoa(pessoa).converteDicionario(), cursor.fetchall()))
        cursor.close()
    conn.close()

    return jsonify(pessoas), HTTPStatus.CREATED


