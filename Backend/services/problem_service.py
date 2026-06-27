
from sqlalchemy.orm import Session
from models.problem import Problem
from fastapi import HTTPException
from schemas.problem_schema import ProblemCreate


def create_problem(
        db: Session,
        problem: ProblemCreate,
        current_user
):

    new_problem = Problem(
        title=problem.title,
        difficulty=problem.difficulty,
        topic=problem.topic,
        time_spend=problem.time_spend,
        notes=problem.notes,
        user_id=current_user.id
    )

    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)

    return {
        "message": "Problem added successfully",
        "problem": new_problem
    }


def get_user_problems(db, current_user):

    problems = db.query(Problem).filter(
        Problem.user_id == current_user.id
    ).all()

    return problems


def update_problem(
        db,
        problem_id,
        problem_data,
        current_user
):

    problem = db.query(Problem).filter(
        Problem.id == problem_id,
        Problem.user_id == current_user.id
    ).first()

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found"
        )

    update_data = problem_data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(problem, key, value)

    db.commit()
    db.refresh(problem)

    return problem


def delete_problem(
        db,
        problem_id,
        current_user
):

    problem = db.query(Problem).filter(
        Problem.id == problem_id,
        Problem.user_id == current_user.id
    ).first()

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found"
        )

    db.delete(problem)
    db.commit()

    return {
        "message": "Problem deleted successfully"
    }
