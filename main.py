from flask import Flask, render_template, request
from mail import Mail
from post import Post

app = Flask(__name__)
posts = Post()


@app.route("/")
def home():
    return render_template("index.html", posts=posts.all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        mail = Mail()
        mail.send_mail(data["name"],
                       data["email"],
                       data["phone"],
                       data["message"])
        return render_template("contact.html", sent=True)
    return render_template("contact.html", sent=False)


@app.route("/post/<int:index>")
def blog(index):
    return render_template("post.html",
                           title=posts.all_posts[index]["title"],
                           subtitle=posts.all_posts[index]["subtitle"],
                           author=posts.all_posts[index]["author"],
                           date=posts.all_posts[index]["date"],
                           body=posts.all_posts[index]["body"])


if __name__ == "__main__":
    app.run()
