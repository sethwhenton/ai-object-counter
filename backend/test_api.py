"""
Test suite for backend API endpoints
"""
import pytest
import json
from unittest.mock import patch, MagicMock
from io import BytesIO

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] == 'healthy'

def test_test_pipeline_endpoint(client):
    """Test the test-pipeline endpoint"""
    response = client.get('/test-pipeline')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'status' in data

def test_count_objects_endpoint_missing_image(client):
    """Test count objects endpoint without image"""
    response = client.post('/api/count', data={})
    assert response.status_code == 400

def test_count_objects_endpoint_missing_object_type(client):
    """Test count objects endpoint without object type"""
    # Create a mock image file
    image_data = b'fake_image_data'
    image_file = (BytesIO(image_data), 'test.jpg')
    
    response = client.post('/api/count', 
                          data={'image': image_file},
                          content_type='multipart/form-data')
    assert response.status_code == 400

@patch('models.pipeline.AIPipeline')
def test_count_objects_endpoint_success(mock_pipeline_class, client):
    """Test successful count objects endpoint"""
    # Mock the pipeline
    mock_pipeline = MagicMock()
    mock_pipeline.count_objects.return_value = {
        'count': 3,
        'confidence': 0.92,
        'processing_time': 1.5,
        'segments': [],
        'metadata': {'model_version': 'test'}
    }
    mock_pipeline_class.return_value = mock_pipeline
    
    # Create a mock image file
    image_data = b'fake_image_data'
    image_file = (BytesIO(image_data), 'test.jpg')
    
    response = client.post('/api/count',
                          data={
                              'image': image_file,
                              'object_type': 'person'
                          },
                          content_type='multipart/form-data')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'count' in data
    assert data['count'] == 3

def test_correct_endpoint_missing_data(client):
    """Test correct endpoint without required data"""
    response = client.post('/api/correct', json={})
    assert response.status_code == 400

@patch('models.database.db')
def test_correct_endpoint_success(mock_db, client):
    """Test successful correct endpoint"""
    # Mock the database session
    mock_session = MagicMock()
    mock_db.session = mock_session
    
    response = client.post('/api/correct', 
                          json={
                              'input_id': 1,
                              'actual_count': 5,
                              'feedback': 'Great job!'
                          })
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data

def test_performance_endpoint(client):
    """Test the performance endpoint"""
    response = client.get('/api/performance')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'metrics' in data

def test_invalid_endpoint(client):
    """Test invalid endpoint returns 404"""
    response = client.get('/invalid-endpoint')
    assert response.status_code == 404

def test_cors_headers(client):
    """Test that CORS headers are present"""
    response = client.get('/health')
    assert 'Access-Control-Allow-Origin' in response.headers

if __name__ == '__main__':
    pytest.main([__file__])
