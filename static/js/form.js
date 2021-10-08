document.getElementById('id_username').placeholder = "Nom d'utilisateur"
document.getElementById('id_email').placeholder = "E-mail"
var pass1 = document.getElementById('id_password1')
var pass2 = document.getElementById('id_password2')

pass1.placeholder = "Mot de passe"
pass2.placeholder = "Confirmer le mot de passe"



$(document).on('change', '#id_password1', function () {

	if (pass1 != pass2) {
		document.getElementById('sub').disabled = true
	}
	else {
		document.getElementById('sub').disabled = false
	}
});

$(document).on('click', '#id_password2', function () {

	if (pass1 === pass2) {
		document.getElementById('sub').disabled = false
	}
	else {
		document.getElementById('sub').disabled = true
	}
});
