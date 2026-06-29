
console.log("dashboard loaded 😎🔥")

const token =
localStorage.getItem(
    "token"
)

console.log(
    "TOKEN 😎🔥",
    token
)

if(!token){

    alert(
        "No token found 😭🔥"
    )

    window.location.href =
    "login.html"

}

/* =========================
   LOAD PROFILE 😎🔥
========================= */

async function loadProfile(){

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/leetcode/profile",

            {

                method:"GET",

                headers:{

                    Authorization:
                    `Bearer ${token}`

                }

            }

        )

        console.log(response)

        if(response.status === 401){

            alert(
                "Token invalid 😭🔥"
            )

            localStorage.removeItem(
                "token"
            )

            window.location.href =
            "login.html"

            return

        }

        const data =
        await response.json()

        console.log(data)

        document.getElementById(
            "profileCard"
        ).innerHTML = `

        <div class="stat-card easy">

            <h3>Easy 😎🔥</h3>

            <p>${data.easy_solved}</p>

        </div>

        <div class="stat-card medium">

            <h3>Medium 🚀</h3>

            <p>${data.medium_solved}</p>

        </div>

        <div class="stat-card hard">

            <h3>Hard 😭🔥</h3>

            <p>${data.hard_solved}</p>

        </div>

        <div class="stat-card">

            <h3>Total</h3>

            <p>${data.total_solved}</p>

        </div>

        <div class="stat-card">

            <h3>Ranking</h3>

            <p>${data.ranking}</p>

        </div>

        <div class="stat-card">

            <h3>Contest Rating</h3>

            <p>${data.contest_rating}</p>

        </div>

        `

    }

    catch(error){

        console.log(error)

        alert(
            "Profile loading failed 😭🔥"
        )

    }

}

/* =========================
   SYNC PROFILE 😎🔥
========================= */

document
.getElementById(
    "syncBtn"
)
.addEventListener(
"click",
async ()=>{

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/leetcode/sync",

            {

                method:"POST",

                headers:{

                    Authorization:
                    `Bearer ${token}`

                }

            }

        )

        const data =
        await response.json()

        console.log(data)

        alert(
            data.message
        )

        loadProfile()

    }

    catch(error){

        console.log(error)

        alert(
            "Sync failed 😭🔥"
        )

    }

})

/* =========================
   LOGOUT 😎🔥
========================= */

document
.getElementById(
    "logoutBtn"
)
.addEventListener(
"click",
()=>{

    localStorage.removeItem(
        "token"
    )

    window.location.href =
    "login.html"

})

loadProfile()

