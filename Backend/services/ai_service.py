from collections import defaultdict
def generate_ai_recommendantion(
        problems
):
    topics_stats = defaultdict(
        lambda:{
            "solved":0,
            "attempts":0,
            "time_spend":0
        }
    )
    for problem in problems:
        topic = problem.topic
        if not topic:
            continue
        topics_stats[topic]['attempts']+= problem.attempts
        topics_stats[topic]['time_spend']+=problem.time_spend
        if problem.is_solved:
            topics_stats[topic]['solved'] += 1
    weak_topics = []
    strong_topics = []
    slow_topics = []
    message = []
    for topic,stats in topics_stats.items():
        if stats['attempts'] == 0:
            continue
        accuracy = (
            stats['solved']/
            stats['attempts']
        )*100
        avg_time =(
            stats['time_spend']/stats['attempts']
        )
        if accuracy < 50:
            weak_topics.append(topic)
        else:
            strong_topics.append(topic)
        if avg_time>40:
            slow_topics.append(topic)
    recommendation = {
        'weak_topics': weak_topics,
        'strong_topics':strong_topics,
        'slow_topics':slow_topics,
        "message":[]
    }
    if weak_topics:
        recommendation['message'].append(
            f"focus more on {','.join(weak_topics)}"
        )
    if strong_topics:
        recommendation['message'].append(
            f"you are strong in {','.join(strong_topics)}"
        )
    if slow_topics:
        recommendation['message'].append(
            f"You spend too much time on {','.join(slow_topics)}"
        )
    if not recommendation['message']:
        recommendation['message'].append(
            "You are doing great"
        )
    return recommendation