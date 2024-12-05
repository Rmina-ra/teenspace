
function triggerFileInput() {
    document.getElementById('fileInput').click();
}


function previewImage() {
    const fileInput = document.getElementById('fileInput');
    const profileImage = document.getElementById('profileImage');
    const defaultIcon = document.getElementById('defaultIcon');

    // Проверяем, загружен ли файл
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        // Чтение файла и отображение в контейнере
        reader.onload = function(e) {
            profileImage.src = e.target.result;
            profileImage.style.display = 'block'; // Показываем изображение
            defaultIcon.style.display = 'none';  // Скрываем иконку пользователя
        };

        reader.readAsDataURL(fileInput.files[0]); // Чтение файла как URL
    }
}

function toggleGlow(button) {
    button.classList.toggle("glowing");
}

  document.addEventListener("DOMContentLoaded", function() {
    fetchWeatherData();
});

document.addEventListener("DOMContentLoaded", function() {
  fetchWeatherData();
});
