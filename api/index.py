import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

PORTFOLIO_DATA = {
    "name": "Muhammad Sohaib Qureshi",
    "title": "Lead Flutter Developer",
    "subtitle": "Mobile App Engineer · Cross-Platform Specialist",
    "location": "Islamabad, Pakistan",
    "email": "sohaibqureshi1997@gmail.com",
    "phone": "+92 308 887 9105",
    "linkedin": "https://linkedin.com/in/sohaibqureshi234",
    "github": "https://github.com/sohaibqureshi",
    "summary": "4+ years shipping production-grade iOS & Android apps across healthcare, fintech, AI, and consumer domains. I lead teams, define mobile architecture, and care deeply about performance, clean code, and real-world impact.",
    "stats": [
        {"number": "4+", "label": "Years Experience"},
        {"number": "5+", "label": "Live Apps Shipped"},
        {"number": "3", "label": "Domains Served"},
        {"number": "2", "label": "Platforms (iOS & Android)"},
    ],
    "skills": {
        "Mobile": ["Flutter", "Dart", "iOS", "Android", "Cross-Platform"],
        "Architecture": ["Clean Architecture", "MVVM", "Repository Pattern", "Design Patterns"],
        "State Management": ["GetX", "BLoC", "Provider", "Riverpod"],
        "Backend": ["Python 3", "JavaScript", "Express.js", "REST APIs", "GraphQL", "WebSockets"],
        "Firebase": ["Auth", "Firestore", "Cloud Functions", "Push Notifications", "AdMob"],
        "Testing": ["Unit Testing", "Widget Testing", "Integration Testing", "mockito"],
        "DevOps": ["Git", "GitHub Actions", "Fastlane", "CI/CD", "Agile", "Scrum"],
        "UI & Design": ["Custom Animations", "Lottie", "Hero Animations", "Figma Collaboration"],
    },
    "experience": [
        {
            "role": "Lead Flutter Developer",
            "company": "Redcoast Corporation",
            "period": "Sep 2023 – Present",
            "location": "Islamabad, Pakistan",
            "highlights": [
                "Architected and shipped 5 cross-platform mobile apps (iOS & Android) following Clean Architecture and MVVM",
                "Led a team of 3 developers, conducted code reviews, and collaborated with designers via Figma",
                "Integrated Firebase, Google Maps SDK, GraphQL, WebSockets, AdMob, and CI/CD via GitHub Actions + Fastlane",
                "Wrote unit/widget/integration tests and used Flutter DevTools for performance profiling",
            ],
        },
        {
            "role": "Co-Founder & Flutter Developer",
            "company": "HilfiTech",
            "period": "Apr 2023 – Present",
            "location": "Remote, Pakistan",
            "highlights": [
                "Co-founded HilfiTech and built TallyTask — live on App Store & Play Store",
                "Implemented AI-driven task automation, role-based access, biometric auth, and real-time dashboards",
                "Reduced manual data entry by ~60% through automated petty cash management",
                "Maintained smooth 60fps rendering via Flutter DevTools performance profiling",
            ],
        },
        {
            "role": "Flutter Developer",
            "company": "Innovo Technologies",
            "period": "Jan 2022 – Aug 2023",
            "location": "Islamabad, Pakistan",
            "highlights": [
                "Developed Vehicle Wallet Driver — an AI-powered fleet fuel management platform for Saudi Arabia's logistics sector",
                "Built a two-sided system (driver app + gas station app) with multi-level security and real-time monitoring",
                "Integrated REST APIs, GraphQL, Payment SDKs, Google Maps, and localization for the Saudi market",
                "Managed version control and releases using Git and Bitbucket",
            ],
        },
        {
            "role": "Flutter Developer (Freelance)",
            "company": "Addictive Receipts",
            "period": "2025 – Present",
            "location": "Remote",
            "highlights": [
                "Designed and shipped Addictive Receipts — live on App Store & Play Store",
                "Built AI-powered receipt verification with PayPal and Amazon Gift Card payouts",
                "Contributed to the Python 3 REST API backend with Google Cloud OCR integration",
                "Delivered full App Store Optimization (ASO) across both stores",
            ],
        },
    ],
    "projects": [
        {
            "name": "KOTA Companion",
            "domain": "Healthcare / AI",
            "description": "HIPAA-compliant AI companion for elderly users — daily check-ins, emergency escalation, conversational AI, and family/agency alerts.",
            "stack": ["Flutter", "Firebase", "AI/LLM", "Speech-to-Text", "HIPAA"],
            "appstore": "https://apps.apple.com/us/app/kota-companion/id6753275339",
            "playstore": "https://play.google.com/store/apps/details?id=com.ankota.kotacompanion",
            "color": "#00e5c3",
        },
        {
            "name": "Vehicle Wallet Driver",
            "domain": "Fintech / Logistics",
            "description": "AI-powered fleet fuel management for Saudi Arabia's logistics sector. Two-sided system with real-time transaction monitoring, VAT invoicing, and vehicle tracking.",
            "stack": ["Flutter", "REST APIs", "Payment SDKs", "Google Maps", "Localization"],
            "appstore": "https://apps.apple.com/in/app/vehicle-wallet-driver/id1642732035",
            "playstore": "https://play.google.com/store/apps/details?id=sa.vehiclewallet.driver",
            "color": "#5b8fff",
        },
        {
            "name": "Ankota FMS",
            "domain": "Healthcare",
            "description": "Healthcare management app with real-time budget tracking, EVV compliance, expense submission with receipts, and service hours monitoring.",
            "stack": ["Flutter", "Firebase", "REST APIs", "Provider", "Google Maps"],
            "appstore": "https://apps.apple.com/us/app/ankota-fms/id6479892000",
            "playstore": "https://play.google.com/store/apps/details?id=com.ankota.fms",
            "color": "#a78bfa",
        },
        {
            "name": "Addictive Receipts",
            "domain": "Consumer / AI",
            "description": "Rewards app with AI receipt verification, PayPal & Amazon Gift Card payouts, and a brand advertising platform with real-time analytics.",
            "stack": ["Flutter", "Firebase", "Camera API", "AI OCR", "REST APIs"],
            "appstore": "https://apps.apple.com/us/app/addictive-receipts/id6756893922",
            "playstore": "https://play.google.com/store/apps/details?id=com.addictive.receipts",
            "color": "#f97316",
        },
        {
            "name": "TallyTask",
            "domain": "Fintech / Productivity",
            "description": "Fintech project management app with AI task automation, role-based access, biometric authentication, and real-time expense tracking.",
            "stack": ["Flutter", "Firebase", "Biometric Auth", "GetX", "REST APIs"],
            "appstore": "https://apps.apple.com/us/app/tallytask/id6584517068",
            "playstore": "https://play.google.com/store/apps/details?id=com.hilfitech.tallytick",
            "color": "#ec4899",
        },
    ],
}


@app.route("/")
def index():
    return render_template("index.html", data=PORTFOLIO_DATA)


if __name__ == "__main__":
    app.run(debug=True)
