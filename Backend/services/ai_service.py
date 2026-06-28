from collections import defaultdict
from pstats import Stats
def generate_ai_recommendantion(
        problems
):
    topics_stats = defaultdict(
        lambda:{
            "solved":0,
            "attempts":0
        }
    )
    for problem in problems:
        topic = problem.topic
        if not topic:
            continue
        topics_stats[topic]['attempts']+= problem.attempts
        if problem.is_solved:
            topics_stats[topic]['solved'] += 1
    weak_topics = []
    strong_topics = []
    for topic,stats in topics_stats.items():
        accuracy = (
            stats['solved']/
            stats['attempts']
        )*100
        if accuracy < 50:
            weak_topics.append(topic)
        else:
            strong_topics.append(topic)
    recommendation = {
        'weak_topics': weak_topics,
        'strong_topics':strong_topics,
        "message":[]
    }
    if weak_topics:
        recommendation['message'].append(
            f"focus more on {weak_topics}"
        )
    if strong_topics:
        recommendation['message'].append(
            f"you are strong in {strong_topics}"
        )
    return recommendation