// Form Loading Animation
const form = document.getElementById('predictForm');
const submitBtn = document.getElementById('submitBtn');

if (form) {
    form.addEventListener('submit', function () {
        submitBtn.textContent = '⏳ Predicting...';
        submitBtn.disabled = true;
        submitBtn.style.background = '#888';
    });
}

// Input validation — highlight empty fields
const inputs = document.querySelectorAll('input[required]');
inputs.forEach(input => {
    input.addEventListener('blur', function () {
        if (this.value === '') {
            this.style.borderColor = '#e53935';
        } else {
            this.style.borderColor = '#43a047';
        }
    });
});

// Auto fade-in animation
document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll(
        '.result-card, .predict-container, .feature-card, .stat-card'
    );
    cards.forEach((card, i) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.5s ease ${i * 0.1}s,
                                  transform 0.5s ease ${i * 0.1}s`;
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });
});