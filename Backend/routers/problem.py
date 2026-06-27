from fastapi import APIRouter,Depends 
from sqlalchemy.orm import Session 
from core.dependencies import get_db,get_current_user
from schemas.problem_schema import ProblemCreate,ProblemUpdate
from services.problem_service import delete_problem, update_problem
from services.problem_service import create_problem,get_user_problems
router = APIRouter(
    prefix='/problems',
    tags = ['Problems']
)
@router.post('/add')
def add_problem(
    problem:ProblemCreate,
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user) #automatically reads JWT tokens,Verifies token, finds logged-in user
):
    return create_problem(
        db,
        problem,
        current_user
    )
@router.get('/my-problem')
def my_problems(
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_user_problems(
        db,
        current_user
    )
@router.put('/{problem_id}')
def update_user_problem(
    problem_id: int,
    problem_data : ProblemUpdate,
    db:Session= Depends(get_db),
    current_user = Depends(get_current_user)

):
    return update_problem(
        db,
        problem_id,
        problem_data,
        current_user
    )
@router.delete("/{problem_is}")
def delete_user_problem(
    problem_id:int,
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return delete_problem(
        db,
        problem_id,
        current_user
    )