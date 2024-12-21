from flask import Flask, render_template, request, redirect, url_for
import blog_data  # Simulating a data source

app = Flask(__name__)
 
@app.route("/")
def home():
    posts = blog_data.get_posts()
    return "index.html", posts

@app.route("/post")
def post(post_id):
    post = blog_data.get_post_by_id(post_id)
    if not post:
        return "Post not found!", 404
    return "/post", post

@app.route("/about.html")
def about():
    return "about.html"

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        # Get data from the form
        title = request.form.get("title")
        content = request.form.get("content")
        author = request.form.get("author", "Admin")  # Default to 'Admin' if no author is provided

        # Add the new post
        blog_data.add_post(title, content, author)

        # Redirect to the home page to display the updated post list
        return redirect(url_for("home"))

    # Render the Create Post page
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)

# def homepage():
#     return '''
# <!DOCTYPE html>
# <html>
#  <head>
#  <title>Aihaks blog</title>
#    <link rel="stylesheet" type="text/css" href="http://127.0.0.1:5000/style">
#  </head>
#  <body>
#  <div id="header">
#   <div class="post-container"></div>
#    <a id="header-title"
#     href="index.html">my blog</a>
#    <ul id="header-nav">
#      <li><a href="http://127.0.0.1:5000/about">about</a></li>
#      <li><a href="mailto:aihakviper@gmail.com">contact</a></li>
#    </ul>
#    <div class="post-content">
#     <p>because of things i learned through <strong>programming<strong><br> i have known for a long time
# that programming was not easy as it was touted to be<br>but its still fun to do because of the challenges
# it gives<br>and today i'm better for having that <strong>knowledge<strong><br>
# i'm reminded of something else <a href="https://www.richdad.com/about/robert-t-kiyosaki">robert</a> said which is<br>its not silver,gold that makes you happy ,its what you know about silver,
# gold that makes you happy.<em></p>
#    <p> a wise man once said 'simplicity is genius' to keep things simple i won't go into excessive details or complex explanations<em>
#   </p>
#      </div>
#     </div>
#    </div>
#  <div id="footer">
#   <div class="container"></div>
#   <div class="column">
#   <h4>my link</h4>
#   <p>
#     <a href="https://instagram.com/aihakviper">instagram</a>
#     <br>
#     <a href="https://facebook.com/aihakviper">facebook</a>
#   </p>
#   </div>
#   <div class="column">
#   <h4>my story</h4>
#   <p>hi there! i am aihak by name and am an inspiring developer among other things.<em></p>
#   </div>
#    </div>
#   </div>
#  </div>
#  </body>
# </html>
# '''

# @app.route('/about')
# def about():
#     return '''
# <!DOCTYPE html>
# <html>
#  <head>
#   <title>Aihaks blog<em></title>
#   <link rel="stylesheet" type="text/css" href="http://127.0.0.1:5000/style">
#  </head>
#  <body>
#  <div id= "header">
#   <div class="container"></div>
#    <a id= "header-title"
#    href="index.html">my blog</a>
#    <ul id="header-nav">
#      <li><a href="http://127.0.0.1:5000/homepage">homepage</a></li>
#      <li><a href="mailto:ahmadisah24@gmail.com">contact</a></li>
#    </ul>
#  <div id="content">
#   <div class="container">
#    <div class="about">
#     <div class="about-author"><img src="me1.jpg">
#    </div>
#    <p class="about-date">09-08-2021</p>
#    <h3 class="about-title">about me</h3>
#    <div class="about-content">
#     <p>as a programmer ask me to review 10 lines of code and i will find issues in all 10 lines but ask me to review 500 lines of code and i will say it looks good.<em></p>
#    <p> a wise man once said 'simplicity is genius' to keep things simple i won't go into excessive details or complex explanations<em>
#   </p>
    
#    </div>
#   </div>
#  <div id="footer"<>/div>
#   <div class="container"></div>
#   <div class="column">
#   <h4>my link</h4>
#   <p>
#     <a href="https://instagram.com/aihakviper">instagram</a>
#     <br>
#     <a href="https://facebook.com/ahmadisahamza">facebook</a>
#   </p>
#   </div>
#   <div class="column">
#   <h4>my story</h4>
#   <p>hi there! i am aihak by name and am an inspiring developer among other things.<em></p>
#   </div>
#  </div>
# </div>
#  </body>
# </html>
# '''

# @app.route('/style')
# def style():
#       return '''
#     @import url(https://fonts.googleapis.com/css?family=montserrat:400,700);

# body{
#   color:#555;
#   margin:0;

#   font-family: 'montserrat' ,sans-serif;
# }

# #header{background-color: #1abc9c;
#   height: 150px;
#   line-height: 150px;
# }

# #header a {
#   color: white;
#   text-decoration: none;

#   text-transform: uppercase;
#   letter-spacing: 0.1em;
# }

# #header a:hover {
#   color: #222;
# }

# #header-title {
#   display: block;
#   float: left;

#   font-size: 20px;
#   font-weight: bold;
# }

# #header-nav {
#   display: block;
#   float: right;
#   margin-top: 0;
# }

# #header-nav li {
#   display: inline;
#   padding-left: 20px;
# }

# .container{
#   max-width: 1000px;
#   margin: 0 auto;
# }

# #footer {
#   background-color: #2f2f2f;
#   padding: 50px 0;
# }

# .column {
#   min-width: 300px;
#   display: inline-block;
#   vertical-align: top;
# }

# #footer h4 {
#   color: white;
#   text-transform:uppercase;
#   letter-spacing: 0.1em;
# }

# #footer p {
#   color: white;
# }

# #footer a {
#   color: #1abc9c;
#   text-decoration: none;
# }

# #footer a:hover{
#   color: #f6a623;
# }

# .post {
#   max-width: 800px;
#   margin: 0 auto;
#   padding: 60px 0;
# }

# .post-author img{
#   width: 50px;
#   height: 50px;
#   vertical-align: middle;
# }

# .post-author span {
#   margin-left: 16px;
# }

# .post-date {
#   color:#d2d2d2;

#   font-size: 14px;
#   font-weight: bold;

#   text-transform: uppercase;
#   letter-spacing: 0.1em;
# }

# h1, h2, h3, h4 {
#   color: #333;
# }

# p {
#   line-height: 1.5;
# }

# .post, .about {
#   max-width: 800px;
#   margin: 0 auto;
#   padding: 60px 0;
# }

# .post {
#   text-align: center;
# }

# .post-author img, .about-author img , .follower img{
#   border-radius: 50%;
# }

# .post-container:nth-child(even) {
#   background-color: #f2f2f2;
# }

# .follower {
#   max-width: 800px;
#   margin: 0 auto;
#   padding: 60px 0;
# }

# .follower img{
#   width: 50px;
#   height: 50px;
#   vertical-align: middle;
# }

# .follower span {
#   margin-left: 16px;
# }

# .about-author img {
#   width: 50px;
#   height: 50px;
#   vertical-align: middle;
# }

# .about-author span{
#   margin-left: 16px;  
# }
#     '''
    
    