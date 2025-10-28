document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm'); //validar login
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const senha = document.getElementById('senha').value;
            
            if (!validarSenha(senha)) {
                e.preventDefault();
                alert('A senha deve ter pelo menos 6 caracteres, incluindo 1 letra maiúscula, 1 número e 1 caractere especial');
            }
        });
    }

  

    function validarSenha(senha) {
        const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]).{6,}$/;
        return regex.test(senha);
    }
});