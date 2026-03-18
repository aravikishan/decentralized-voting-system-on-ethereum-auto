document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.navbar-nav');

    navToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');
    });

    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                form.classList.add('was-validated');
            }
        }, false);
    });

    // Dynamic content loading
    function loadCandidates() {
        fetch('/api/candidates')
            .then(response => response.json())
            .then(data => {
                const candidateSelect = document.getElementById('candidate');
                data.forEach(candidate => {
                    const option = document.createElement('option');
                    option.value = candidate.id;
                    option.textContent = `${candidate.name} (${candidate.party})`;
                    candidateSelect.appendChild(option);
                });
            });
    }

    if (document.getElementById('candidate')) {
        loadCandidates();
    }
});
