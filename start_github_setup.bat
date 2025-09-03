@echo off
echo 🚀 AI Object Counter - GitHub Setup Script
echo ===========================================
echo.

echo 📋 This script will help you set up your GitHub repository
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed. Please install Git first:
    echo    https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git is installed
echo.

REM Check if we're in the right directory
if not exist "backend\app.py" (
    echo ❌ Please run this script from the project root directory
    echo    (where backend\ and frontend\ folders are located)
    pause
    exit /b 1
)

echo ✅ Project structure verified
echo.

REM Get GitHub username
set /p GITHUB_USERNAME="Enter your GitHub username: "
if "%GITHUB_USERNAME%"=="" (
    echo ❌ Username cannot be empty
    pause
    exit /b 1
)

echo.

REM Update README with username
echo 🔄 Updating README.md with your username...
powershell -Command "(Get-Content README.md) -replace 'yourusername', '%GITHUB_USERNAME%' | Set-Content README.md"
if %errorlevel% neq 0 (
    echo ❌ Failed to update README.md
    pause
    exit /b 1
)

echo ✅ README.md updated
echo.

REM Initialize Git repository if not already done
if not exist ".git" (
    echo 🔄 Initializing Git repository...
    git init
    git remote add origin https://github.com/%GITHUB_USERNAME%/ai-object-counter.git
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)

echo.

REM Stage all files
echo 🔄 Staging all files...
git add .
if %errorlevel% neq 0 (
    echo ❌ Failed to stage files
    pause
    exit /b 1
)

echo ✅ Files staged
echo.

REM Create initial commit
echo 🔄 Creating initial commit...
git commit -m "🚀 Initial commit: AI Object Counter application

✨ Features:
- Advanced AI pipeline with SAM, ResNet-50, and DistilBERT
- Flask backend with RESTful API
- React TypeScript frontend with modern UI
- Real-time performance monitoring
- User feedback system with F1 score metrics
- Comprehensive documentation and setup guides
- Docker containerization and CI/CD pipeline

🔧 Tech Stack:
- Backend: Flask, PyTorch, SQLAlchemy
- Frontend: React 18, TypeScript, Tailwind CSS
- AI/ML: SAM, ResNet-50, DistilBERT
- DevOps: Docker, GitHub Actions, Nginx

📚 Documentation:
- Complete README with setup instructions
- Contributing guidelines
- API documentation
- Implementation roadmap"

if %errorlevel% neq 0 (
    echo ❌ Failed to create commit
    pause
    exit /b 1
)

echo ✅ Initial commit created
echo.

REM Push to GitHub
echo 🔄 Pushing to GitHub...
git branch -M main
git push -u origin main

if %errorlevel% neq 0 (
    echo.
    echo ❌ Failed to push to GitHub. This usually means:
    echo    1. The repository doesn't exist on GitHub yet
    echo    2. You need to create it first at: https://github.com/new
    echo    3. Repository name should be: ai-object-counter
    echo.
    echo 📋 Next steps:
    echo    1. Go to https://github.com/new
    echo    2. Create repository named: ai-object-counter
    echo    3. Make it Public
    echo    4. Don't initialize with README (we already have one)
    echo    5. Run this script again
    echo.
    pause
    exit /b 1
)

echo.
echo 🎉 SUCCESS! Your AI Object Counter project is now on GitHub!
echo.
echo 📋 Next steps:
echo    1. Visit: https://github.com/%GITHUB_USERNAME%/ai-object-counter
echo    2. Check the Actions tab to see CI/CD pipeline running
echo    3. Review and customize repository settings
echo    4. Share your project with the community!
echo.
echo 📚 For complete setup instructions, see: GITHUB_SETUP_GUIDE.md
echo.

pause
