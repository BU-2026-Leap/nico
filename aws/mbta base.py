def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    event: dict with "rawPath" (URL path) and optional "queryStringParameters"
    """
    path = event.get("rawPath", "/")
    query = event.get("queryStringParameters") or {}

    if path == "/":
        return html_response("""
            <h1>🚆 Train Conductor Simulator</h1>
            <p>Welcome, Conductor.</p>
            <a href="/intro">Start Shift</a>
        """)

    elif path == "/intro":
        return html_response("""
            <h2>Shift Briefing</h2>
            <p>You are starting a 12-hour shift.</p>
            <a href="/cockpit">Enter Cockpit</a>
        """)

    elif path == "/cockpit":
        return html_response("""
            <h2>Cockpit</h2>
            <p>Did you bring your lunch?</p>
            <a href="/lunch?choice=yes">Yes</a><br>
            <a href="/lunch?choice=no">No</a>
        """)

    elif path == "/lunch":
        choice = query.get("choice", "no")
        message = (
            "Good thinking. You'll need energy."
            if choice == "yes"
            else "12 hours without food is risky."
        )
        return html_response(f"""
            <h2>Lunch Check</h2>
            <p>{message}</p>
            <a href="/start_train">Start Train</a>
        """)

    elif path == "/start_train":
        return html_response("""
            <h2>Train Started</h2>
            <p>Choose your stop:</p>
            <ul>
                <li><a href="/stop/B">B Line</a></li>
                <li><a href="/stop/BC">BC Stop</a></li>
                <li><a href="/stop/Kenmore">Kenmore</a></li>
            </ul>
        """)

    elif path.startswith("/stop/"):
        stop = path.split("/")[-1]
        return html_response(f"""
            <h2>Arrival</h2>
            <p>You arrive at <strong>{stop}</strong>.</p>
            <p>Shift complete. Well done.</p>
            <a href="/">Play Again</a>
        """)

    # default 404
    return html_response("<h2>404 - Not Found</h2>", 404)


def html_response(body, status=200):
    """
    Wraps HTML body with headers and status for Lambda
    """
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"""
        <html>
            <body>
                {body}
            </body>
        </html>
        """
    }

# -----------------------
# Local testing in PyCharm
# -----------------------
if __name__ == "__main__":
    # simulate a few test paths
    test_paths = ["/", "/intro", "/cockpit", "/lunch?choice=yes", "/start_train", "/stop/B"]

    for path in test_paths:
        # split query string if exists
        if "?" in path:
            p, qs = path.split("?", 1)
            query = dict(q.split("=") for q in qs.split("&"))
        else:
            p = path
            query = {}

        event = {
            "rawPath": p,
            "queryStringParameters": query
        }

        response = lambda_handler(event, None)
        print(f"=== Path: {path} ===")
        print(response["body"])
        print("\n\n")
