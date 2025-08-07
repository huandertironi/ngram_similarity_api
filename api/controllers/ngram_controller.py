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

    @ngram_blueprint.route("/", methods=["HEAD"])
    def head():
        return "", 200

    @ngram_blueprint.route('/', methods=["GET"])
    @cross_origin()
    def get():

        WORD = request.args.get("word", "")

        N = int(request.args.get("n", 2))

        result = ngram_service.get_top_5(WORD, N)

        return jsonify(result), 201
        