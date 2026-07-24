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
    "title": "Senior Flutter & AI Engineer",
    "subtitle": "Flutter Mobile & Web · Clean Architecture · AI/LLM Integrations",
    "location": "Islamabad, Pakistan",
    "email": "sohaibqureshi1997@gmail.com",
    "phone": "+92 308 887 9105",
    "whatsapp": "https://wa.me/923088879105?text=Hi%20Sohaib%2C%20I%20found%20your%20portfolio%20and%20would%20like%20to%20connect.",
    "linkedin": "https://www.linkedin.com/in/sohaib-qureshi-4a5654253/",
    "github": "https://github.com/sohaibqureshi234",
    "website": "https://sohaib-portfolio-topaz.vercel.app/",
    "summary": "Senior Flutter & AI Engineer with 4+ years of experience building production mobile and web applications across healthcare, fintech, logistics, fleet operations, and social-discovery products.",
    "stats": [
        {"number": "4+", "label": "Years Experience"},
        {"number": "8", "label": "Products & Platforms"},
        {"number": "4", "label": "Platform Targets"},
        {"number": "5", "label": "Product Domains"},
    ],
    "about": [
        "I build production Flutter applications across mobile and web, combining strong product delivery with Clean Architecture, native integrations, real-time workflows, testing, performance optimization, and release ownership.",
        "My AI integration work spans LLM agents, OpenAI tool-calling workflows, Google Cloud Vision OCR, speech-to-text, and human-in-the-loop safeguards. I use Python/FastAPI and C#/.NET as secondary skills to prototype services, shape API contracts, and collaborate effectively with backend teams.",
        "I have delivered healthcare, fintech, logistics, rewards, fleet-operations, and social-discovery products across iOS, Android, Web, and Android TV, supported by Firebase, REST/GraphQL/WebSockets, PostgreSQL, Redis, Docker, and CI/CD.",
    ],
    "details": [
        {"label": "Location", "value": "Islamabad, Pakistan"},
        {"label": "Platforms", "value": "iOS · Android · Web · Android TV"},
        {"label": "Education", "value": "BS Software Engineering, CECOS University of IT and Emerging Sciences, Peshawar · October 2021"},
        {"label": "AI Engineering", "value": "LLM Agents · OpenAI Responses API · RAG · Tool Calling · OCR"},
        {"label": "Supporting Backend", "value": "FastAPI · C#/.NET · PostgreSQL/pgvector · Redis"},
    ],
    "skills": {
        "Flutter Platforms": ["Flutter", "Dart", "Flutter Web", "iOS", "Android", "Android TV"],
        "Architecture": ["Clean Architecture", "Modular Monolith", "MVVM", "Repository Pattern", "Dependency Injection", "Design Patterns"],
        "State Management": ["GetX", "BLoC", "Provider", "Riverpod"],
        "Backend Collaboration": ["FastAPI", "Python", "C#", ".NET", "ASP.NET Core", "REST APIs", "GraphQL", "WebSockets"],
        "Data & Messaging": ["PostgreSQL", "pgvector", "Redis", "SQLAlchemy", "Alembic", "SQL Server", "SQLite", "Hive"],
        "Cloud & Firebase": ["Firebase", "Firestore", "FCM", "Firebase Crashlytics", "Azure", "Supabase", "OneSignal"],
        "Native & Devices": ["Kotlin", "Swift", "SwiftUI", "Platform Channels", "BLE", "MQTT", "Google Maps SDK"],
        "AI & LLM Engineering": ["LLM Agents", "OpenAI Responses API", "Tool Calling", "RAG", "Human-in-the-Loop AI", "Google Cloud Vision OCR", "Grok API", "Speech-to-Text"],
        "Security": ["JWT", "RBAC", "Firebase Auth", "Multi-tenant Design", "Audit Trails", "Policy-gated AI"],
        "Quality & Delivery": ["Unit Testing", "Widget Testing", "Integration Testing", "Pytest", "Ruff", "mypy", "Docker", "Docker Compose", "Git", "CI/CD", "GitHub Actions", "Fastlane"],
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
                "Architected FleetGuard AI, an autonomous fleet-operations intelligence platform spanning Flutter mobile/web, FastAPI, PostgreSQL/pgvector, Redis, Docker, and explainable LLM tool orchestration.",
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
            "name": "FleetGuard AI",
            "associated_with": "HilfiTech",
            "domain": "Autonomous Fleet Intelligence",
            "platforms": "iOS · Android · Web · Backend",
            "description": "Auditable fleet-operations intelligence platform that validates fuel claims with specialist AI tools, explains every recommendation, and routes uncertain or high-risk decisions to human review.",
            "stack": ["Flutter", "FastAPI", "LLM Agents", "OpenAI Responses API", "PostgreSQL/pgvector", "Redis", "Docker"],
            "color": "#22c55e",
        },
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
            "associated_with": "HilfiTech",
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
            "name": "Addictive Receipts",
            "associated_with": "HilfiTech",
            "domain": "Rewards & OCR",
            "platforms": "iOS · Android",
            "description": "Receipt rewards app for scanning and uploading receipts, tracking verification and reward status, and supporting OCR-driven receipt processing and reward-redemption workflows.",
            "stack": ["Flutter", "Google Cloud Vision OCR", "Camera", "FastAPI", "Rewards"],
            "appstore": "https://apps.apple.com/us/app/addictive-receipts/id6756893922",
            "playstore": "https://play.google.com/store/apps/details?id=com.addictive.receipts&hl=en",
            "color": "#ef4444",
        },
        {
            "name": "Addictive Ads",
            "associated_with": "HilfiTech",
            "domain": "Advertising & Creator Economy",
            "platforms": "iOS · Android",
            "description": "Advertising platform for publishing and sharing ad content, earning through engagement, and tracking campaign views, clicks, reach, and performance.",
            "stack": ["Flutter", "REST APIs", "Content Uploads", "Engagement Analytics", "Rewards"],
            "appstore": "https://apps.apple.com/us/app/addictive-ads/id6762096926",
            "playstore": "https://play.google.com/store/apps/details?id=com.addictiveads.app",
            "color": "#f59e0b",
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
