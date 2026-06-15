from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def election_result():
    results = [
        {"candidate": "Rakshan", "votes": 5200},
        {"candidate": "Mark", "votes": 4300},
        {"candidate": "urvil", "votes": 2100}
    ]

    winner = max(results, key=lambda x: x["votes"])

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Election Results</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                text-align: center;
            }
            table {
                margin: auto;
                border-collapse: collapse;
                width: 50%;
            }
            th, td {
                border: 1px solid black;
                padding: 10px;
            }
            th {
                background-color: #f2f2f2;
            }
            h2 {
                color: green;
            }
        </style>
    </head>
    <body>

        <h1>Election Results</h1>

        <table>
            <tr>
                <th>Candidate</th>
                <th>Votes</th>
            </tr>

            {% for candidate in results %}
            <tr>
                <td>{{ candidate.candidate }}</td>
                <td>{{ candidate.votes }}</td>
            </tr>
            {% endfor %}
        </table>

        <h2>
            Winner: {{ winner.candidate }} ({{ winner.votes }} votes)
        </h2>

    </body>
    </html>
    """

    return render_template_string(
        html,
        results=results,
        winner=winner
    )

if __name__ == "__main__":
    app.run(debug=True)
