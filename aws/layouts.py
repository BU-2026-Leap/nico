# aws/layouts.py

def html_response(body, status=200):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width,initial-scale=1" />

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
                  integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB"
                  crossorigin="anonymous">

            <style>
                /* --- background + typography --- */
                body {{
                    min-height: 100vh;
                    margin: 0;
                    color: #f1f5f9;
                    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
                    background:
                      radial-gradient(900px 600px at 20% 10%, rgba(99,102,241,.35), transparent 55%),
                      radial-gradient(900px 600px at 100% 0%, rgba(34,211,238,.25), transparent 55%),
                      linear-gradient(180deg, #070A14, #0B1022);
                }}

                /* --- adventure "frame" --- */
                .game-shell {{
                    max-width: 980px;
                    margin: 0 auto;
                    padding: 28px 16px 60px;
                }}

                .game-header {{
                    position: sticky;
                    top: 0;
                    z-index: 10;
                    backdrop-filter: blur(10px);
                    background: rgba(7,10,20,0.55);
                    border-bottom: 1px solid rgba(255,255,255,0.08);
                }}

                .brand {{
                    font-weight: 700;
                    letter-spacing: .4px;
                }}

                .brand-dot {{
                    display: inline-block;
                    width: 10px;
                    height: 10px;
                    border-radius: 999px;
                    margin-right: 8px;
                    background: linear-gradient(135deg, #7c5cff, #22d3ee);
                    box-shadow: 0 0 18px rgba(124,92,255,.45);
                }}

                .card-adventure {{
                    border-radius: 18px;
                    border: 1px solid rgba(255,255,255,0.12);
                    background: rgba(255,255,255,0.06);
                    box-shadow: 0 18px 50px rgba(0,0,0,0.55);
                    overflow: hidden;
                }}

                /* Make images look like "scene cards" */
                img {{
                    max-width: 100%;
                    height: auto;
                    border-radius: 14px;
                    border: 1px solid rgba(255,255,255,0.12);
                }}

                /* --- Make links look like choice buttons (without changing your HTML) --- */
                a {{
                    display: inline-block;
                    padding: 10px 14px;
                    margin: 8px 10px 0 0;
                    border-radius: 12px;
                    text-decoration: none;
                    color: #f8fafc;
                    border: 1px solid rgba(255,255,255,0.16);
                    background: rgba(255,255,255,0.06);
                    transition: transform .12s ease, background .12s ease, border-color .12s ease;
                }}
                a:hover {{
                    transform: translateY(-2px);
                    background: rgba(255,255,255,0.10);
                    border-color: rgba(124,92,255,0.55);
                }}

                /* Lists for stop selection */
                ul {{
                    margin: 10px 0 0 0;
                    padding-left: 18px;
                }}
                li {{
                    margin: 8px 0;
                }}

                h1, h2 {{
                    margin-bottom: 10px;
                    letter-spacing: .2px;
                }}

                p {{
                    color: rgba(241,245,249,0.88);
                    line-height: 1.6;
                    font-size: 1.05rem;
                    margin-bottom: 8px;
                }}

                .hint {{
                    color: rgba(241,245,249,0.65);
                    font-size: 0.9rem;
                    margin-top: 10px;
                }}
            </style>
        </head>

        <body>
            <div class="game-header py-3">
                <div class="container d-flex justify-content-between align-items-center">
                    <div class="brand"><span class="brand-dot"></span>MBTA: Choose Your Shift</div>
                    <div class="small text-white-50">Prototype</div>
                </div>
            </div>

            <main class="game-shell">
                <div class="card-adventure">
                    <div class="p-4 p-md-5">
                        {body}
                        <div class="hint">Tip: click a choice to continue the story.</div>
                    </div>
                </div>
            </main>
        </body>
        </html>
        """
    }
