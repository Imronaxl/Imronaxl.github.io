  function closeAbout() {
            const aboutModal = document.getElementById("aboutModal");
            aboutModal.style.display = "none";
        }

      function openAbout() {
            const aboutModal = document.getElementById("aboutModal");
            aboutModal.style.display = "block";
        }
       function toggleNav() {
            const sidebar = document.getElementById("mySidebar");
            sidebar.style.width = sidebar.style.width === "250px" ? "0" : "250px";
        }

       function closeNav() {
            document.getElementById("mySidebar").style.width = "0";
        }

  function logout() {
        fetch('http://192.168.43.57:5000/logout')
            .then(response => {
                if (response.ok) {
                    return response.text();
                } else {
                    throw new Error('Ошибка при выполнении запроса');
                }
            })
            .then(data => {
                console.log(data);
                window.location.href = "Autorezation.html";
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    fetch('http://192.168.43.57:5000/get_login')
        .then(response => response.json())
        .then(data => {
            const userLogin = document.getElementById('userLogin');
            if (data.login == '') {
                window.location.href = "Autorezation.html";
            } else {
                userLogin.textContent = data.login;
            }
        })
        .catch(error => {
            userLogin.textContent = "Оффлайн";
        });
 function simulateLoading() {
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 7;
            if (progress > 100) {
                clearInterval(interval);
                document.getElementById("loader-wrapper").style.display = "none";
                document.getElementById("black-bg").style.display = "none";
                document.getElementById("main-content").style.display = "block";
            }
            document.getElementById("progressText").textContent = `${Math.round(progress)}%`;
            updateLoader(progress); // Вызываем функцию для обновления анимации спрайта
        }, 100);
    }
  function updateLoader(progress) {
        const loader = document.getElementById('loader');
        const degrees = progress * 0.6; // Преобразуем процент в градусы для изменения цвета
        const hue = (progress / 100) * 120; // Преобразуем процент в градусы для изменения оттенка
        loader.style.transform = `rotate(${degrees}deg)`; // Поворачиваем кружок
        loader.style.backgroundColor = `hsl(${hue}, 70%, 50%)`; // Изменяем цвет круга в зависимости от процента
    }

    simulateLoading();
fetch('http://192.168.43.57:5000/get_info_user')
    .then(response => response.json())
    .then(data => {
        const userLogin = document.getElementById('user_login');
        const solvedTasks = document.getElementById('solvedTasks');
        userLogin.textContent = data.login;
        solvedTasks.textContent = data.count;
        const elements = document.querySelectorAll('[id*="user_name"]');
        elements.forEach(element => {
            element.textContent = data.name;
        });

    })
    .catch(error => {
        console.error('Error:', error);
    });

    fetch('http://192.168.43.57:5000/get_packages')
    .then(response => response.json())
    .then(data => {
        const packagesDiv = document.getElementById('packages');
        data.forEach(package => {
            const packageElement = document.createElement('div');
            packageElement.classList.add('package');
            if (package.verdict.includes("неправильный ответ")) {
                packageElement.innerHTML = `<h3>${package.name}</h3><p class="wrong">${package.verdict}</p>`;
                
            }
            else {
            packageElement.innerHTML = `<h3>${package.name}</h3><p class="accepted">${package.verdict}</p>`;
            } 
               packagesDiv.appendChild(packageElement);
        });
    })
    .catch(error => console.error('Error:', error));



        function showFullText(newsId) {
            const fullText = document.getElementById(newsId + "Full");
            const showBtn = document.querySelector(`#${newsId}Container .show-btn`);
            const hideBtn = document.querySelector(`#${newsId}Container .hide-btn`);
        
            fullText.style.display = "block";
            showBtn.style.display = "none";
            hideBtn.style.display = "inline-block";
            fullText.style.maxHeight = fullText.scrollHeight + "px"; // Установка максимальной высоты для показа всего текста
        
        }
        
        function hideFullText(newsId) {
            const fullText = document.getElementById(newsId + "Full");
            const showBtn = document.querySelector(`#${newsId}Container .show-btn`);
            const hideBtn = document.querySelector(`#${newsId}Container .hide-btn`);
            fullText.style.maxHeight = 0; // Установка максимальной высоты 0, чтобы скрыть текст
        
            fullText.style.display = "none";
            showBtn.style.display = "inline-block";
            hideBtn.style.display = "none";
        }
           
        fetch('http://192.168.43.57:5000/get_task_description1')
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при запросе данных');
            }
            return response.json();
        })
        .then(data => {
            const taskDetails = document.querySelector('.task-details');
            const taskDescription = document.createElement('pre');
            taskDescription.textContent = data.taskDescription;
            taskDetails.appendChild(taskDescription);
        })
        .catch(error => {
            console.error('Error:', error);
        }); 
           