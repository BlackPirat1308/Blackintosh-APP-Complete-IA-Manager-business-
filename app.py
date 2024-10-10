from flask import Flask, jsonify
from flask_cors import CORS
from blackintosh_seo_ai import BlackintoshSEOAI

app = Flask(__name__)
CORS(app)

ai = BlackintoshSEOAI()

@app.route('/generate_marketing_strategy')
def generate_marketing_strategy():
    return jsonify({"result": ai.generate_marketing_strategy()})

@app.route('/analyze_sales')
def analyze_sales():
    return jsonify({"result": ai.analyze_sales()})

@app.route('/generate_content_idea')
def generate_content_idea():
    return jsonify({"result": ai.generate_content_idea()})

@app.route('/optimize_communication')
def optimize_communication():
    return jsonify({"result": ai.optimize_communication()})

@app.route('/suggest_saas_feature')
def suggest_saas_feature():
    return jsonify({"result": ai.suggest_saas_feature()})

@app.route('/calculate_seo_score')
def calculate_seo_score():
    score = ai.calculate_seo_score()
    recommendation = ai.get_seo_recommendations(score)
    return jsonify({"result": f"Your SEO score is: {score:.2f}/100\n{recommendation}"})

@app.route('/manage_social_connections')
def manage_social_connections():
    return jsonify({"result": ai.manage_social_connections()})

if __name__ == '__main__':
    app.run(debug=True)