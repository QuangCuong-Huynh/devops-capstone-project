"""
Error Handler Test Suite
"""
import os
import logging
from unittest import TestCase
from flask import abort
from service import app
from service.models import init_db, DataValidationError
from service.common import status  # HTTP Status Codes


DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)

######################################################################
# Helper routes to trigger error handlers
######################################################################
@app.route("/cause_400")
def cause_400():
    abort(status.HTTP_400_BAD_REQUEST, description="Bad data input")


@app.route("/cause_404")
def cause_404():
    abort(status.HTTP_404_NOT_FOUND, description="Resource missing")


@app.route("/cause_405", methods=["POST"])
def cause_405():
    # Only POST allowed — will cause 405 if GET used
    return "OK", status.HTTP_200_OK


@app.route("/cause_415")
def cause_415():
    abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, description="Unsupported type")


@app.route("/cause_500")
def cause_500():
    raise Exception("Simulated server error")


@app.route("/cause_datavalidation")
def cause_datavalidation():
    raise DataValidationError("Invalid data format")


######################################################################
# Test Suite for Error Handlers
######################################################################
class TestErrorHandlers(TestCase):
    """Test all error handlers defined in service/error_handlers.py"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        init_db(app)

    def setUp(self):
        """Run before each test"""
        self.client = app.test_client()

    def tearDown(self):
        """Run after each test"""
        pass  # no DB interaction needed here

    ##################################################################
    # Individual tests
    ##################################################################
    def test_bad_request_handler(self):
        """Should return 400 Bad Request JSON"""
        resp = self.client.get("/cause_400")
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
        data = resp.get_json()
        assert data["status"] == status.HTTP_400_BAD_REQUEST
        assert data["error"] == "Bad Request"
        assert "Bad data input" in data["message"]

    def test_not_found_handler(self):
        """Should return 404 Not Found JSON"""
        resp = self.client.get("/cause_404")
        assert resp.status_code == status.HTTP_404_NOT_FOUND
        data = resp.get_json()
        assert data["status"] == status.HTTP_404_NOT_FOUND
        assert data["error"] == "Not Found"
        assert "Resource missing" in data["message"]

    def test_method_not_supported_handler(self):
        """Should return 405 Method Not Allowed"""
        resp = self.client.get("/cause_405")  # GET not allowed
        assert resp.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        data = resp.get_json()
        assert data["status"] == status.HTTP_405_METHOD_NOT_ALLOWED
        assert data["error"] == "Method not Allowed"

    def test_mediatype_not_supported_handler(self):
        """Should return 415 Unsupported Media Type"""
        resp = self.client.get("/cause_415")
        assert resp.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        data = resp.get_json()
        assert data["status"] == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        assert data["error"] == "Unsupported media type"

    def test_internal_server_error_handler(self):
        """Should return 500 Internal Server Error"""
        resp = self.client.get("/cause_500")
        assert resp.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        data = resp.get_json()
        assert "error" in data
        assert data["error"] in ("Simulated server error", "Internal Server Error")

    def test_datavalidation_error_handler(self):
        """Should handle DataValidationError as 400 Bad Request"""
        resp = self.client.get("/cause_datavalidation")
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
        data = resp.get_json()
        assert data["status"] == status.HTTP_400_BAD_REQUEST
        assert data["error"] == "Bad Request"
        assert "Invalid data format" in data["message"]
