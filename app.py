from flask import Flask, render_template, request, redirect, url_for, session, send_file, send_from_directory
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import os
import time
real_time_date = time.strftime("%d-%m-%y")

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "generated_files")  # Folder to store PDFs

os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure folder exists

cric_result = {
    "q1": "11",
    "q2": "22 yards",
    "q3": "West Indies",
    "q4": "Sachin Tendulkar",
    "q5": "264",
    "q6": "Muttiah Muralitharan",
    "q7": "20",
    "q8": "Australia",
    "q9": "Brian Lara",
    "q10": "1975"
}

history_result = {
    "q1": "1914",
    "q2": "George Washington",
    "q3": "Ancient Egyptians",
    "q4": "American Civil War",
    "q5": "Adolf Hitler",
    "q6": "1492",
    "q7": "Silk Road",
    "q8": "Qin Shi Huang",
    "q9": "Storming of the Bastille",
    "q10": "Mahatma Gandhi"
}

env_result = {
    "q1": "Trapping of heat by atmospheric gases",
    "q2": "Carbon dioxide (CO2)",
    "q3": "Clearing of forests",
    "q4": "Reduce waste and conserve resources",
    "q5": "Biodiversity",
    "q6": "Sulfur dioxide and nitrogen oxides",
    "q7": "Absorb harmful UV radiation",
    "q8": "Meeting current needs without compromising future needs",
    "q9": "Land-based human activities",
    "q10": "Solar energy"
}

elec_result = {
    "q1": "Light Emitting Diode",
    "q2": "Ohm",
    "q3": "DC",
    "q4": "Store electrical energy",
    "q5": "Amplifies signals",
    "q6": "Allows current in one direction",
    "q7": "Capacitor",
    "q8": "Blocks DC and allows AC",#
    "q9": "To prevent excessive current flow",  
    "q10": "Silicon" 
}


gk_result= {
    "q1": "Paris",
    "q2": "Trapping of heat by atmospheric gases",
    "q3": "Mars",
    "q4": "Carbon dioxide (CO2)",
    "q5": "Pacific Ocean",
    "q6": "Australia",
    "q7": "Blue whale",
    "q8": "Leonardo da Vinci",
    "q9": "Yen",
    "q10": "7"
}

math_result = {
    "q1": "56",         # 7 × 8 = 56
    "q2": "12",         # √144 = 12
    "q3": "3.14",       # Approximate value of π
    "q4": "30",         # 15% of 200 = (15/100) × 200 = 30
    "q5": "50",         # Area of rectangle = length × width = 10 × 5 = 50
    "q6": "16",         # 2^4 = 16
    "q7": "180 degrees",# Sum of angles in a triangle = 180°
    "q8": "100",        # 1000 ÷ 10 = 100
    "q9": "13",         # Next prime number after 11 is 13
    "q10": "7"          # x + 5 = 12 → x = 12 - 5 = 7
}

tech_result = {
    "q1": "Central Processing Unit",
    "q2": "Random Access Memory",
    "q3": "Manage hardware and software resources",
    "q4": "HyperText Markup Language",
    "q5": "Network security",
    "q6": "Internet Protocol address",
    "q7": "Delivering computing services over the Internet",
    "q8": "A set of instructions for a computer to execute",
    "q9": "To connect multiple networks",
    "q10": "Uniform Resource Locator"
}

app.secret_key = "your_secret_key"  # Needed for session handling

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        return render_template("data.html")
    return render_template("index.html")

@app.route('/static/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)  


@app.route("/data", methods=["POST"])
def details():
    session['name'] = request.form.get('name', 'Guest')
    session['email'] = request.form.get('email', 'Not provided')
    session['type'] = request.form.get('type', 'User')
    session['country'] = request.form.get('country', 'Unknown')
    session['interest'] = request.form.get('interest', 'General Knowledge')

    interest_redirects = {
        "Cricket": 'cricket',
        "History": 'history',
        "Technology": 'tech',
        "General Knowledge": 'gk',
        "Maths": 'math',
        "Electronic": 'electronic',
        "Environment": 'environment'
    }

    return redirect(url_for(interest_redirects.get(session['interest'], 'home')))



@app.route('/cricket', methods=['GET', 'POST'])
def cricket():
    user_score = 0

    if request.method == 'POST':
        for x in range(1, 11):
            user_answer = request.form.get(f'q{x}', '').strip()  # Get and strip the user's answer
            
            if user_answer:  # Only store if the user selected an option
                session[f'q{x}'] = user_answer

            # Compare with correct answer (case insensitive)
            if user_answer.lower() == cric_result.get(f'q{x}', '').lower():
                user_score += 1

        session['score'] = user_score  # Store the score in session
        return render_template("result.html", score=user_score)

    return render_template("cricket.html", name=session.get('name', 'Guest'))  


@app.route('/history', methods=['GET', 'POST'])
def history():
    user_score = 0

    if request.method == 'POST':
        for x in range(1, 11):
            user_answer = request.form.get(f'q{x}', '').strip()  # Get and strip the user's answer
            
            if user_answer:  # Only store if the user selected an option
                session[f'q{x}'] = user_answer

            # Compare with correct answer (case insensitive)
            if user_answer.lower() == history_result.get(f'q{x}', '').lower():
                user_score += 1

        session['score'] = user_score  # Store the score in session
        return render_template("result.html", score=user_score)
    
    return render_template("history.html", name=session.get('name', 'Guest'))


@app.route('/tech',  methods=['GET', 'POST'])
def tech():
    user_score = 0

    if request.method == 'POST':
        for x in range(1, 11):
            user_answer = request.form.get(f'q{x}', '').strip()  # Get and strip the user's answer
            
            if user_answer:  # Only store if the user selected an option
                session[f'q{x}'] = user_answer

            # Compare with correct answer (case insensitive)
            if user_answer.lower() == tech_result.get(f'q{x}', '').lower():
                user_score += 1

        session['score'] = user_score  # Store the score in session
        return render_template("result.html", score=user_score)
    return render_template("tech.html", name=session.get('name', 'Guest'))


@app.route('/gk', methods=['GET', 'POST'])
def gk():
    user_score = 0

    if request.method == 'POST':
        for x in range(1, 11):
            user_answer = request.form.get(f'q{x}', '').strip()  # Get and strip the user's answer
            
            if user_answer:  # Only store if the user selected an option
                session[f'q{x}'] = user_answer

            # Compare with correct answer (case insensitive)
            if user_answer.lower() == gk_result.get(f'q{x}', '').lower():
                user_score += 1

        session['score'] = user_score  # Store the score in session
        return render_template("result.html", score=user_score)
    return render_template("gk.html", name=session.get('name', 'Guest'))


@app.route('/math', methods=['GET', 'POST'])
def math():
    user_score = 0

    if request.method == 'POST':
        for x in range(1, 11):
            user_answer = request.form.get(f'q{x}', '').strip()  # Get and strip the user's answer
            
            if user_answer:  # Only store if the user selected an option
                session[f'q{x}'] = user_answer

            # Compare with correct answer (case insensitive)
            if user_answer.lower() == math_result.get(f'q{x}', '').lower():
                user_score += 1

        session['score'] = user_score  # Store the score in session
        return render_template("result.html", score=user_score)
    return render_template("math.html", name=session.get('name', 'Guest'))


@app.route('/electronic', methods=['GET', 'POST'])
def electronic():
    user_score = 0

    if request.method == 'POST':
        for x in range(1, 11):
            user_answer = request.form.get(f'q{x}', '').strip()  # Get and strip the user's answer
            
            if user_answer:  # Only store if the user selected an option
                session[f'q{x}'] = user_answer

            # Compare with correct answer (case insensitive)
            if user_answer.lower() == elec_result.get(f'q{x}', '').lower():
                user_score += 1

        session['score'] = user_score  # Store the score in session
        return render_template("result.html", score=user_score)

    return render_template("electronic.html", name=session.get('name', 'Guest'))


@app.route('/environment', methods=['GET', 'POST'])
def environment():
    user_score = 0

    if request.method == 'POST':
        for x in range(1, 11):
            user_answer = request.form.get(f'q{x}', '').strip()  # Get and strip the user's answer
            
            if user_answer:  # Only store if the user selected an option
                session[f'q{x}'] = user_answer

            # Compare with correct answer (case insensitive)
            if user_answer.lower() == env_result.get(f'q{x}', '').lower():
                user_score += 1
        
        session['score'] = user_score  # Store the score in session
        return render_template("result.html", score=user_score)

    return render_template("environment.html", name=session.get('name', 'Guest'))

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        return render_template("certificate.html")

    return render_template('result.html')



@app.route("/download",  methods=['GET', 'POST'])
def download_certificate():
    # Retrieve data from session
    name = session.get("name", "Unknown")
    user_type = session.get("type", "Unknown")
    interest = session.get("interest", "Unknown")
    score = session.get("score", "0")

    filename = os.path.join(UPLOAD_FOLDER, f"{name}_quiz_certificate.pdf")  # Unique filename

    # Create a PDF
    pdf = canvas.Canvas(filename, pagesize=letter)
    width, height = letter  # Get page size

    # Certificate Border
    pdf.setStrokeColorRGB(0, 0, 0)  # Black Border
    pdf.setLineWidth(4)
    pdf.rect(30, 30, width - 60, height - 60, stroke=1, fill=0)


    # Certificate Title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2, height - 100, "QUIZY JUNGLE CERTIFICATE OF ACHIEVEMENT")

    # Subtitle
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(width / 2, height - 140, "This is to certify that")
    # Name
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2, height - 180, f"Mr./Ms. {name}")

    # Achievement Text
    text1 = "has successfully participated in the quiz as a "
    text2 = user_type.capitalize()  # Bold text

    x_position = width / 2
    y_position = height - 220

    # Draw normal text first
    pdf.setFont("Helvetica", 14)
    pdf.drawString(x_position - pdf.stringWidth(text1 + text2, "Helvetica", 14) / 2, y_position, text1)

    # Draw bold text next, slightly adjusted
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x_position - pdf.stringWidth(text1 + text2, "Helvetica", 14) / 2 + pdf.stringWidth(text1, "Helvetica", 14), y_position, text2)



    text1 = "with an interest in "
    text2 = interest  
    text3 = " and achieved a score of"

    x_position = width / 2
    y_position = height - 250

    pdf.setFont("Helvetica", 12)
    pdf.drawRightString(x_position - pdf.stringWidth(text2, "Helvetica-Bold", 12) / 2, y_position, text1)

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x_position - pdf.stringWidth(text2, "Helvetica-Bold", 12) / 2, y_position, text2)

    pdf.setFont("Helvetica", 12)
    pdf.drawString(x_position + pdf.stringWidth(text2, "Helvetica-Bold", 12) / 2, y_position, text3)

    # Score
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(width / 2, height - 290, f"{score} / 10")

    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(width / 2, height - 320, f"Congratulations from MOH_DEV!")

    pdf.drawImage("QJPDF.jpg", (width - 190) / 2, (height - 400) / 2, width=170, height=170)



    # Signature & Date Placeholder
    pdf.setFont("Helvetica-Oblique", 12)
    pdf.drawString(50, 100, "                    MOH_DEV")
    pdf.drawString(50, 100, "Signature: _______________")

    pdf.drawString(width - 200, 100, f"           {real_time_date}")
    pdf.drawString(width - 200, 100, "Date: _______________")

    pdf.save()

    return send_file(filename, as_attachment=True)


@app.route('/reset')
def reset():
    session.clear()  # Clears all stored session data
    return redirect(url_for('home'))  # Redirects to home page for a fresh start


if __name__ == '__main__':
    app.run(debug=True, port=5000)




