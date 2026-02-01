# 📊 AI Intelligence Dashboard

A containerized Flask application for customer churn prediction using Scikit-Learn, Pandas, and Tailwind CSS.

## 🛠 Project Setup
Before running the app, ensure you have your local environment ready:

1. **Environment Variables**: Create a `.env` file in the root directory (this is ignored by Git).
2. **Add Credentials**:
   ```text
   MYSQL_ROOT_PASSWORD=your_password
   MYSQL_PASSWORD=your_password
3. **Data**: Ensure customer_data.csv is inside the /data folder.

## 🚀 Docker Commands

Use these commands to manage the application:

• Start the App: docker-compose up --build

• Stop Services: docker-compose down

• Train the AI Model: docker-compose run --rm web python model_trainer.py

## Git Branching Workflow

To practice professional development habits, always work on a branch:

1. Create a new branch: git checkout -b feature/your-task-name

2. Save your progress: git add . git commit -m "Description of changes"

3. Push to GitHub: git push origin feature/your-task-name