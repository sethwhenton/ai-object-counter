# 🤝 Contributing to AI Object Counter

Thank you for your interest in contributing to the AI Object Counter project! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### **Prerequisites**
- Python 3.8+
- Node.js 18+
- Git
- Basic knowledge of Flask, React, and machine learning concepts

### **Development Setup**
1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/sethwhenton/ai-object-counter.git
   cd ai-object-counter
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/original-owner/ai-object-counter.git
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🔧 Development Workflow

### **1. Backend Development (Python/Flask)**
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### **2. Frontend Development (React/TypeScript)**
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Type checking
npm run type-check

# Build verification
npm run build
```

### **3. Testing**
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm run test
```

## 📝 Code Style Guidelines

### **Python (Backend)**
- **PEP 8** compliance
- **Type hints** for function parameters and return values
- **Docstrings** for all functions and classes
- **Maximum line length**: 88 characters (Black formatter)

```python
def count_objects(image_file: FileStorage, object_type: str) -> Dict[str, Any]:
    """
    Count objects in an image using the AI pipeline.
    
    Args:
        image_file: Uploaded image file
        object_type: Type of object to count
        
    Returns:
        Dictionary containing count results and metadata
        
    Raises:
        ValueError: If image file is invalid
        RuntimeError: If AI pipeline fails
    """
    # Implementation here
    pass
```

### **TypeScript (Frontend)**
- **ESLint** and **Prettier** configuration
- **Strict TypeScript** mode
- **Functional components** with hooks
- **Proper error handling** and loading states

```typescript
interface ImageUploadProps {
  onUpload: (file: File) => void;
  acceptedTypes?: string[];
  maxSize?: number;
}

export const ImageUpload: React.FC<ImageUploadProps> = ({
  onUpload,
  acceptedTypes = ['image/*'],
  maxSize = 10 * 1024 * 1024 // 10MB
}) => {
  // Implementation here
};
```

### **General Guidelines**
- **Meaningful commit messages** following conventional commits
- **Small, focused commits** that are easy to review
- **Comprehensive testing** for new features
- **Documentation updates** for API changes

## 🧪 Testing Requirements

### **Backend Testing**
- **Unit tests** for all new functions
- **Integration tests** for API endpoints
- **Test coverage** should be >80%
- **Mock external dependencies** (AI models, databases)

```python
def test_count_objects_endpoint():
    """Test the /api/count endpoint with valid image."""
    with app.test_client() as client:
        # Test implementation
        pass
```

### **Frontend Testing**
- **Component testing** with React Testing Library
- **Integration tests** for user workflows
- **Accessibility testing** for UI components
- **Cross-browser compatibility** testing

```typescript
test('should upload image and show results', async () => {
  // Test implementation
});
```

## 📚 Documentation Standards

### **Code Documentation**
- **Inline comments** for complex logic
- **API documentation** for all endpoints
- **README updates** for new features
- **Code examples** in docstrings

### **User Documentation**
- **Installation instructions** for new features
- **Configuration options** and environment variables
- **Troubleshooting guides** for common issues
- **Screenshots and demos** for UI features

## 🔄 Pull Request Process

### **1. Before Submitting**
- [ ] **Code follows** style guidelines
- [ ] **Tests pass** locally
- [ ] **Documentation updated** for new features
- [ ] **No console.log** or debug code left in
- [ ] **Performance impact** considered for large changes

### **2. Pull Request Template**
```markdown
## 📝 Description
Brief description of changes and why they're needed.

## 🔧 Changes Made
- [ ] Feature A added
- [ ] Bug B fixed
- [ ] Performance C improved

## 🧪 Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## 📚 Documentation
- [ ] README updated
- [ ] API docs updated
- [ ] Code comments added

## 🚀 Performance Impact
Describe any performance implications of these changes.

## 📸 Screenshots (if applicable)
Add screenshots for UI changes.
```

### **3. Review Process**
- **Code review** by maintainers
- **Automated checks** (CI/CD pipeline)
- **Address feedback** promptly
- **Squash commits** before merging

## 🐛 Bug Reports

### **Bug Report Template**
```markdown
## 🐛 Bug Description
Clear description of what the bug is.

## 🔄 Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## ✅ Expected Behavior
What you expected to happen.

## ❌ Actual Behavior
What actually happened.

## 🖥️ Environment
- OS: [e.g. Windows 10, macOS 12]
- Browser: [e.g. Chrome 120, Firefox 119]
- Python: [e.g. 3.9.7]
- Node.js: [e.g. 18.17.0]

## 📸 Screenshots
Add screenshots if applicable.

## 📋 Additional Context
Any other context about the problem.
```

## 💡 Feature Requests

### **Feature Request Template**
```markdown
## 🚀 Feature Description
Clear description of the feature you'd like to see.

## 🎯 Use Case
Explain why this feature would be useful.

## 💭 Proposed Implementation
Any ideas you have for how this could be implemented.

## 🔄 Alternatives Considered
Other solutions you've considered.

## 📸 Mockups/Screenshots
Visual examples if applicable.
```

## 🏷️ Issue Labels

We use the following labels to categorize issues:

- **🐛 bug**: Something isn't working
- **🚀 enhancement**: New feature or request
- **📚 documentation**: Improvements or additions to documentation
- **🧪 testing**: Adding or improving tests
- **🔧 maintenance**: Code maintenance tasks
- **🚨 security**: Security-related issues
- **⚡ performance**: Performance improvements
- **🎨 ui/ux**: User interface and experience improvements
- **🌐 internationalization**: Multi-language support
- **📱 mobile**: Mobile-specific features or fixes

## 🤝 Community Guidelines

### **Code of Conduct**
- **Be respectful** and inclusive
- **Help newcomers** learn and contribute
- **Constructive feedback** on code and ideas
- **No personal attacks** or harassment

### **Communication Channels**
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code contributions and reviews

## 🎯 Contribution Areas

### **High Priority**
- **Performance optimization** for AI pipeline
- **Error handling** improvements
- **Testing coverage** expansion
- **Documentation** updates

### **Medium Priority**
- **UI/UX improvements** and accessibility
- **New object types** support
- **API enhancements** and new endpoints
- **Mobile responsiveness** improvements

### **Low Priority**
- **Code refactoring** and cleanup
- **Additional language** support
- **Advanced analytics** features
- **Integration** with other services

## 🏆 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub profile** contribution graph
- **Project documentation** acknowledgments

## 📞 Getting Help

If you need help with contributing:

1. **Check existing issues** for similar problems
2. **Read the documentation** and README files
3. **Ask questions** in GitHub Discussions
4. **Join our community** channels

## 🎉 Thank You!

Thank you for contributing to the AI Object Counter project! Your contributions help make this tool better for everyone in the AI and computer vision community.

---

**Happy coding! 🚀🤖**
