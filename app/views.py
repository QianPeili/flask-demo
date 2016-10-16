from flask import Blueprint

main = Blueprint(
    'main', __name__,
)


@main.route('/index', methods=['GET'])
@main.route('/', methods=['GET'])
def index():
    return "hello!"