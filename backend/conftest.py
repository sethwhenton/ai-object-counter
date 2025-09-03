"""
Pytest configuration for backend tests
"""
import pytest
import os
import sys
from unittest.mock import Mock, patch

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def app():
    """Create a test Flask app instance"""
    from app import app as flask_app
    flask_app.config['TESTING'] = True
    flask_app.config['WTF_CSRF_ENABLED'] = False
    return flask_app

@pytest.fixture
def client(app):
    """Create a test client for the Flask app"""
    return app.test_client()

@pytest.fixture
def mock_pipeline():
    """Mock the AI pipeline to avoid loading heavy models during tests"""
    with patch('models.pipeline.AIPipeline') as mock:
        mock_instance = Mock()
        mock_instance.count_objects.return_value = {
            'count': 5,
            'confidence': 0.95,
            'processing_time': 1.2,
            'segments': [],
            'metadata': {'model_version': 'test'}
        }
        mock.return_value = mock_instance
        yield mock_instance

@pytest.fixture
def sample_image():
    """Create a sample image file for testing"""
    # Create a simple test image (1x1 pixel PNG)
    import io
    from PIL import Image
    
    # Create a minimal test image
    img = Image.new('RGB', (1, 1), color='red')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io
