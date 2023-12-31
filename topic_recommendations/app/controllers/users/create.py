from topic_recommendations.app.controllers.base import Controller
from topic_recommendations.app.presenters.users import CreateUserPresenter
from topic_recommendations.interactor.interfaces.repositories.users import IUsersRepository
from topic_recommendations.interactor.use_cases.users.create_user import CreateUser


class CreateUserController(Controller):
    def __init__(self, presenter: CreateUserPresenter, repository: IUsersRepository):
        self._presenter = presenter
        self._repository = repository

    def execute(self, name: str, password: str):
        return CreateUser(self._presenter, self._repository).execute(name, password)
