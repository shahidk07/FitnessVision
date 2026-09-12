# FitnessVision — Folder Structure

This document describes the high-level structure of the FitnessVision Django project.

## Structure

```text
FitnessVision/
├── config/
├── datasets/
├── documentation/
├── exercises/
├── main_app/
├── models/
├── pose_estimation/
├── posture_analysis/
├── static/
├── templates/
├── manage.py
├── README.md
└── requirements.txt
```

## Directories-Brief

| Directory | Purpose |
|---|---|
| `config/` | Django project configuration: settings, URLs, ASGI and WSGI. |
| `datasets/` | Datasets used for development, testing and analysis. |
| `documentation/` | Project and technical documentation. |
| `exercises/` | Exercise-specific logic and evaluation rules. |
| `main_app/` | Main Django application: views, models, migrations and admin. |
| `models/` | ML/CV model files and artifacts. |
| `pose_estimation/` | Human pose detection and body landmark extraction. |
| `posture_analysis/` | Posture analysis, error detection and feedback logic. |
| `static/` | CSS, JavaScript, images and other static files. |
| `templates/` | Django HTML templates for the user interface. |

## Important Files

- `manage.py` — Command-line utility for managing the Django project.
- `requirements.txt` — Python dependencies required by the project.
- `README.md` — Main project overview and setup documentation.

## Architecture

```text
Camera / Input
      ↓
pose_estimation/
      ↓
Body Landmarks
      ↓
posture_analysis/
      ↓
Exercise Evaluation
      ↓
Feedback
      ↓
Django UI
```

The project separates the Django web layer from pose estimation, exercise logic, and posture analysis to keep the system organized and maintainable.







## Directory Details

### `config/`
Django project configuration.

Contains:
- `settings.py` — Django settings, installed apps, middleware, database, templates and static-file configuration.
- `urls.py` — Main URL routing.
- `asgi.py` / `wsgi.py` — Deployment entry points.
- `__init__.py` — Python package marker.

This directory should contain project-level configuration, not exercise or computer-vision logic.

### `main_app/`
Main Django application and web-layer logic.

Typical responsibilities:
- Handling HTTP requests and responses.
- Connecting URLs to views.
- Database models for users, workout sessions, exercise results, etc.
- Django forms and validation.
- Admin configuration.
- Application-level tests.

Typical functions may include:
- `home()` — Render the home page.
- `workout()` — Start or display a workout session.
- `results()` — Display workout results.
- Helper functions for handling requests or preparing data for templates.

### `pose_estimation/`
Human pose-estimation functionality.

Responsible for converting camera/video frames into body landmarks.

Typical utilities/functions:
- Initialize the pose-estimation model.
- Process an image or video frame.
- Extract body landmarks.
- Return landmark coordinates and visibility/confidence values.
- Draw landmarks/skeleton on frames.
- Convert or normalize landmark data.

Example responsibilities:

```text
Frame
  ↓
detect_pose()
  ↓
33 landmarks
  ↓
extract_landmarks()
```

### `exercises/`
Exercise-specific definitions and logic.

Each exercise can have its own module, for example:

```text
exercises/
├── squat.py
├── pushup.py
└── utils.py
```

Typical functions:
- `analyze_squat()` — Evaluate squat-specific conditions.
- `check_depth()` — Check whether sufficient squat depth is reached.
- `check_knee_alignment()` — Check knee alignment.
- `check_torso_angle()` — Check torso position.
- Exercise-specific repetition-state logic.

`utils.py` can contain reusable exercise utilities shared by multiple exercises.

### `posture_analysis/`
General posture-analysis and feedback logic.

This layer works with landmarks/features produced by `pose_estimation` and exercise-specific information from `exercises`.

Typical modules/functions may include:

```text
posture_analysis/
├── angles.py
├── posture.py
├── feedback.py
└── utils.py
```

Possible responsibilities:

- Calculate joint angles.
- Calculate distances and relative positions.
- Check body alignment.
- Apply posture rules.
- Identify specific form errors.
- Generate corrective feedback.

Examples:

- `calculate_angle()` — Calculate the angle between three landmarks.
- `calculate_distance()` — Calculate distance between two landmarks.
- `check_alignment()` — Evaluate alignment between body landmarks.
- `detect_errors()` — Identify posture violations.
- `generate_feedback()` — Convert detected errors into user-friendly feedback.

### `models/`
Stores machine-learning/computer-vision model files and other model artifacts.

Examples:

```text
models/
├── pose_landmarker.task
└── posture_classifier.pkl
```

This directory is for model files, not Python model classes. Django database models belong in `main_app/models.py`.

### `datasets/`
Stores project datasets.

Possible contents:

```text
datasets/
├── raw/
└── processed/
```

Examples:
- Raw exercise videos/images.
- Landmark data.
- Processed CSV files.
- Training/validation/test data.

Large datasets should generally not be committed to Git unless required.

### `templates/`
Contains Django HTML templates.

Possible structure:

```text
templates/
├── base.html
└── main_app/
    ├── home.html
    ├── workout.html
    └── results.html
```

Templates are responsible for the presentation layer of the web application.

### `static/`
Contains frontend static assets.

Possible structure:

```text
static/
├── css/
├── js/
└── images/
```

Typical contents:
- CSS stylesheets.
- JavaScript files.
- Images/icons.
- Other frontend assets.

### `documentation/`
Contains project documentation.

Examples:
- `FOLDER_STRUCTURE.md`
- `SRS.md`
- System design documents.
- Research/literature review.
- API or implementation documentation.
- Testing documentation.

### `manage.py`
Django's command-line utility.

Common commands:

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### `requirements.txt`
Lists Python dependencies required by the project.

Example:

```text
Django
mediapipe
opencv-python
numpy
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

### `README.md`
The main project documentation containing the project overview, setup instructions, features, technologies and usage information.

---

## Separation of Responsibilities

The main processing pipeline is:

```text
Camera / Video
      ↓
pose_estimation/
      ↓
Body Landmarks
      ↓
posture_analysis/
      ↓
Geometric Features
      ↓
exercises/
      ↓
Exercise Rules & Error Detection
      ↓
Feedback
      ↓
main_app/
      ↓
Django Web Interface
```

### Utility Principle

Reusable mathematical or processing operations should be placed in utility modules rather than duplicated across files.

For example:

```text
calculate_angle()
calculate_distance()
normalize_landmarks()
check_visibility()
```

can be reused by multiple exercises.

Exercise-specific rules should remain inside the relevant exercise module, while general-purpose utilities should remain reusable and independent of a particular exercise.
