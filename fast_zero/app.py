from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from schemas import UserDB, UserList, UserReturn, Users

database = []
app = FastAPI()


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserReturn)
def create_user(user: Users):
    user_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_id)
    return user_id

@app.get('/users/{user_id}' , status_code=HTTPStatus.OK , response_model=UserReturn)
def return_unique_user(user_id: int):
    for dbUser in database:
        
        if user_id < 0 or user_id > len(database):
              raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, message='usuário não encontrado'
            )
    
        if dbUser.id == user_id:
                return dbUser
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, message='usuário não encontrado'
            )
        
    return {"user": dbUser}


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def return_users():
    return {'users': database}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserReturn
)
def update_users(user_id: int, user: Users):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete('/users/{user_id}', status_code=HTTPStatus.OK)
def deleted_users(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, message='Usuário não encontrado'
        )

    del database[user_id - 1]

    return {'message': 'Usuário Deletado com sucesso', 'status': 200}
