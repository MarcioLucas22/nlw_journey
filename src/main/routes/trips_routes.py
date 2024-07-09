from flask import jsonify, Blueprint #Blueprint ajuda a dar um bom nome para as rotas

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=['POST'])
def create_trip():
    return jsonify({'olá': 'mundo'}), 200