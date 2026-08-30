# FitnessVision

## Project Overview

**FitnessVision** is a web-based AI fitness trainer designed to help users improve exercise form through computer vision.

The system will initially support **three exercises**. A camera will capture the user's movement, a pose-estimation model will extract body landmarks, and the system will analyze those landmarks to identify **specific exercise-form errors** and provide corrective feedback.

The project is intended as a practical prototype for exercise guidance rather than a replacement for a professional fitness trainer.

---

## Confirmed Project Scope

- **Project name:** FitnessVision
- **Platform:** Web application
- **Initial exercise count:** 3 exercises
- **Core technology:** Computer vision and deep learning for human pose estimation
- **Form-analysis approach:** Rule-based geometric analysis
- **Primary goal:** Identify specific exercise-form errors and provide corrective feedback
- **Repetition counting:** Included
- **Camera input:** Included

The exact three exercises have **not yet been finalized**.

---

## Proposed System Workflow

```text
Camera Input
     ↓
Pose Estimation
     ↓
Body Landmarks
     ↓
Feature Extraction
     ↓
Movement Analysis
     ↓
Geometric Error Detection
     ↓
Specific Form Error
     ↓
Corrective Feedback
     ↓
Web Interface
```

A separate repetition-counting component will operate during movement analysis.

---

## Core Approach

### 1. Pose Estimation

A pose-estimation model will be used to detect relevant human body landmarks from camera frames.

The exact pose-estimation model has **not yet been finalized**. Candidates discussed include:

- MediaPipe Pose / BlazePose
- MoveNet
- YOLO-Pose

The final choice will consider ease of learning and implementation, ability to train or fine-tune, real-time performance, landmark quality, documentation, and hardware suitability.

### 2. Geometric Analysis

The detected body landmarks will be converted into measurable movement features, potentially including:

- Joint angles
- Relative positions
- Distances or ratios
- Body alignment
- Range of motion
- Changes in measurements over time

These features will be used to determine whether a predefined form condition is being violated.

### 3. Rule-Based Error Identification

Instead of training a separate ML classifier to simply output `correct` or `incorrect`, FitnessVision will initially use **exercise-specific geometric rules** to identify the exact form error.

```text
Body Landmarks
      ↓
Geometric Features
      ↓
Exercise-Specific Rules
      ↓
Specific Error
      ↓
Corrective Feedback
```

The exact rules and thresholds have **not yet been finalized** and will be determined after selecting the exercises and studying the relevant movement characteristics.

### 4. Repetition Counting

The system will track movement through an exercise cycle and determine when a complete repetition has been performed.

The exact repetition-counting method has not yet been finalized.

---

## Research Methodology

The current methodology is organized into five stages.

### Stage 1 — Exercise & Scope Definition

- Select three exercises.
- Define correct form for each exercise.
- Identify common and detectable form errors.
- Determine relevant body movements and joints.
- Define criteria for a completed repetition.
- Define expected corrective feedback.

**Expected outcome:** A defined set of exercises, form errors, movement characteristics, and repetition criteria.

### Stage 2 — Data Collection & Preparation

- Obtain exercise movement samples representing correct and incorrect forms.
- Include multiple repetitions.
- Where possible, include variation between users and recording conditions.
- Extract relevant body landmarks.
- Organize data by exercise and form category.
- Prepare appropriate labels/ground truth for evaluation.

**Expected outcome:** Structured exercise movement data suitable for development and evaluation.

### Stage 3 — Pose & Movement Analysis

- Capture exercise movement through a camera.
- Detect body landmarks.
- Track relevant joints.
- Calculate angles and relative positions.
- Analyze how measurements change during movement.
- Identify movement patterns relevant to each exercise.

**Expected outcome:** Measurable movement features for form assessment and repetition counting.

### Stage 4 — Form Assessment & Repetition Counting

- Compare movement measurements against defined form criteria.
- Identify predefined form errors.
- Generate corresponding corrective feedback.
- Detect completed repetitions.
- Compare detected repetitions with actual repetitions during evaluation.

**Expected outcome:** Automatic form assessment, specific error identification, repetition counting, and corrective feedback.

### Stage 5 — System Evaluation

The prototype will be evaluated using appropriate measures such as:

- Form-error detection performance
- Repetition-counting accuracy
- Response time / real-time performance
- Robustness across users and conditions where possible
- Clarity and usefulness of corrective feedback

**Expected outcome:** Evidence of the system's accuracy, responsiveness, and practical usefulness.

---

## Proposed System Design

The current conceptual architecture is:

```text
                    User
                      │
                      ↓
                 Camera Input
                      │
                      ↓
                 Pose Estimation
                      │
                      ↓
                 Body Landmarks
                      │
                      ↓
                Feature Extraction
                      │
                      ↓
                Movement Analysis
                   /          \
                  ↓            ↓
          Form Assessment   Rep Counting
                  │            │
                  ↓            ↓
        Error Identification  Rep Count
                  │            │
                  └──────┬─────┘
                         ↓
                 Corrective Feedback
                         │
                         ↓
                    Web Interface
```

This is a **proposed design**, not a finalized implementation.

---

## Dataset Plan

The dataset strategy has **not yet been finalized**.

The project requires data that can support:

- The three selected exercises
- Correct exercise form
- Specific incorrect forms
- Multiple repetitions
- Variation between users where possible
- Evaluation of the geometric error-detection rules

Possible sources discussed include:

1. Public exercise/pose datasets
2. Self-collected exercise data
3. A combination of public and self-collected data

A previously discussed candidate was the **MM-Fit dataset**, but it has **not been officially selected** as the project dataset.

The dataset decision should be made after selecting the exercises, defining specific errors, determining required landmark/movement information, checking suitable public data, and determining whether self-collected samples are necessary.

---

## AI / ML Architecture Decision

One important decision currently made is that **specific form-error identification will be rule-based rather than handled by a second ML classifier**.

The current candidate architecture is:

```text
Pose Estimation Model
        ↓
Body Landmarks
        ↓
Geometric Feature Extraction
        ↓
Rule-Based Error Detection
        ↓
Specific Form Error
        ↓
Corrective Feedback
```

A second ML model for overall form classification is **not currently required**.

The pose-estimation model may be used as a pre-trained model, fine-tuned, or otherwise adapted depending on the final technical decision. This has **not yet been finalized**.

---

## Expected Features

The planned prototype is expected to provide:

- Camera-based exercise analysis
- Pose estimation
- Body-landmark tracking
- Exercise movement analysis
- Specific form-error identification
- Repetition counting
- Corrective feedback
- Web-based user interface

---

## Current Decisions vs. Open Decisions

### Confirmed

- Project name: **FitnessVision**
- Web-based system
- Three exercises initially
- Camera-based movement analysis
- Pose estimation
- Geometric feature analysis
- Rule-based specific error identification
- Corrective feedback
- Repetition counting
- System evaluation
- Three-person team

### Not Yet Finalized

- Exact three exercises
- Pose-estimation model
- Whether/how the pose model will be fine-tuned
- Dataset and final data source
- Exact form errors for each exercise
- Geometric features for each error
- Threshold-selection method
- Repetition-counting algorithm
- Web technology stack
- Final evaluation metrics
- Final UI design

---

## Research Direction

The main technical focus of FitnessVision is:

> **How can body landmarks obtained through pose estimation be converted into meaningful geometric measurements and exercise-specific rules that identify exact form errors and provide understandable corrective feedback?**

This keeps the project focused on **interpretable exercise-form analysis** rather than only classifying an exercise as correct or incorrect.

---

## Project Goal

The overall goal is to develop a web-based prototype that can observe selected exercises through a camera, analyze body movement, identify predefined form errors, count repetitions, and provide immediate corrective feedback.
