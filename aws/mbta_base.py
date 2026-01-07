from aws.layouts import html_response

IMAGE_MAP = {
    "intro": "https://your-bucket.s3.amazonaws.com/intro.jpg",
    "cockpit": "https://your-bucket.s3.amazonaws.com/cockpit.jpg",
    "lunch_yes": "https://your-bucket.s3.amazonaws.com/lunch_yes.jpg",
    "lunch_no": "https://your-bucket.s3.amazonaws.com/lunch_no.jpg",
    "train_starting": "https://your-bucket.s3.amazonaws.com/train.jpg",
    "BU": "https://your-bucket.s3.amazonaws.com/stop_b.jpg",
    "BC": "https://your-bucket.s3.amazonaws.com/stop_bc.jpg",
    "Kenmore": "https://your-bucket.s3.amazonaws.com/stop_kenmore.jpg",
}

def get_page(title, content, image_key=None):
    img = f'<img src="{IMAGE_MAP.get(image_key)}">' if image_key else ''
    return f"<h2>{title}</h2>{img}<div>{content}</div>"

def lambda_handler(event, context):
    path = event.get("rawPath", "/")
    query = event.get("queryStringParameters") or {}

    if path == "/":
        return html_response(get_page(
            "MBTA Train Conductor Simulator (Green Line)",
            '<p>Welcome, Conductor!</p><a href="/intro">Start Shift</a>'
        ))

    elif path == "/intro":
        return html_response(get_page(
            "Shift Briefing",
            '<p>You are starting your regular 16-hour shift.</p><a href="/cockpit">Enter Cockpit</a>',
            image_key="intro"
        ))

    elif path == "/cockpit":
        return html_response(get_page(
            "Cockpit",
            '''<p>Did you bring your lunch?</p>
               <a href="/lunch?choice=yes">Yes</a><br>
               <a href="/lunch?choice=no">No</a>''',
            image_key="cockpit"
        ))

    elif path == "/lunch":
        choice = query.get("choice", "no")
        message = (
            "Aw yeah! Brought my box of Parliments and my medium iced regular from Dunkies!"
            if choice == "yes"
            else "Cigarette butt again..."
        )
        return html_response(get_page(
            "Lunch Check",
            f'<p>{message}</p><a href="/start_train">Start Train</a>',
            image_key=f"lunch_{choice}"
        ))

    elif path == "/start_train":
        return html_response(get_page(
            "Train Started",
            '''<p>Choose your stop:</p>
               <ul>
                   <li><a href="/stop/BU">B Line</a></li>
                   <li><a href="/stop/BC">BC Stop</a></li>
                   <li><a href="/stop/Kenmore">Kenmore</a></li>
               </ul>''',
            image_key="train_starting"
        ))

    elif path.startswith("/stop/"):
        stop = path.split("/")[-1]
        return html_response(get_page(
            "Arrival",
            f'<p>You arrive at <strong>{stop}</strong>.</p><p>Shift complete. Well done.</p><a href="/">Play Again</a>',
            image_key=stop
        ))

    return html_response(get_page("404 - Not Found", ""), 404)

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

