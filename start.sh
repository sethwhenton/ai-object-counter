#!/bin/sh

# Start script for AI Object Counter Docker container

echo "🚀 Starting AI Object Counter..."

# Start backend in background
echo "🐍 Starting Python backend..."
cd /app/backend
python3 app.py &

# Wait for backend to start
echo "⏳ Waiting for backend to start..."
sleep 10

# Check if backend is running
if curl -f http://localhost:5000/health > /dev/null 2>&1; then
    echo "✅ Backend is running on port 5000"
else
    echo "❌ Backend failed to start"
    exit 1
fi

# Start nginx
echo "🌐 Starting nginx..."
nginx -g "daemon off;"
