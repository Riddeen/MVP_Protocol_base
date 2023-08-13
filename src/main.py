from models.model import Model
from views.view import View
from presenters.presenter import Presenter


def main() -> None:
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()


if __name__ == "__main__":
    main()