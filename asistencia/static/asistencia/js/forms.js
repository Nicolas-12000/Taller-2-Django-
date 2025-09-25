// JS helper for asistencia forms: add form-control to appropriate inputs but skip checkboxes/radios/hidden
document.addEventListener('DOMContentLoaded', function() {
	try {
		const inputs = document.querySelectorAll('input, textarea, select');
		inputs.forEach(input => {
			const t = (input.type || '').toLowerCase();
			if (['checkbox', 'radio', 'hidden', 'file'].includes(t)) return;
			if (!input.classList.contains('form-check-input')) {
				input.classList.add('form-control');
			}
		});
		console.log('asistencia forms loaded and styled');
	} catch (e) {
		console.error('Error initializing asistencia forms JS', e);
	}
});
