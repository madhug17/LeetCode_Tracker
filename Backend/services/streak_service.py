from collections import defaultdict
from datetime import datetime, timedelta, timezone
from models.problem import Problem

def get_daily_tracker(db, current_user):
    problems = db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()

    tracker = defaultdict(int)
    for problem in problems:
        solved_date = problem.solved_at.date().isoformat()
        tracker[solved_date] += 1

    return tracker

def get_current_streak(db, current_user):
    problems = db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()

    solved_dates = {problem.solved_at.date() for problem in problems}

    today = datetime.now(timezone.utc).date()
    current_streak = 0
    while today in solved_dates:
        current_streak += 1
        today = today - timedelta(days=1)

    return {
        "current_streak": current_streak
    }

def get_longest_streak(db, current_user):
    problems = db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()

    solved_dates = sorted(
        {problem.solved_at.date() for problem in problems}
    )

    if not solved_dates:
        return {
            "longest_streak": 0
        }

    longest_streak = 1
    current_streak = 1
    for i in range(1, len(solved_dates)):
        previous_day = solved_dates[i - 1]
        current_day = solved_dates[i]
        if current_day == previous_day + timedelta(days=1):
            current_streak += 1
        else:
            current_streak = 1
        longest_streak = max(longest_streak, current_streak)

    return {
        "longest_streak": longest_streak
    }

def get_consistency_tracking(db, current_user):
    problems = db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()

    active_days = {
        problem.solved_at.date()
        for problem in problems
    }

    total_active_days = len(active_days)
    total_days = 30
    consistency_percentage = (total_active_days / total_days) * 100

    return {
        "active_days": total_active_days,
        "total_days": total_days,
        "consistency_percentage": round(consistency_percentage, 2)
    }
def get_heatmap_data(db, current_user):
    problems = db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()

    heatmap = {}
    for problem in problems:
        solved_date = problem.solved_at.date().isoformat()
        if solved_date not in heatmap:
            heatmap[solved_date] = 0
        heatmap[solved_date] += 1

    results = []
    for date, count in heatmap.items():
        results.append({
            "date": date,
            "count": count
        })

    return results