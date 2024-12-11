function showLogin() {
    document.getElementById('loginModal').style.display = 'block';
    document.getElementById('registerModal').style.display = 'none';
}

function showReg() {
    document.getElementById('loginModal').style.display = 'none';
    document.getElementById('registerModal').style.display = 'block';
}

function closeReg() {
    document.getElementById('registerModal').style.display = 'none';
}

function closeLogin() {
    document.getElementById('loginModal').style.display = 'none';
}

function showCart() {
    document.getElementById('cart_items_container').style.display = 'block';
}

function closeCart() {
    document.getElementById('cart_items_container').style.display = 'none';
}


window.onclick = function(event) {
    if (event.target == loginModal) {
        closeLogin()
    }
    if (event.target == registerModal) {
        closeReg()
    }
    if (event.target == cart_items_container) {
        closeCart()
    }
}

window.onload = function() { 

    // Поиск элемента с ошибкой
    const logError = document.getElementById('ErrorForm'); 
    const regError = document.getElementById('ErrorForm2');

    // Проверяем, нужно ли закрыть эти ебанные формы
    const loginClosed = sessionStorage.getItem('loginClosed') === 'true';
    const regClosed = sessionStorage.getItem('regClosed') === 'true';

    // Форма с Входом
    if (logError === null || loginClosed) { 
        closeLogin(); 
    } else { 
        showLogin(); 
        sessionStorage.setItem('loginClosed', 'true');
    } 

    // Форма с Регистрацией
    if (regError === null || regClosed) { 
        closeReg(); 
    } else { 
        showReg();
        sessionStorage.setItem('regClosed', 'true'); 
    } 

    // Отслеживание события отправки формы
    document.getElementById('loginModal').addEventListener('submit', function() {
        sessionStorage.setItem('loginClosed', 'false');
    });

    document.getElementById('registerModal').addEventListener('submit', function() {
        sessionStorage.setItem('regClosed', 'false');
    });
};