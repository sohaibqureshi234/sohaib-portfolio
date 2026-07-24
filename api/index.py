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
    "title": "Senior Flutter Developer",
    "subtitle": "Flutter Web & Mobile · Clean Architecture · AI/OCR Integrations",
    "location": "Islamabad, Pakistan",
    "email": "sohaibqureshi1997@gmail.com",
    "phone": "+92 308 887 9105",
    "linkedin": "https://linkedin.com/in/sohaibqureshi234",
    "github": "https://github.com/sohaibqureshi234",
    "summary": "Senior Flutter Developer with 4+ years of experience building production mobile and web applications across healthcare, fintech, logistics, and social-discovery domains.",
    "stats": [
        {"number": "4+", "label": "Years Experience"},
        {"number": "5", "label": "Production Applications"},
        {"number": "4", "label": "Platform Targets"},
        {"number": "4", "label": "Product Domains"},
    ],
    "about": [
        "I build production mobile and web applications with Flutter and Dart, with strong experience in Clean Architecture, REST and GraphQL integrations, Firebase, native platform integrations, testing, and performance optimization.",
        "I adapt architecture and state management to the product and its existing codebase. My hands-on experience spans BLoC, GetX, Provider, and Riverpod, supported by code reviews, technical guidance, release preparation, and CI/CD workflows.",
        "My recent work includes healthcare workflows, Flutter Web, native Kotlin and Swift integrations, AI-powered OCR and speech features, BLE and MQTT device communication, and Android TV optimization.",
    ],
    "details": [
        {"label": "Location", "value": "Islamabad, Pakistan"},
        {"label": "Platforms", "value": "iOS · Android · Web · Android TV"},
        {"label": "Education", "value": "BS Software Engineering, CECOS University · October 2021"},
        {"label": "AI & OCR", "value": "Google Cloud Vision · OpenAI · Grok · Speech-to-Text"},
        {"label": "Backend Growth", "value": ".NET / C# · FastAPI"},
    ],
    "skills": {
        "Flutter Platforms": ["Flutter", "Dart", "Flutter Web", "iOS", "Android", "Android TV"],
        "Architecture": ["Clean Architecture", "MVVM", "Repository Pattern", "Design Patterns"],
        "State Management": ["GetX", "BLoC", "Provider", "Riverpod"],
        "APIs & Firebase": ["REST APIs", "GraphQL", "WebSockets", "Firebase", "Firestore", "FCM", "Crashlytics", "OneSignal"],
        "Native & Devices": ["Kotlin", "Swift", "SwiftUI", "Platform Channels", "BLE", "MQTT", "Google Maps SDK"],
        "AI Integrations": ["Google Cloud Vision OCR", "OpenAI API", "Grok API", "Real-time Speech-to-Text"],
        "Data & Tooling": ["SQLite", "Hive", "Shared Preferences", "Flutter DevTools", "AppDynamics", "Jira"],
        "Quality & Delivery": ["Unit Testing", "Widget Testing", "Integration Testing", "Git", "CI/CD", "Fastlane", "GitHub Actions"],
    },
    "experience": [
        {
            "role": "Senior Flutter Developer",
            "company": "RedCoast Corporation",
            "period": "Sep 2024 – Present",
            "location": "Islamabad, Pakistan",
            "highlights": [
                "Contribute across 5 production applications, helping define architecture standards, review implementation approaches, and support team members through code reviews and technical guidance.",
                "Built major features for KOTA Companion and Ankota FMS, including EVV-related workflows, budget tracking, role-based access control, and secure healthcare user flows.",
                "Extended Ankota FMS from a mobile-focused codebase to Flutter Web so iOS, Android, and Web share business logic and core UI patterns.",
                "Added and maintained unit, widget, and integration tests for production features, regression checks, and release preparation.",
                "Implemented native Kotlin and Swift integrations for platform-specific requirements, including Android TV optimization work for Peeq.",
            ],
        },
        {
            "role": "Senior Flutter Engineer",
            "company": "HilfiTech",
            "period": "May 2023 – Aug 2024",
            "location": "Remote · Dubai",
            "highlights": [
                "Owned mobile delivery for TallyTask, covering Flutter architecture, API integration, testing, release support, and production issue resolution for iOS and Android.",
                "Built Addictive Receipts and Addictive Ads with Google Cloud Vision OCR, receipt processing, and reward-redemption workflows while coordinating on FastAPI service contracts.",
                "Used Flutter DevTools to resolve UI jank, memory usage, and release-stability regressions.",
            ],
        },
        {
            "role": "Mobile Application Developer",
            "company": "Innovo Technologies",
            "period": "Jan 2022 – Apr 2023",
            "location": "Islamabad, Pakistan",
            "highlights": [
                "Built Vehicle Wallet Driver and its companion Station app, a two-sided fleet fuel platform for the Saudi logistics market with real-time transactions, VAT-compliant invoicing, and multiple user roles.",
                "Implemented MVVM and the Repository Pattern with GraphQL, REST APIs, Google Maps SDK, offline-first local storage, and Arabic localization.",
                "Delivered features from requirements analysis through development, QA support, release, and post-release fixes with product, backend, and QA stakeholders.",
            ],
        },
    ],
    "projects": [
        {
            "name": "KOTA Companion",
            "domain": "Healthcare AI",
            "platforms": "iOS · Android",
            "description": "Healthcare AI companion with AI integration, secure user flows, and healthcare-focused workflows.",
            "stack": ["Flutter", "AI Integration", "Secure User Flows", "Healthcare Workflows"],
            "appstore": "https://apps.apple.com/us/app/kota-companion/id6753275339",
            "playstore": "https://play.google.com/store/apps/details?id=com.ankota.kotacompanion",
            "color": "#00e5c3",
        },
        {
            "name": "Ankota FMS",
            "domain": "Healthcare Operations",
            "platforms": "iOS · Android · Web",
            "description": "Healthcare operations platform extended to Flutter Web, with EVV-related workflows, budget tracking, and shared business logic across platforms.",
            "stack": ["Flutter Web", "EVV Workflows", "Budget Tracking", "Shared Business Logic"],
            "appstore": "https://apps.apple.com/us/app/ankota-fms/id6479892000",
            "playstore": "https://play.google.com/store/apps/details?id=com.ankota.fms",
            "color": "#5b8fff",
        },
        {
            "name": "TallyTask",
            "domain": "Fintech & Workforce Management",
            "platforms": "iOS · Android",
            "description": "Fintech and workforce-management platform delivered across mobile architecture, API integration, testing, release support, and production issue resolution.",
            "stack": ["Flutter Architecture", "API Integration", "Testing", "Release Support"],
            "appstore": "https://apps.apple.com/us/app/tallytask/id6584517068",
            "playstore": "https://play.google.com/store/apps/details?id=com.hilfitech.tallytick",
            "color": "#a78bfa",
        },
        {
            "name": "Vehicle Wallet Driver / Station",
            "domain": "Fleet Fuel Management",
            "platforms": "Saudi Market · iOS · Android",
            "description": "Two-sided fleet fuel platform supporting real-time transactions, VAT-compliant invoicing, Arabic localization, maps, and multiple user roles.",
            "stack": ["MVVM", "GraphQL", "REST APIs", "Google Maps", "Arabic Localization"],
            "appstore": "https://apps.apple.com/in/app/vehicle-wallet-driver/id1642732035",
            "playstore": "https://play.google.com/store/apps/details?id=sa.vehiclewallet.driver",
            "color": "#f97316",
        },
        {
            "name": "Minew BLE Button Project",
            "domain": "Connected Devices",
            "platforms": "Flutter · Native Device Communication",
            "description": "BLE and MQTT integration demonstrating Flutter-native device communication. Portfolio or GitHub sample is available where client permissions allow.",
            "stack": ["Flutter", "BLE", "MQTT", "Platform Channels"],
            "color": "#ec4899",
        },
    ],
}


@app.route("/")
def index():
    return render_template("index.html", data=PORTFOLIO_DATA)


if __name__ == "__main__":
    app.run(debug=True)
