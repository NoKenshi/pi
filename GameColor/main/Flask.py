from flask import Flask, redirect, jsonify
from main import *

app = Flask(__name__, static_folder='static')

bestScore = 0
play = 0
score = 1

@app.route('/')
def index():
    global score
    global bestScore
    score = 1
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;900&display=swap');
        *{{
            margin : 0;
            padding : 0;
            box-sizing: border-box;
            font-family: 'poppins', sans-serif;
        }}
        body{{
            overflow: hidden;
            background-color: black;
            color: white;
        }}
        nav{{
            display: flex;
            width: 100%;
            justify-content: space-around;
            /* background-color: #1A181B; */
            height: 80px;
            line-height: 80px; /* Pour mettre la ligne au millieu des 80 pixels d'hauteur */
        }}
        .title{{
            display: flex;
            font-size: 30px;
            font-weight: 800; /* Taille du bold */
            letter-spacing: 4px;
            text-transform: uppercase;
            cursor: pointer;
        }}
        .title:hover{{
            scale: 1.05;
        }}
        #first{{
            color: orange;
        }}
        #first:hover{{
            scale: 1.05;
            color: #eb772a;
        }}
        .wrapper{{
            display: flex;
            width: 100%;
            height: 100%;
            justify-content: center;
            align-items: center;
            text-align: center;
            overflow: hidden;
        }}
        .game{{
            margin-top: 10%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            border-radius: 8px;
            border-style: none;
            padding: 75px 50px 75px 50px;
            background-color: #241f1c;
            color: orange;
        }}
        .game:hover{{
            color: #eb772a;
        }}
        .play{{
            background-color: orange;
            border-radius: 8px;
            border-style: none;
            box-sizing: border-box;
            color: white;
            cursor: pointer;
            font-size: 16px;
            font-weight: 500;
            height: 30px;
            padding: 0 1.6rem;
            margin-top: 20px;
            padding-bot: 10px;
            text-align: center;
            text-shadow: rgba(0, 0, 0, 0.25) 0 3px 8px;
            transition: all .5s;
            text-transform: capitalize;
        }}
        .play:hover{{
            box-shadow: orange 0 1px 30px;
            transition-duration: .1s;
            scale: 1.1;
        }}
        a{{
            text-decoration: none;
        }}
    </style>
    <script>
        function get_score() {{
            fetch('/score')
            .then(response => response.json())
            .then(data => {{
                document.getElementById("score").textContent = data.score;
            }})
            .catch(error => {{
                console.error(error);
            }});
        }}
        function set_interval() {{
            setInterval(get_score, 1000);
        }}
    </script>
    <title>Projet 1T</title>
</head>
<body onload="set_interval();">
    <nav>
        <div class="title">
            <span id="first">c</span>olor <span id="first">g</span>ame
        </div>
    </nav>
    <div class="wrapper">
        <div class="game">
            <p>Niveau : <b><span id="score">{score}</span></b> </p><br>
            <p>Best score : <b>{bestScore}</b> </p><br>
            <a href="/game" class="play" role="button">play game</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/game')
def game():
    global bestScore
    global score
    global play
    tab = [1, True]
    if play == 0:
        play = 1
        while tab[1]:
            tab = main(tab[0])
            score = tab[0]
    if score > bestScore:
        bestScore = score
    play = 0
    return redirect('/')

@app.route('/score')
def get_score():
    global score
    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
