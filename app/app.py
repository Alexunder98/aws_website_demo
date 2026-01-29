from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string(f"""
        <html>
        <head>
            <title>Hello, Internet!</title>
            <style>
                body {{
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #111;
                    color: white;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }}
                h1 {{
                    margin-bottom: 20px;
                }}
                a.button {{
                    display: inline-block;
                    padding: 15px 30px;
                    background: crimson;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    border-radius: 8px;
                    transition: background 0.3s;
                }}
                a.button:hover {{
                    background: darkred;
                }}
            </style>
        </head>
        <body>
            <h1>Hello, Internet!</h1>
            <a class="button" href="{url_for('video')}">Don't click here</a>
        </body>
        </html>
    """)

@app.route("/video")
def video():
    video_id = "wSj1q-DUSqg"  # YouTube Shorts ID
    embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&mute=0&playsinline=1"

    return render_template_string(f"""
        <html>
        <head>
            <title>Video Page</title>
            <style>
                body {{
                    margin: 0;
                    height: 100vh;
                    background: black;
                }}
                iframe {{
                    width: 100%;
                    height: 100%;
                    border: none;
                }}
            </style>
        </head>
        <body>
            <iframe 
                src="{embed_url}" 
                allow="autoplay; fullscreen">
            </iframe>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
