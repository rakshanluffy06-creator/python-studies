from flask import Flask, request, render_template

app = Flask(__name__)

class Election:

    def calculate(self, v1, v2, v3):

        total_votes = v1 + v2 + v3

        votes = {
            "Candidate 1": v1,
            "Candidate 2": v2,
            "Candidate 3": v3
        }

        winner = max(votes, key=votes.get)
        winning_votes = votes[winner]

        return total_votes, winner, winning_votes

election = Election()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result")
def show_result():

    constituency = request.args.get("constituency")

    c1 = request.args.get("c1")
    c2 = request.args.get("c2")
    c3 = request.args.get("c3")

    v1 = int(request.args.get("v1"))
    v2 = int(request.args.get("v2"))
    v3 = int(request.args.get("v3"))

    total_votes, winner, winning_votes = election.calculate(v1, v2, v3)

    if winner == "Candidate 1":
        winner_name = c1
    elif winner == "Candidate 2":
        winner_name = c2
    else:
        winner_name = c3

    return render_template(
        "result.html",
        constituency=constituency,
        c1=c1,
        c2=c2,
        c3=c3,
        v1=v1,
        v2=v2,
        v3=v3,
        total_votes=total_votes,
        winner=winner_name,
        winning_votes=winning_votes
    )

if __name__ == "__main__":
    app.run(debug=True)
