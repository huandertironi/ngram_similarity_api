from flask import Blueprint, request, jsonify, Response, stream_with_context
from flask_cors import cross_origin
import jsonpickle
import logging
import json

from application.services import ngram_service

ngram_blueprint = Blueprint("ngram", __name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ngram_service = ngram_service.NGramService()

class NGramController:

    @ngram_blueprint.route('/', methods=["GET"])
    @cross_origin()
    def get():

        WORD = request.args.get("word")

        n_param = request.args.get("n")
        if n_param is None:
            return jsonify({"error": "Missing 'n' parameter"}), 400

        try:
            N = int(n_param)
        except ValueError:
            return jsonify({"error": "'n' must be an integer"}), 400

        result = ngram_service.get_top_5(WORD, N)

        return jsonify(result), 201
        