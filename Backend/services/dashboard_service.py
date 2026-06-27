from models.problem import Problem
from sqlalchemy import func
from datetime import datetime, timedelta,timezone
def get_dashboard_stats(db,current_user):
    problems = db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()
    total = db.query(
        func.count(Problem.id) # for Optimization query
    ).scalar()
    easy = db.query(
        func.count(Problem.id)
    ).filter(
        Problem.difficulty == "Easy"
    ).scalar()
    medium = db.query(
        func.count(Problem.id)
    ).filter(
        Problem.difficulty == "Medium"
    ).scalar()
    hard = db.query(
        func.count(Problem.id)
    ).filter(
        Problem.difficulty == "Hard"
    ).scalar()
    topic_stats = {}
    for p in problems:
        if p.topic in topic_stats:
            topic_stats[p.topic]+=1
        else:
            topic_stats[p.topic]=1
    return{
        "total":total,
        'easy':easy,
        "medium":medium,
        'hard':hard,
        "topics":topic_stats
    }
def get_user_progress(db,current_user):
    problems= db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()
    total_solved = len(problems)
    seven_days_ago = datetime.now(timezone.utc)-timedelta(days=7)
    last_7 = len([
        p for p in problems
        if p.solved_at >= seven_days_ago
    ])
    progerss_map = {}
    for p in problems:
        date_str = p.solved_at.strftime("%Y-%m-%d")
        if date_str in progerss_map:
            progerss_map[date_str]+=1
        else:
            progerss_map[date_str]=1
    daily_progress= []
    for date,count in progerss_map.items():
        daily_progress.append({
            "date":date,
            'count': count

        })
        return{
            'total_solved':total_solved,
            'last_7_days':last_7,
            'daily_progress':daily_progress
        }