from flask import Flask, render_template_string

app = Flask(__name__)

# HTML, CSS, and JavaScript code

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
        }

        h1 {
            text-align: center;
        }

        #gameBoard {
            width: 604px;
            height: 604px;
            border: 2px solid #333;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }

        .box {
            width: 175px;
            height: 175px;
            margin: 2px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Count: <span id="countDisplay">0</span></h1>
    <div id="gameBoard"></div>

    <script>
        const colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'lime'];
        const boxes = Array.from({ length: 9 }, (_, i) => ({
            id: i,
            color: colors[Math.floor(Math.random() * colors.length)],
        }));

        let count = 0;

        const countDisplay = document.getElementById('countDisplay');
        const gameBoard = document.getElementById('gameBoard');

        boxes.forEach(({ id, color }) => {
            const box = document.createElement('div');
            box.className = 'box';
            box.id = `box-${id}`;
            box.style.backgroundColor = color;

            box.addEventListener('click', () => {
                const newColor = colors[Math.floor(Math.random() * colors.length)];
                box.style.backgroundColor = newColor;

                count++;
                countDisplay.textContent = count;

                const allBoxes = document.querySelectorAll('.box');
                const firstColor = allBoxes[0].style.backgroundColor;
                const isAllSameColor = Array.from(allBoxes).every(
                    box => box.style.backgroundColor === firstColor
                );

                if (isAllSameColor) {
                    alert(`You won the game in ${count} clicks!`);
                }
            });

            gameBoard.appendChild(box);
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(debug=True)


