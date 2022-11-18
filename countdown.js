const getTime = dateTo => {
    let now = new Date(),
        time = (new Date(dateTo) - now + 1000) / 1000,
        seconds = ('0' + Math.floor(time % 60)).slice(-2),
        minutes = ('0' + Math.floor(time / 60 % 60)).slice(-2),
        hours = ('0' + Math.floor(time / 3600 % 24)).slice(-2),
        days = Math.floor(time / (3600 * 24));
 
    return {
        seconds,
        minutes,
        hours,
        days,
        time
    }
};
 
const countdown = (dateTo, element) => {
    const item = document.getElementById(element);
 
    const timerUpdate = setInterval( () => {
        let currenTime = getTime(dateTo);
        item.innerHTML =`
            <div class="flex-container">
                <div>
                    <div class="countdown-container">
                        <div class="number">
                            ${currenTime.days}
                        </div>
                        <div class="concept">
                            Días
                        </div>
                    </div>
                </div>
                <div class="col-lg-2">
                    <div class="countdown-container">
                        <div class="number">
                            ${currenTime.hours}
                        </div>
                        <div class="concept">
                            Horas
                        </div>
                    </div>
                </div>
                <div class="col-lg-2">
                    <div class="countdown-container">
                        <div class="number">
                            ${currenTime.minutes}
                        </div>
                        <div class="concept">
                            Minutos
                        </div>
                    </div>
                </div>
                <div class="col-lg-2">
                    <div class="countdown-container">
                        <div class="number">
                            ${currenTime.seconds}
                        </div>
                        <div class="concept">
                            Segundos
                        </div>
                    </div>
                </div>
            </div>`;
 
        if (currenTime.time <= 1) {
            clearInterval(timerUpdate);
            alert('Fin de la cuenta '+ element);
        }
 
    }, 1000);
};

var date = new Date()
var new_date1 = new Date(date)


countdown(new_date1, 'countdown1');



//Local Storage
let cuenta = localStorage.setItem("minutos", new_date1.setMinutes(date.getMinutes() + 2)),
    cuenta2 = localStorage.setItem("horas", new_date1.setHours(date.getHours() + 2)),
    cuenta3 = localStorage.setItem("dias", new_date1.setDate(date.getDate() + 6));
    
let ambulanceButton = document.getElementById("ambulance");
let verificador = localStorage.getItem("sesion");
if (verificador == "true"){
    ambulanceButton.innerHTML=`<button id="ambulance" class="button"><a href="./pages/Ambulancia.html">Ambulancia</a>
    </button>`
}