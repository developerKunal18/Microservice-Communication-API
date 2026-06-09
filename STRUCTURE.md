🧠 Why This Is Important

Instead of one large application:

Monolith
├── Users
├── Orders
├── Payments
└── Inventory

Modern systems often use:

User Service
Order Service
Payment Service
Inventory Service

Each service communicates via APIs.

👉 Used by:

Netflix
Amazon
Uber
Spotify

🛠 Tech Stack
Python
Flask
Requests Library
JSON APIs

📂 Project Structure
microservice-demo/
│
├── user_service.py
├── order_service.py
└── README.md
