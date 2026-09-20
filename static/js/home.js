const startWorkoutBtn = document.getElementById("startWorkoutBtn");
const exerciseModal = document.getElementById("exerciseModal");
const closeModal = document.getElementById("closeModal");

startWorkoutBtn.addEventListener("click", () => {
    exerciseModal.classList.add("active");
});

closeModal.addEventListener("click", () => {
    exerciseModal.classList.remove("active");
});

// Close when clicking outside the modal
exerciseModal.addEventListener("click", (event) => {
    if (event.target === exerciseModal) {
        exerciseModal.classList.remove("active");
    }
});

// Close with Escape key
document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        exerciseModal.classList.remove("active");
    }
});