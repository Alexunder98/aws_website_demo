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
                .buttons {{
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                    align-items: center;
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

                .socials {{
                    display: flex;
                    gap: 12px;
                    margin-top: 6px;
                }}

                a.social {{
                    display: inline-block;
                    padding: 10px 16px;
                    background: rgba(255,255,255,0.06);
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: 600;
                    transition: background 0.2s, transform 0.08s;
                    border: 1px solid rgba(255,255,255,0.04);
                }}
                a.social:hover {{
                    background: rgba(255,255,255,0.09);
                    transform: translateY(-2px);
                }}
                /* platform colors */
                a.social.linkedin {{ background: #0077b5; }}
                a.social.github {{ background: #24292e; }}
            </style>
        </head>
        <body>
            <h1>Hello, Internet!</h1>
            <div class="buttons">
                <a class="button" href="{url_for('video')}">Don't click here</a>

                <div class="socials">
                    <a class="social linkedin" href="https://www.linkedin.com/in/alexandru-troaca/" target="_blank" rel="noopener noreferrer" aria-label="Alexandru on LinkedIn">LinkedIn</a>
                    <a class="social github" href="https://github.com/Alexunder98" target="_blank" rel="noopener noreferrer" aria-label="Alexunder98 on GitHub">GitHub</a>
                </div>
            </div>
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
