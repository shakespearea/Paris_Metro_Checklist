
function toggleLine(header) {
    header.closest('.card').classList.toggle('open')
}

function updateProgress() {
    const all = document.querySelectorAll('.station-btn').length;
    const done = document.querySelectorAll('.station-btn.visited').length;
    const pct = all ? Math.round(done / all * 100) : 0;
    document.getElementById('progressFill').style.width = pct + '%';
    document.getElementById('pct').textContent = pct + '%';
}

document.addEventListener('DOMContentLoaded', () => {
    updateProgress();
});