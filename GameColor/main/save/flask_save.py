from flask import Flask, redirect
from gpiozero import *
from main import *

app = Flask(__name__, static_folder='static')

bestScore = 0
play = 0
score = 0

@app.route('/')
def index():
    global score
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        *{{
            margin : 0;
            padding : 0;
            background-color: black;
            color: white;
        }}
        .wrapper{{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .game{{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .play{{
            background-image: linear-gradient(92.88deg, #455EB5 9.16%, #5643CC 43.89%, #673FD7 64.72%);
            border-radius: 8px;
            border-style: none;
            box-sizing: border-box;
            color: #FFFFFF;
            cursor: pointer;
            flex-shrink: 0;
            font-family: "Inter UI","SF Pro Display",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Open Sans","Helvetica Neue",sans-serif;
            font-size: 16px;
            font-weight: 500;
            height: 4rem;
            padding: 0 1.6rem;
            text-align: center;
            text-shadow: rgba(0, 0, 0, 0.25) 0 3px 8px;
            transition: all .5s;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }}
        .play:hover{{
            box-shadow: rgba(80, 63, 205, 0.5) 0 1px 30px;
            transition-duration: .1s;
        }}
    </style>
    <script>
        function set_interval(){{
            setInterval("reload_page();", 5000);
            print("Test");
        }}
        function reload_page(){{
            location.reload(true);
        }}
    </script>
    <title>Projet 1T</title>
</head>
<body onload="set_interval();>
    <div class="wrapper">
        <div class="game">
            <p>Score : {score} </p><br>
            <p>Best score : {bestScore} </p><br>
            <a href="/game" class="play" role="button">Jeu couleur</a>
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
    tab = [3, True]
    if play == 0:
        play = 1
        while tab[1]:
            tab = main(tab[0])
            score = tab[0]
            print(tab)
    if score > bestScore:
        bestScore = score
    play = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
