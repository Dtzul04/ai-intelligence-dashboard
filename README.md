# 📊 AI Intelligence Dashboard

A professional, containerized Flask application for customer churn prediction using Scikit-Learn, Pandas, and Tailwind CSS.

## 🚀 Live Demo
**Project URL:** [Insert Railway Link Here after deployment]

## 🛠 Project Setup
Before running the app locally, ensure your environment is ready:

1. **Environment Variables**: Create a .env file in the root directory.
2. **Add Credentials**:
   MYSQL_ROOT_PASSWORD=your_password
   MYSQL_PASSWORD=your_password
3. **Data**: Ensure customer_data.csv is inside the /data folder.

## 🚀 Docker Commands
Use these commands to manage the application:

* Start the App: docker-compose up --build
* Stop Services: docker-compose down
* Train the AI Model: docker-compose run --rm web python model_trainer.py

## 🧪 Testing the Website
To verify the model logic, try inputting these scenarios into the dashboard:

| Scenario | Tenure | Monthly Charges | Contract Type | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| Loyal Customer | 72 | 20.00 | Two Year (2) | Unlikely to Churn |
| High Risk | 1 | 115.00 | Month-to-month (0) | Likely to Churn |
| Standard User | 24 | 65.00 | One Year (1) | Varies by Model |

## 📦 Deployment (Railway)
This project is Docker-ready for deployment:
1. Push changes to GitHub.
2. Connect repository to Railway.app.
3. Railway will automatically build the container using the Dockerfile.

## 🌳 Git Branching Workflow
Always work on a feature branch to keep the main branch stable:

1. Create branch: git checkout -b feature/your-task-name
2. Save progress: git add . then git commit -m "Description of changes"
3. Push to GitHub: git push origin feature/your-task-name

---
© 2026 Daniel Tzul
