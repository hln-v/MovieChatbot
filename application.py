from flask import Flask, render_template, request
from recommender.recommend import get_recommendations

application = Flask(__name__)

@application.route("/", methods=["GET", "POST"])
def index():
    chat_history = []

    if request.method == "POST":
        user_message = request.form.get("message", "").strip()

        if user_message:
            # 1) Add user message
            chat_history.append({
                "role": "user",
                "text": user_message
            })

            # 2) Get recommendations based on this message
            recommendations = get_recommendations(user_message)

            # 3) Add bot messages (one per movie)
            for rec in recommendations:
                title = rec.get("title", "Unknown title")
                year = rec.get("year", "")
                synopsis = rec.get("synopsis", "")

                bot_text = f"{title}"
                if year:
                    bot_text += f" ({year})"
                if synopsis:
                    bot_text += f"\n{synopsis}"

                chat_history.append({
                    "role": "bot",
                    "text": bot_text
                })

    return render_template("index.html", chat_history=chat_history)


if __name__ == "__main__":
    application.run(debug=True)
