const button = document.getElementById('user-menu-button');
const dropdown = document.getElementById('user-dropdown');

if (button && dropdown) {

    button.addEventListener('click', (event) => {

        event.stopPropagation();

        dropdown.classList.toggle('hidden');

    });

    window.addEventListener('click', (event) => {

        if (!button.contains(event.target) &&
            !dropdown.contains(event.target)
        ) {
            dropdown.classList.add('hidden');
        }

    });

}