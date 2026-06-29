import requests
from datetime import timedelta,timezone,datetime
import time

def get_leetcode_profile(username: str):
    start = time.time()
    url = "https://leetcode.com/graphql"

    query = """
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            profile {
                ranking
            }
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
        userContestRanking(username: $username) {
            attendedContestsCount
            rating
            globalRanking
            topPercentage
        }
        userContestRankingHistory(username: $username) {
            attended
            trendDirection
            problemsSolved
            totalProblems
            rating
            ranking
            contest {
                title
                startTime
            }
        }
    }
    """

    variables = {"username": username}

    headers = {
        # Tells LeetCode we are sending JSON
        "Content-Type": "application/json",
        # Helps bypass CSRF protection
        "Referer": "https://leetcode.com",
        # Browser-like request
        "User-Agent": "Mozilla/5.0",
    }

    response = requests.post(
        url, json={"query": query, "variables": variables}, headers=headers
    )

    # DEBUGGING
    print(response.status_code)
    print(response.text)

    # SAFE JSON HANDLING
    try:
        data = response.json()
    except Exception:
        return {"error": "Response is not JSON", "response_text": response.text}

    # LEETCODE ERROR HANDLING
    if "data" not in data:
        return {"error_from_leetcode": data}

    payload = data["data"]
    matched_user = payload.get("matchedUser")

    if not matched_user:
        return {"message": "Leetcode user not found"}

    # PROBLEM STATS
    raw_stats = matched_user["submitStats"]["acSubmissionNum"]
    stats_map = {item["difficulty"]: item["count"] for item in raw_stats}

    # CONTEST DATA
    contest_ranking = payload.get("userContestRanking") or {}
    contest_history = payload.get("userContestRankingHistory") or []
    end = time.time()
    total_time = end - start
    print(f"total time taken for one request{total_time:.2f} seconds ")

    return {
        # BASIC USER INFO
        "username": matched_user["username"],
        "ranking": matched_user["profile"]["ranking"],
        # PROBLEM ANALYTICS
        "easy_solved": stats_map.get("Easy", 0),
        "medium_solved": stats_map.get("Medium", 0),
        "hard_solved": stats_map.get("Hard", 0),
        "total_solved": stats_map.get("All", 0),
        # CONTEST ANALYTICS
        "contest_rating": contest_ranking.get("rating", 0),
        "contest_global_ranking": contest_ranking.get("globalRanking", 0),
        "contest_top_percentage": contest_ranking.get("topPercentage", 0),
        "contests_attended": contest_ranking.get("attendedContestsCount", 0),
        # CONTEST HISTORY
        "contest_history": contest_history,
    }
def sync_leetcode_data(
        db,current_user
):
    if not current_user.leetcode_username:
        return {
            'message':"LeetCode username not linked"
        }
    profile_data = get_leetcode_profile(
        current_user.leetcode_username
    )
    current_user.leetcode_ranking = profile_data.get(
        "ranking",0
    )
    current_user.easy_solved= profile_data.get(
        "easy_solved",0
    )
    current_user.medium_solved = profile_data.get(
        "medium_solved", 0
    )
    current_user.hard_solved = profile_data.get(
        "hard_solved",0
    )
    current_user.total_solved = profile_data.get(
        "total_solved",0
    )
    current_user.contest_rating = profile_data.get(
        "contest_rating",0
    )
    current_user.contest_global_ranking=profile_data.get(
        "contest_global_ranking",0
    )
    current_user.contest_top_percentage =profile_data.get(
        "contest_top_percentage",0
    )
    current_user.contest_attended=profile_data.get(
        "contest_attended",0
    )
    current_user.last_synced = datetime.now(
        timezone.utc 
    )
    db.commit()
    update_user = db.query(type(current_user)).filter(
        type(current_user).id == current_user.id
    ).first()
    return{
        'message':"LeetCode data synced successfull",
        "last_synced": update_user.last_synced
    }

def get_cache_profile(
        current_user
):
    return{
        "leetcode_username": current_user.leetcode_username,
        "ranking":current_user.leetcode_ranking,
        "easy_solved":current_user.easy_solved,
        "medium_solved":current_user.medium_solved,
        'hard_solved':current_user.hard_solved,
        "total_solved":current_user.total_solved,
        "contest_rating":current_user.contest_rating,
        "contest_global_ranking":current_user.contest_global_ranking,
        "contest_top_percentage":current_user.contest_top_percentage,
        "contests_attended":current_user.contest_attended,
        "last_synced":current_user.last_synced
    }


