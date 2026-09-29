const video = document.getElementById("camera");

const startButton = document.getElementById("startButton");
const stopButton = document.getElementById("stopButton");

const placeholder = document.getElementById("cameraPlaceholder");

const status = document.getElementById("connectionStatus");

let cameraStream = null;


// =============================
// START CAMERA
// =============================

startButton.addEventListener("click", async () => {

    try {

        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        });

        // Give the camera stream to the video element
        video.srcObject = cameraStream;

        // Show video
        video.style.display = "block";

        // Hide placeholder
        placeholder.style.display = "none";

        // Update buttons
        startButton.disabled = true;
        stopButton.disabled = false;

        // Update status
        status.textContent = "Camera Active";

    } catch (error) {

        console.error("Camera error:", error);

        status.textContent = "Camera Error";

        alert(
            "Could not access the camera. Please allow camera permission."
        );

    }

});


// =============================
// STOP CAMERA
// =============================

stopButton.addEventListener("click", () => {

    if (cameraStream) {

        cameraStream.getTracks().forEach(track => {
            track.stop();
        });

        cameraStream = null;
    }

    video.srcObject = null;

    video.style.display = "none";

    placeholder.style.display = "flex";

    startButton.disabled = false;
    stopButton.disabled = true;

    status.textContent = "Ready";

});