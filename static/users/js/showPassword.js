const buttons = document.getElementsByClassName('toggle-password');
const inputs = [document.getElementById('id_password'), document.getElementById('id_repeat_password')]

Array.from(buttons).map(b => {
    b.onclick = () => {
        inputs.map(input => {

            if (input.type === 'password') {
                input.type = 'text';
            } else {
                input.type = 'password';
            }
        })
    }
})