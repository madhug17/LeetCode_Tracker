# 🚀 LeetCode Tracker

A full-stack LeetCode progress tracker built with **FastAPI**, **PostgreSQL**, **Docker**, **Kubernetes**, and **Vanilla JavaScript** — designed to help users log problems, track streaks, visualize progress, and get AI-powered recommendations on what to solve next.

Live demo: [leetcode-tracker-frontend-puxu.onrender.com](https://leetcode-tracker-frontend-puxu.onrender.com)

---


## ✨ Features

### Authentication
- User registration & secure login (JWT access + refresh tokens)
- Password hashing with bcrypt
- Protected routes via auth middleware

### Problem Tracking
- Add, view, and delete solved problems (title, difficulty, topic, time spent, notes)
- Difficulty and topic breakdown via interactive Chart.js visualizations

### Streaks & Consistency
- Current streak, longest streak, active days, and consistency percentage
- GitHub-style activity heatmap

### LeetCode Sync
- Sync LeetCode profile stats (easy/medium/hard solved, ranking, contest rating)

### AI Recommendations
- Personalized suggestions on what to practice next based on solve history

### Dashboard
- Unified view combining profile stats, streaks, heatmap, and charts

---

## 🛠 Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL, JWT, Passlib, Uvicorn
**Frontend:** HTML5, CSS3, Vanilla JavaScript, Chart.js
**Infrastructure:** Docker, Kubernetes
**Deployment:** Render (backend + static frontend)
**CI/CD:** GitHub Actions *(planned)*

---

## 📁 Project Structure

```text
LeetCode_Tracker
│
├── Backend
│   ├── core
│   ├── database
│   ├── k8s              # Deployments, Services, HPA, metrics-server config
│   ├── models
│   ├── nginx
│   ├── routers
│   ├── schemas
│   ├── services
│   ├── utils
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── main.py
│   └── requirements.txt
│
├── Frontend
│   ├── css
│   │   └── style.css
│   ├── js
│   │   ├── api.js
│   │   ├── login.js
│   │   ├── register.js
│   │   └── dashboard.js
│   ├── index.html
│   ├── register.html
│   └── dashboard.html
│
└── README.md
```

---

## ⚙ Getting Started

### Clone the repo

```bash
git clone https://github.com/madhug17/LeetCode_Tracker.git
cd LeetCode_Tracker
```

### Backend setup

```bash
cd Backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```



### Run locally

```bash
uvicorn main:app --reload
```

- API: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

### Run with Docker

```bash
docker compose up --build
```

### Deploy to Kubernetes

```bash
kubectl apply -f Backend/k8s/
```

---

## 🔒 Auth Flow

```text
Register → Login → Access Token → Protected Routes → Refresh Token (on expiry)
```

---

## 📌 API Reference

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Log in, returns access + refresh tokens |

### LeetCode
| Method | Endpoint | Description |
|---|---|---|
| GET | `/leetcode/profile` | Fetch synced LeetCode stats |
| POST | `/leetcode/sync` | Sync latest stats from LeetCode |

### Problems
| Method | Endpoint | Description |
|---|---|---|
| POST | `/problems/add` | Log a solved problem |
| GET | `/problems/my-problem` | List all logged problems |
| DELETE | `/problems/{id}` | Delete a logged problem |

### Streaks
| Method | Endpoint | Description |
|---|---|---|
| GET | `/streak/all` | Current streak, longest streak, consistency |
| GET | `/streak/heatmap` | Daily activity data for heatmap |

### Dashboard
| Method | Endpoint | Description |
|---|---|---|
| GET | `/dashboard/ai-recommendation` | AI-generated practice suggestions |

---


## 📖 What I Learned Building This

- Designing and securing a REST API with FastAPI + JWT
- Modeling relational data with SQLAlchemy + PostgreSQL
- Debugging real production issues: CORS, CI/CD pipelines, container networking, database integrity constraints
- Containerizing and orchestrating a multi-service app with Docker and Kubernetes
- Connecting a vanilla JS frontend to a deployed API (auth flows, token storage, protected routes)

---

## 👨‍💻 Author

**Madhu Goud**
B.Tech AI & ML, Woxsen University

- GitHub: [github.com/madhug17](https://github.com/madhug17)
- LinkedIn: [linkedin.com/in/goundla-madhu-goud-511002325](https://linkedin.com/in/goundla-madhu-goud-511002325)

---

## ⭐ Support

If this project helped you, consider starring the repo, forking it, or opening a PR with improvements.

---

## 📜 License

MIT License