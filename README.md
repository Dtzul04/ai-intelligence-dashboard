## Markdown# 📊 AI Intelligence Dashboard

A professional, containerized Flask application for customer churn prediction using Scikit-Learn, Pandas, and Tailwind CSS.

## 🚀 Live Demo
**Project URL:** [ai-intelligence-dashboard-production.up.railway.app]

## 🛠 Project Setup
Before running the app locally, ensure your environment is ready:

1. **Environment Variables**: Create a `.env` file in the root directory.
2. **Add Credentials**:
   ```text
   MYSQL_ROOT_PASSWORD=your_password
   MYSQL_PASSWORD=your_password 

3. Data: Ensure `customer_data.csv` is inside the `/data` folder.

## 🚀 Docker Commands
Use these commands to manage the application:
• Start the App: `docker-compose up --build`
• Stop Services: `docker-compose down`
• Train the AI Model: `docker-compose run --rm web python model_trainer.py`

## 📦 Deployment (Render)
This project is configured for easy deployment on Render:
1. Push your latest changes to GitHub.
2. Log in to **Render.com** and create a new **Web Service**.
3. Connect your GitHub repository.
4. Select **Docker** as the Runtime.
5. Add your Environment Variables (MYSQL credentials) in the Render 'Environment' tab.
6. Render will automatically build and deploy your container.

## 🌳 Git Branching Workflow
Always work on a feature branch to keep the main branch stable:
1. Create branch: `git checkout -b feature/your-task-name`
2. Save progress: `git add .` then `git commit -m "Description of changes"`
3. Push to GitHub: `git push origin feature/your-task-name`

© 2026 Daniel Tzul