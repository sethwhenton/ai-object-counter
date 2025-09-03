# 🤖 AI Object Counting Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com)
[![React](https://img.shields.io/badge/React-18.3.1-blue.svg)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.6.3-blue.svg)](https://typescriptlang.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.6.0+-red.svg)](https://pytorch.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Advanced AI-powered application that counts objects in images using a sophisticated 3-step machine learning pipeline with real-time performance monitoring and user feedback system.**

## 🌟 Features

### 🧠 **AI Pipeline**
- **Segmentation**: SAM (Segment Anything Model) for precise image segmentation
- **Classification**: ResNet-50 for accurate object identification
- **Mapping**: DistilBERT for intelligent label mapping and zero-shot learning
- **GPU Acceleration**: CUDA support with automatic CPU fallback

### 📊 **Smart Analytics**
- **F1 Score Metrics**: Precision and recall balanced accuracy measurement
- **Performance Monitoring**: Real-time CPU, GPU, and memory tracking
- **User Feedback System**: Correct AI predictions and improve accuracy over time
- **Historical Analysis**: Track performance trends and model improvements

### 🎨 **Modern UI/UX**
- **Drag & Drop**: Intuitive image upload interface
- **Real-time Processing**: Live progress indicators and status updates
- **Responsive Design**: Beautiful, mobile-friendly interface built with React + Tailwind
- **Interactive Results**: Clickable history items with detailed analysis views

### 🗄️ **Data Management**
- **SQLite/MySQL Support**: Flexible database options for development and production
- **Bulk Operations**: Delete multiple results with confirmation dialogs
- **Image Storage**: Secure file handling with UUID-based naming
- **Cascade Cleanup**: Automatic cleanup of related data

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   AI Pipeline   │
│   (React/TS)    │◄──►│   (Flask)       │◄──►│   (PyTorch)     │
│                 │    │                 │    │                 │
│ • Image Upload  │    │ • REST API      │    │ • SAM Model     │
│ • Results View  │    │ • Database      │    │ • ResNet-50     │
│ • Performance   │    │ • File Storage  │    │ • DistilBERT    │
│ • History       │    │ • Monitoring    │    │ • GPU Support   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+
- Node.js 18+
- Git

### **1. Clone the Repository**
```bash
git clone https://github.com/sethwhenton/ai-object-counter.git
cd ai-object-counter
```

### **2. Backend Setup**
```bash
cd backend

# Install dependencies
py -m pip install -r requirements.txt

# Initialize database
py init_db.py

# Start the API server
py app.py
```

**Wait for:** `✅ AI Pipeline initialized successfully!`

### **3. Frontend Setup**
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### **4. Test the System**
1. **Backend**: http://localhost:5000/health
2. **Frontend**: http://localhost:3000
3. **Upload an image** and select an object type
4. **Watch the AI magic happen!** ✨

## 📱 Supported Object Types

| Object | Description | Example Use Cases |
|--------|-------------|-------------------|
| 🚗 **Car** | Automobiles and vehicles | Traffic analysis, parking management |
| 🐱 **Cat** | Domestic cats | Pet detection, animal counting |
| 🌳 **Tree** | Trees and large plants | Forest inventory, urban planning |
| 🐕 **Dog** | Dogs and canines | Pet detection, security systems |
| 🏢 **Building** | Buildings and structures | Construction monitoring, city planning |
| 👤 **Person** | People and humans | Crowd counting, security analysis |
| ☁️ **Sky** | Sky and atmospheric elements | Weather analysis, time-of-day detection |
| 🌍 **Ground** | Ground and terrain | Land use analysis, agriculture |
| 🔧 **Hardware** | Tools and hardware items | Inventory management, quality control |

## 🔧 API Endpoints

### **Health Check**
```http
GET /health
```
Returns API status and pipeline availability

### **Test Pipeline**
```http
POST /test-pipeline
Content-Type: multipart/form-data

{
  "image": <file>,
  "object_type": "car"
}
```

### **Count Objects**
```http
POST /api/count
Content-Type: multipart/form-data

{
  "image": <file>,
  "object_type": "person"
}
```

### **Submit Correction**
```http
POST /api/correct
Content-Type: application/json

{
  "result_id": 123,
  "corrected_count": 5
}
```

### **Performance Metrics**
```http
GET /api/performance
```
Returns real-time system performance data

## 🛠️ Technology Stack

### **Backend**
- **Framework**: Flask 3.0.0
- **AI/ML**: PyTorch, Transformers, SAM
- **Database**: SQLAlchemy, SQLite/MySQL
- **Monitoring**: Custom performance tracking
- **File Handling**: Secure upload with UUID naming

### **Frontend**
- **Framework**: React 18.3.1 + TypeScript 5.6.3
- **Styling**: Tailwind CSS + Radix UI components
- **State Management**: React Hooks
- **Build Tool**: Vite 6.3.5
- **Charts**: Recharts for data visualization

### **AI Models**
- **Segmentation**: Meta's Segment Anything Model (SAM)
- **Classification**: ResNet-50 for image classification
- **NLP**: DistilBERT for zero-shot label mapping
- **Hardware**: CUDA GPU acceleration with CPU fallback

## 📊 Performance Features

### **Real-time Monitoring**
- **CPU Usage**: Live CPU utilization tracking
- **GPU Metrics**: Memory, temperature, clock speeds
- **Memory Usage**: RAM consumption monitoring
- **Processing Speed**: Time per image analysis

### **Accuracy Metrics**
- **F1 Score**: Balanced precision and recall
- **User Feedback**: Continuous model improvement
- **Historical Trends**: Performance over time
- **Object-specific Stats**: Per-category accuracy

## 🎯 Use Cases

### **🔄 Development & Testing**
- **Machine Learning Research**: Test segmentation and classification models
- **Computer Vision Projects**: Benchmark object detection accuracy
- **API Development**: Learn Flask REST API patterns
- **Frontend Integration**: React + TypeScript best practices

### **🏢 Production Applications**
- **Security Systems**: Count people in surveillance footage
- **Traffic Analysis**: Monitor vehicle counts on roads
- **Retail Analytics**: Track customer flow in stores
- **Agricultural Monitoring**: Count crops or livestock
- **Construction Sites**: Monitor worker and equipment counts

## 🔍 Project Structure

```
ai-object-counter/
├── 📁 backend/                 # Flask API server
│   ├── 🐍 app.py              # Main Flask application
│   ├── 🗄️ models/            # Database models & AI pipeline
│   ├── 📊 performance_monitor.py  # System monitoring
│   ├── 🧪 test_*.py          # Test scripts
│   └── 📋 requirements.txt    # Python dependencies
├── 📁 frontend/               # React TypeScript app
│   ├── ⚛️ src/components/    # React components
│   ├── 🎨 src/styles/        # CSS and styling
│   ├── 🔌 src/services/      # API integration
│   └── 📦 package.json       # Node.js dependencies
├── 📁 model_pipeline/         # Jupyter notebooks
├── 📋 README.md               # This file
├── 📋 IMPLEMENTATION_ROADMAP.md  # Development roadmap
└── 🚫 .gitignore             # Git ignore rules
```

## 🧪 Testing

### **Backend Tests**
```bash
cd backend
py test_pipeline.py      # Test AI pipeline
py test_api_endpoints.py # Test API endpoints
py test_app.py          # Test Flask app
```

### **Frontend Tests**
```bash
cd frontend
npm run type-check      # TypeScript validation
npm run build          # Build verification
```

## 🚀 Deployment

### **Development**
```bash
# Backend
cd backend && py app.py

# Frontend  
cd frontend && npm run dev
```

### **Production**
```bash
# Backend
cd backend
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Frontend
cd frontend
npm run build
# Serve dist/ folder with nginx/apache
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### **Development Setup**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📈 Roadmap

- [x] **Core AI Pipeline** - SAM + ResNet + DistilBERT
- [x] **Flask API** - RESTful endpoints with database
- [x] **React Frontend** - Modern UI with real-time updates
- [x] **Performance Monitoring** - Live system metrics
- [x] **User Feedback System** - Correction and improvement
- [ ] **Multi-language Support** - Internationalization
- [ ] **Mobile App** - React Native version
- [ ] **Cloud Deployment** - AWS/Azure integration
- [ ] **Advanced Analytics** - Machine learning insights

## 🐛 Troubleshooting

### **Common Issues**

**"AI Pipeline not available"**
```bash
cd backend
py -m pip install torch torchvision transformers
```

**"Cannot find module 'react'"**
```bash
cd frontend
npm install --force
```

**"CORS error"**
- Ensure backend is running on port 5000
- Check CORS configuration in `app.py`

**"GPU not detected"**
- Install CUDA toolkit if available
- Application will automatically fall back to CPU

### **Performance Tips**
- **First Run**: Models download automatically (~2GB)
- **GPU Usage**: Enable CUDA for 5-10x speed improvement
- **Memory**: Close other applications for optimal performance
- **Batch Processing**: Process multiple images simultaneously

## 📚 Documentation

- [API Documentation](backend/API_DOCUMENTATION.md)
- [Installation Steps](backend/INSTALL_STEPS.md)
- [Frontend Integration](frontend/INTEGRATION_GUIDE.md)
- [Implementation Roadmap](IMPLEMENTATION_ROADMAP.md)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Meta AI** for the Segment Anything Model (SAM)
- **Hugging Face** for Transformers library
- **PyTorch Team** for the deep learning framework
- **React Team** for the frontend framework
- **Tailwind CSS** for the styling system

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/sethwhenton/ai-object-counter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sethwhenton/ai-object-counter/discussions)
- **Wiki**: [Project Wiki](https://github.com/sethwhenton/ai-object-counter/wiki)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

**🤖 Built with AI, for AI enthusiasts**

[![GitHub stars](https://img.shields.io/github/stars/sethwhenton/ai-object-counter?style=social)](https://github.com/sethwhenton/ai-object-counter)
[![GitHub forks](https://img.shields.io/github/forks/sethwhenton/ai-object-counter?style=social)](https://github.com/sethwhenton/ai-object-counter)
[![GitHub issues](https://img.shields.io/github/issues/sethwhenton/ai-object-counter)](https://github.com/sethwhenton/ai-object-counter/issues)

</div>
