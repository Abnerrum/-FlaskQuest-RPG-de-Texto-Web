from flask import Flask, render_template, request, redirect, session
import sqlite3
import random

app = Flask(__name__)
app.secret_key = 'uma_chave_muito_secreta'

# --- BANCO DE DADOS ---
def init_db():
    conn = sqlite3.connect('game.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS players 
                 (id INTEGER PRIMARY KEY, nome TEXT, hp INTEGER, ouro INTEGER, level INTEGER)''')
    conn.close()

def get_db():
    conn = sqlite3.connect('game.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- ROTAS ---
@app.route('/')
def index():
    player = None
    if 'player_id' in session:
        conn = get_db()
        player = conn.execute('SELECT * FROM players WHERE id = ?', (session['player_id'],)).fetchone()
        conn.close()
    return render_template('index.html', player=player)

@app.route('/novo_jogo', methods=['POST'])
def novo_jogo():
    nome = request.form.get('nome')
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO players (nome, hp, ouro, level) VALUES (?, 100, 0, 1)', (nome,))
    session['player_id'] = cur.lastrowid
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/explorar')
def explorar():
    if 'player_id' not in session: return redirect('/')
    
    # Sorteio: 70% chance de monstro, 30% chance de ouro
    evento = random.random()
    conn = get_db()
    
    if evento < 0.7:
        mensagem = "Um Goblin apareceu! Você lutou e perdeu 10 de HP, mas achou 5 moedas."
        conn.execute('UPDATE players SET hp = hp - 10, ouro = ouro + 5 WHERE id = ?', (session['player_id'],))
    else:
        mensagem = "Você encontrou um baú vazio... mas ganhou 20 de ouro no fundo!"
        conn.execute('UPDATE players SET ouro = ouro + 20 WHERE id = ?', (session['player_id'],))
    
    conn.commit()
    conn.close()
    session['log'] = mensagem
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)